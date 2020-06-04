from Sort.Shell import Shell, Shell2
from Test_template import test


def main():
  print("셸 정렬")
  shell1 = Shell()
  test(shell1)
  shell2 = Shell2()
  test(shell2, mode="r")
  

if __name__ == "__main__":
  main()

