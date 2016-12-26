from Relation import Relation


def attributes_match(attributes1, attributes2) :
  if len(attributes1) != len(attributes2):
    return False
  
  for attr1, attr2 in zip(attributes1, attributes2) :
    if attr1.getName() != attr2.getName() or attr1.getType() != attr2.getType() :
      return False
  
  return True

def check_matching_attributes(calling_rel, attributes1, attributes2) :
  if not attributes_match(attributes1, attributes2) :
    error_str = 'attributes from subrelation1 does not match attributes from subrelation2\n'
    error_str = error_str+'\tAttributes from subrelation1 :\n'+str_attributes(attributes1, '\t\t')
    error_str = error_str+'\tAttributes from subrelation2 :\n'+str_attributes(attributes2, '\t\t')
    calling_rel.error(error_str)
  return attributes1

def check_relation(calling_rel, checked_relation, rel_name='checked_relation') :
  if not isinstance(checked_relation, Relation) :
    calling_rel.error('Argument '+rel_name+' must be an object of type Relation')
  return checked_relation

def str_attributes(attributes, prefix='') :
  s = ''
  for attr in attributes :
    s = s+prefix+str(attr)+'\n'
  return s
