import sys


class IntStack:
  def __init__(self, max_):
    self.ptr = 0
    try:
      self.max = int(max_)
    except ValueError:
      print("MAX value is not avaliable")
      sys.exit(1)
