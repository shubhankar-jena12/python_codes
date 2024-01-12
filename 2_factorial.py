fact=1
num=5

if num<0:
    print("factorial of -ve num doesn't exist")
elif num==0:
    print("fact of 0 is 1")
else:
    for i in range(1,num+1):
         fact=fact*i
print("the factorial of ", num ,"is" ,fact)