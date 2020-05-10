prime = [2, 3]
counter = 0
for i in range(5, 1001, 2):
  ptr = 1
  flag = 1
  while(prime[ptr] * prime[ptr] <= i):
    counter += 1
    if(i % prime[ptr] == 0):
      flag = 0
      break
    ptr += 1  
  if(flag):
    prime.append(i)

for j in range(len(prime)):
  print(prime[j], end=" ") 
print(f"곱셈과 나눗셈을 실행한 횟수: {counter}")
