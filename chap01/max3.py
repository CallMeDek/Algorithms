max = 0
print(f"Get the maximum value among three variables.", end="\n")
a = int(input("a : ").strip())
b = int(input("b : ").strip())
c = int(input("c : ").strip())
max = a
if(b > max): max = b
if(c > max): max = c
print(f"The maximum value is {max}", end="\n")
