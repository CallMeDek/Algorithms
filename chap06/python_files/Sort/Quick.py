from Sort.Sort_template import Sort
from Stack.int_stack import IntStack

class Quick(Sort):
  def sort(self):
    def check(obj, return_value):
      print(f"{obj.__name__} is Failed.") if return_value == -1 else print("", end="")

    start = 0
    size = self.get_list_len()
    lstack = IntStack(size - start + 1)
    rstack = IntStack(size - start + 1)
    l_v = lstack.Push(start)
    check(lstack, l_v) 
    r_v = rstack.Push(size-1)
    check(rstack, r_v)
    x = super().list
    while(lstack._IsEmpty()==False):
      pl = start = lstack.Pop()
      check(lstack, pl)
      pr = end = rstack.Pop()
      check(rstack, pr)
      middle_value = x[int((pl + pr)//2)] 
      while(pl <= pr):
        while(x[pl] < middle_value): 
          pl += 1
        while(x[pr] > middle_value):
          pr -= 1
        if(pl <= pr):
          x[pl], x[pr] = x[pr], x[pl]
          pl += 1
          pr -= 1
      if(start < pr):
        l_v = lstack.Push(start)
        check(lstack, l_v)
        r_v = rstack.Push(pr)
        check(rstack, r_v)
      if(pl < end):
        l_v = lstack.Push(pl)
        check(lstack, l_v)
        r_v = rstack.Push(end)
        check(rstack, r_v)
    del lstack
    del rstack


  def get_list_len(self):
    return super().size   
 

  def recursive_sort(self, start, end):
    def partition(a_list, start, end):
      x = a_list
      left = start; right = end;
      middle_value = x[int((left + right) / 2)]
      while(left <= right):
        while(middle_value > x[left]):
          left += 1
        while(middle_value < x[right]):
          right -= 1
        if(left <= right):
          x[left], x[right] = x[right], x[left]
          left += 1
          right -= 1
      return left, right

    x = self.list
    left, right = partition(x, start, end)
    if(start < right): 
      self.recursive_sort(start, right)
    if(end > left):
      self.recursive_sort(left, end)
