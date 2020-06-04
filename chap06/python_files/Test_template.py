import time


def test(sorting_obj, mode="i"):
  if mode in ["r", "i"] == False:
    print("Inaccurate mode value. Exit.")
    return

  get_time = lambda: time.time()
  get_consumed_time = lambda x, y: x - y

  sorting_obj.get_values()
  start = get_time()
  if mode == "i":
    sorting_obj.sort()
  else:
    sorting_obj.recursive_sort(0, sorting_obj.get_list_len()-1)
  end = get_time()
  print("오름차순 정렬")
  sorting_obj.print_values()
  consumed_time = get_consumed_time(end, start)
  print(f"{sorting_obj.__class__.__name__} - Time: {'%.3f'%(consumed_time)}")  
