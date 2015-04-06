from bar import foo
from bar import foo
from bar import foo
from bar import foo
from bar import foo
from bar import foo
from bar import foo
from bar import foo
from bar import foo
from bar import foo

def long_method(self):
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  foo()
  # 21
  foo()

def baz():
  if foo and bar:
    print "Foo and bar"
  elif foo:
    print "Foo"
  elif bar:
    print "Bar"
  else:
    print "None"
  pass

def duplicated_baz():
  if foo and bar:
    print "Foo and bar"
  elif foo:
    print "Foo"
  elif bar:
    print "Bar"
  else:
    print "None"
  pass

def cyclomatically_complex():
  if foo and bar and baz or buzz:
    return True
  elif baz or foo and bar or buzz:
    [f for foo in bar]
  elif bar and baz or buzz and foo:
    return False

def high_param(foo, bar, baz, buzz, threshold=5):
  pass
