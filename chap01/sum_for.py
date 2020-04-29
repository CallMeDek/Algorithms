print("The sum of 1 through n")
n = int(input("n : "))
sum = 0
for i in range(1, n+1):
  sum += i

print(f"The sum of 1 through {n} is {sum}")
