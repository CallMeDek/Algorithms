from Sort.Sort_template import Sort

class HeapSort(Sort):
  def sort(self):
    def heapify(x, left, right):
      parent = left
      root = x[left]
      while(parent < (right + 1)//2):
        child_left = parent * 2 + 1
        child_right = child_left + 1
        if(child_right <= right):
          child = child_left if x[child_left] > x[child_right] else child_right
        else:
          child = child_left
        if(root >= x[child]):
          break
        x[parent] = x[child]
        parent = child
      x[parent] = root

    end = self.get_list_len()
    x = super().list
    for i in range(int((end-1)//2), -1, -1):
      heapify(x, i, end-1)
    for i in range(end-1, 0, -1):
      x[0], x[i] = x[i], x[0]
      heapify(x, 0, i-1)
 

  def get_list_len(self):
    return super().size   
 

  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()
