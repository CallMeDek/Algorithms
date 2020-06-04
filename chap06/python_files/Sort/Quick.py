from Sort.Sort_template import Sort

class Quick(Sort):

  def sort(self):
    self.recursive_sort(0, len(self.a)-1) 


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
