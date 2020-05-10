def card_conv(x, n, d):
  digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  digits_num = 0
  if(x == 0): 
    d.append(digits[0])
    digits_num += 1
  else:
    while(x > 0):
      d.append(digits[x % n]) 
      digits_num += 1
      x = x//n
  return digits_num


print("10진수를 기수 변환합니다.")
retry = 1
while(retry):
  char = []
  number = 1
  try:
    number = int(input("변환하는 음이 아닌 정수 : ")) 
    if number < 0:
      raise ValueError
  except ValueError as e:
    continue
  while(True):
    try: 
      cardinal_number = int(input("어떤 진수로 변환할까요?(2-36) : "))
      if (2 > cardinal_number) or (cardinal_number > 36):
        raise ValueError
      break
    except ValueError as e:
      continue
  digits_number = card_conv(number, cardinal_number, char);
  print(f"{cardinal_number}진수로는 ", end="")
  for i in range(digits_number-1, -1, -1):
      print(f"{char[i]}", end="")
  print()
  while(True):
    try:
      retry = int(input("한번 더 할까요?(1 ... 예/0 ... 아니오) : "))
      if retry not in [0, 1]:
        raise ValueError
    except ValueError as e:
      continue
    break
    
