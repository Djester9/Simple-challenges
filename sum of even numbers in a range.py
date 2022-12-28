"""
#this code allows the user to input a number and find the sum of all numbers between 0 and picked number


num = input('which num: ') #allow user to pick number 
sum = 0 #define varaible as 'sum' which = 0

num = (int(num))
num += 1 #adding one number to users num to make more user friendly. (as range only goes upto to but does not include picked num 

for e in range(1, num):
    if e % 2 == 0:
        sum += e
        
        
print(sum)
    
