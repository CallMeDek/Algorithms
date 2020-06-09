from Sort.Sort_template import Sort

class Merge(Sort):
  def sort(self):
    print("Iterative sort is not implemented yet so it starts recurvie sorting automatically.")
    start = 0
    end = self.get_list_len()-1
    self.recursive_sort(start, end)   

 
  def get_list_len(self):
    return super().size   
 

  def recursive_sort(self, start, end):
    def merge(x, start1, start2, end1, end2):
      ptr1, ptr2 = start1, start2;
      temp_x = []
      while(ptr1 < end1 and ptr2 < end2):
        if(x[ptr1] > x[ptr2]):
          temp_x.append(x[ptr2])
          ptr2 += 1
        else:
          temp_x.append(x[ptr1])
          ptr1 += 1
      while(ptr1 < end1):
        temp_x.append(x[ptr1])
        ptr1 += 1
      while(ptr2 < end2):
        temp_x.append(x[ptr2])
        ptr2 += 1          
      for i, ele in enumerate(temp_x):
        x[i + start1] = ele            
  
    if (start >= end):
      return
    x = super().list
    middle = int((start + end)/2)
    self.recursive_sort(start, middle)
    self.recursive_sort(middle+1, end)
    merge(x, start, middle+1, middle+1, end+1)
