import random
value = int(input()) 
for i in range(6):
 num1 = (value % pow(10,3))//pow(10,2)
 num2 = (value % pow(10,2))//pow(10,1)
 num3 = value % 10


 str1 =str(num1)     
 str2 = str(num2)    
 str3 = str(num3)    
 sum = str1+str2+str3    
 a = random.choice(sum) 
 b = random.choice(sum) 


 for i in range(100):
  if a==b:
   b=random.choice(sum)
  c=random.choice(sum)
  for i in range(100):
   if c==a or c==b:
    c=random.choice(sum)
 print(a,b,c)
  



