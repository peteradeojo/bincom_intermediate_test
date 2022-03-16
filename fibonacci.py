#!python

def fibonnacci(n):
  a = 1
  b = 1
  bridge = 0
  if n > 1:
    print(a)
    print(b)
  
  def fix(a,b):
    bridge = a
    a = b
    b = bridge + b
    if (b < n):
      print(b)
      fix(a,b)

  fix(a,b)

fibonnacci(23)
