print("The sum of 1 through n")
n = int(input("n: "))

sum = 0
i = 1
while(i <= n):
  sum += i
  i += 1

print(f"The sum of 1 through {n} is {sum}")
