#n번째 원반을 x, y로 옴기는데(출력) 1-(n-1)까지 원반을 x에서 중간 기둥(x, y말고 빈 자리)으로 옮기고 
#출력하고 나서 1-(n-1)까지 원반을 중간 기둥에서 y까지 옮긴다라는 의미 내포.
def move(n, x, y): #출력은 n을 x에서 y로 옮김
  if(n > 1):
    move(n-1, x, 6 - x - y)
  print(f"[{n}]을(를) {x}에서 {y}로 옮김.")
  if(n > 1):
    move(n-1, 6 - x - y, y)

while(True):
   try:
     n = int(input("하노이의 탑\n원반 개수 : "))
     if n < 1:
       raise ValueError
   except ValueError:
     continue
   break

move(n, 1, 3)  
