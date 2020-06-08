from Sort.Quick import Quick
from Test_template import test

def main():
  print("퀵 정렬")
  quick = Quick()
  test(quick)
  quick = Quick()
  test(quick, mode="r")


if __name__ == "__main__":
  main()

