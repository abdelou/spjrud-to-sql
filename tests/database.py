import sqlite3

def delete_database(database_name) :
  os.remove(database_name+'.db')

def create_database(database_name) :
  # create database from SQL TP, to run some tests
  database = sqlite3.connect(database_name+'.db')

  # get cursor
  cursor = database.cursor()

  # create table emp
  table_def = """
  empno INTEGER PRIMARY KEY,
  ename TEXT,
  job TEXT,
  mgr INTEGER,
  hiredate TEXT,
  sal FLOAT,
  comm FLOAT,
  deptno INTEGER NOT NULL
  """
  cursor.execute('CREATE TABLE emp ('+table_def+');')
  # fill table emp
  cursor.execute("insert into emp values (7839,'KING','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);");
  cursor.execute("insert into emp values (7698,'BLAKE','MANAGER',7839,'2001-05-01',2850,NULL,30);");
  cursor.execute("insert into emp values (7782,'CLARK','MANAGER',7839,'2001-06-09',2450,NULL,10);");
  cursor.execute("insert into emp values (7566,'JONES','MANAGER',7839,'2001-04-02',2975,NULL,20);");
  cursor.execute("insert into emp values (7654,'MARTIN','SALESMAN',7698,'2001-09-28',1250,1400,30);");
  cursor.execute("insert into emp values (7499,'ALLEN','SALESMAN',7698,'2001-02-20',1600,300,30);");
  cursor.execute("insert into emp values (7844,'TURNER','SALESMAN',7698,'2001-09-08',1500,0,30);");
  cursor.execute("insert into emp values (7900,'JAMES','CLERK',7698,'2001-12-03',950,NULL,30);");
  cursor.execute("insert into emp values (7521,'WARD','SALESMAN',7698,'2001-02-22',1250,500,30);");
  cursor.execute("insert into emp values (7902,'FORD','ANALYST',7566,'2001-12-03',3000,NULL,20);");
  cursor.execute("insert into emp values (7369,'SMITH','CLERK',7902,'2000-12-17',800,NULL,20);");
  cursor.execute("insert into emp values (7788,'SCOTT','ANALYST',7566,'2002-12-09',3000,NULL,20);");
  cursor.execute("insert into emp values (7876,'ADAMS','CLERK',7788,'2003-01-12',1100,NULL,20);");
  cursor.execute("insert into emp values (7934,'MILLER','CLERK',7902,'2002-01-23',1300,NULL,10);");
  cursor.execute("insert into emp values (7939,'PALMER','ANALYST',7902,'2012-01-23',1300,NULL,10);");
  cursor.execute("insert into emp values (7983,'LOPEZ','SALESMAN',7566,'2012-01-23',1500,600,20);");
  cursor.execute("insert into emp values (7994,'WILLIAMS','ANALYST',7698,'2012-01-23',950,NULL,30);");

  # create table dept
  table_def = """
  deptno INTEGER PRIMARY KEY,
  dname TEXT,
  loc TEXT
  """
  cursor.execute('CREATE TABLE dept ('+table_def+');')
  # fill table dept
  cursor.execute("insert into dept values (10, 'ACCOUNTING','NEW YORK');");
  cursor.execute("insert into dept values (20, 'RESEARCH','DALLAS');");
  cursor.execute("insert into dept values (30, 'SALES','CHICAGO');");
  cursor.execute("insert into dept values (40, 'OPERATIONS','BOSTON');");

  # create table salgrade
  table_def = """
  grade INTEGER PRIMARY KEY,
  losal INTEGER,
  hisal INTEGER
  """
  cursor.execute('CREATE TABLE salgrade ('+table_def+');')
  # fill table salgrade
  cursor.execute("insert into salgrade values (1,700,1200);");
  cursor.execute("insert into salgrade values (2,1201,1400);");
  cursor.execute("insert into salgrade values (3,1401,2000);");
  cursor.execute("insert into salgrade values (4,2001,3000);");
  cursor.execute("insert into salgrade values (5,3001,9999);");

  # save changes
  database.commit()
  database.close()
