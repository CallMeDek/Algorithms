from Sort.Shell import Shell, Shell2
import time


def main():
  print("셸 정렬")
  shell1 = Shell()
  test(shell1)
  shell2 = Shell2()
  test(shell2)
  

def test(sorting_obj):
  get_time = lambda: time.time()
  get_consumed_time = lambda x, y: x - y

  sorting_obj.get_values()
  start = get_time()
  sorting_obj.sort()
  end = get_time()
  print("오름차순 정렬")
  sorting_obj.print_values()
  consumed_time = get_consumed_time(end, start)
  print(f"{sorting_obj.__class__.__name__} - Time: {'%.3f'%(consumed_time)}")  


if __name__ == "__main__":
  main()

