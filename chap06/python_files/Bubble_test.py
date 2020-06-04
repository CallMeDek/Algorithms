from Sort.Bubble import Bubble1, Bubble2, Bubble3
from Test_template import test


def main():
  print("버블 정렬")
  bubble1 = Bubble1()
  test(bubble1, mode="r")

  bubble2 = Bubble2()
  test(bubble2, mode="r")

  bubble3 = Bubble3()
  test(bubble3, mode="r")

if __name__ == "__main__":
  main()
