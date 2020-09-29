print("task3.1")
def area ():
    pass
    
    
a=int(input("enter the no. of sticks"))
stick=[]
for i in range(a):
    x=int(input("enter the length of each sticks"))
    stick.append(x)
print(stick)
stick.sort(reverse = True) 
dim= [0,0]
i = 0
j = 0
while(i < a-1 and j < 2): 
 if (stick[i] == stick[i + 1]): 
    dim[j] = stick[i] 
    j += 1
    i += 1
 i += 1 
maxarea=dim[0]*dim[1]

if maxarea>0:
    print("max area is"+str(maxarea))
else:
    print("max area is -1")



print("task 3.2")
def arr():
    pass
n=int(input("enter the size of array"))

elements=[]

for i in range(n):
    x=int(input("enter the elements"))
    elements.append(x)
print(elements)



 
print("task 3.3")
def sports():
    pass

n=int(input("enter the value of X"))
m=int(input("enter the value of Y"))

a=int(n/2)  #no. of matches to win
b=n%2  #no. of matches to tie



print("number of matches required to win",a)





print("task 3.4")
def movie():
     pass

n=int(input("enter number of movies"))

L=[]
R=[]
movies=[]

for i in range(1,n+1):
    a=int(input("L"+str(i)+"-"))
    b=int(input("R"+str(i)+"-"))
    L.append(a)
    R.append(b)


    x=(a*b,b,n+1-i)
    movies.append(x)
m=max(movies)
j=movies.index(m)
print("movie",j+1)



print("task 3.5")
def small():
    pass

n=int(input("enter the size of array"))

elements=[]

for i in range(n):
    x=int(input("enter the elements"))
    elements.append(x)

print(elements)


x=min(elements)
total = (n-1)*x

print("output is:", total)
    
