# some functions usefull to run tests

# convert Relation to SQL request and exec request on given database
def exec_request(database_name, relation, print_sql=True, print_result=True) :
  import sqlite3
  
  sql = relation.toSQL()+';'
  if print_sql :
    print 'SQL Request :'
    print '"'+sql+'"'
  
  database = sqlite3.connect(database_name+'.db')
  cursor = database.cursor()
  tuples = cursor.execute(sql)
  
  if print_result :
    print_relation(relation.getAttributesName(), tuples)
  else :
    return tuples

# pretty print attributes name and tuples (format similar to mysql command line)
def print_relation(attributes, tuples) :
  # compute len for future checks
  attr_len = len(attributes)
  # get data and convert them to str
  rows = []
  for t in tuples :
    # check each tuple is same length than attributes
    t_len = len(t)
    if t_len != attr_len :
      raise Exception('Attribute length is "'+attr_len+'" but tuple length is "'+t_len+'"')
    # save tuple in list
    new_row = []
    for val in t :
      new_row.append(str(val))
    rows.append(new_row)
  
  # get max length for each column
  max = {}
  for attr in attributes :
    max[attr] = len(attr)
  
  for row in rows :
    for attr, val in zip(attributes, row) :
      l = len(val)
      if l > max[attr] :
        max[attr] = l
  
  # create separator
  separator = '+-'
  for attr in attributes :
    separator = separator + padding_left('', max[attr], '-') + '-+-'
  # remove last "-"
  separator = separator[:-1]
  
  # print header
  print separator
  line = '| '
  for attr in attributes :
    line = line + padding_left(attr, max[attr]) + ' | '
  # remove last " "
  line = line[:-1]
  print line
  print separator
  # print data
  for row in rows :
    line = '| '
    for attr, val in zip(attributes, row) :
      line = line + padding_left(val, max[attr]) + ' | '
    # remove last " "
    line = line[:-1]
    print line
  
  print separator

def padding_left(string, size, character=' ') :
  l = len(string)
  # if string is bigger, padding is empty
  if l > size :
    return string
  
  padding = ''
  for i in range(l, size) :
    padding = padding+character
  
  return padding+string
