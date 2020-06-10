from Sort.Sort_template import Sort

class Count(Sort):
  def get_list_len(self):
    return super().size
 

  def sort(self):
    x = super().list
    size = self.get_list_len()
    b = [0 for _ in range(size+1)]
    f = [0 for _ in range(max(x)+1)]
    for i in range(size):
      f[x[i]] += 1
    for i in range(1, len(f)):
      f[i] += f[i-1]
    for i in range(size-1, -1, -1):
      b[f[x[i]]] = x[i]
      f[x[i]] -= 1
    for i in range(size):
      x[i] = b[i]
        
    
  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()
