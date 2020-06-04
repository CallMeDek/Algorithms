from Sort.Sort_template import Sort

class Insertion(Sort):
  def get_list_len(self):
    return super().size


  def sort(self):
    x = super().list
    size = super().size
    for i in range(1, size):
      tmp = x[i]
      j = i
      while(j > 0 and x[j-1] > tmp):
        x[j] = x[j-1]
        j -= 1
      x[j] = tmp


  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()
        
