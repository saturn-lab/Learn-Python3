#!/usr/bin/env python

class Fibs():
    def __init__(self):
      self.a = 0
      self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        fib=self.a
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == '__main__':
  fibs=Fibs()
	
  for f in fibs:
      if f > 100:
        print(f)
        break		