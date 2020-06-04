from Sort.Sort_template import Sort

class Selection(Sort):
  def get_list_len(self):
    return super().size
 

  def sort(self):
    x = super().list
    size = super().size
    for i in range(size):
      min_index = i
      for j in range(i+1, len(x)):
        if x[j] < x[min_index]:
          min_index = j
      x[i], x[min_index] = x[min_index], x[i]


  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()
