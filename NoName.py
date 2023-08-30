num = int(input())  
sum = 0

for i in range(num):
     d = num % 10
     sum = sum + d
     num = num //10
print('finish')
    
print(sum)