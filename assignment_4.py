#assignment4

#q1
#tower of hanoi
#here we have 3 pegs namely A B C and we want all the disks in A to
#be transferred to C. We can't keep a smaller disk below a larger disk
#n is no. of disks
#here A is the starting peg,B is auxillary and C is final peg
print("-------------1--------------")
def Towerofhanoi(n,Start,Extra,End):
    if n>0:
        Towerofhanoi(n-1,Start,End,Extra)
        print("Transfer disk from",Start,"to",End)
        Towerofhanoi(n-1,Extra,Start,End)
        
Towerofhanoi(3,"A","B","C")

#q2
#Pascal's triangle

#using iteration
print("-------------2(A)------------")
print("Using iteration-")
#making factorial function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#making ncr function
def ncr(n,r):
    x=factorial(n)/(factorial(n-r)*factorial(r))
    return int(x)    

row=int(input("Give the no. of rows-"))
i=1
while i<=row:
    print(" "*(row-i),end="")
    j=0
    while j<i:
        print(ncr(i-1,j)," ",end="")
        j+=1
    print("\n")
    i+=1

#using recursion
print("--------------2(B)-------------")
print("Using recursion-")
def pascals_triangle(n,s,m):
    if n==0:
        print(" "*(s-1),1,"\n")
        
        return pascals_triangle(n+1,s,m)
    elif n==m:
        print("Done!")
        n=-1
        
    else:
        print(" "*(s-n),end="")
        x=0
        while x<=n:
            print(ncr(n,x),"",end="")
            x+=1
        print("\n")
        if n==m:
            print("Done!")
            n=-2
        return pascals_triangle(n+1,s,m)
    
        
m=int(input("Please give no. of rows-"))
n=m-m
s=m+m
pascals_triangle(n,s,m)

#q3

print("-------------3(A)-----------")
def fun(a,b):
    quotient=a//b
    remainder=a%b
    print("The quotient is-",quotient)
    print("The remainder is-",remainder)
    list=[quotient,remainder]
    return list

a=int(input("Please give the first number-"))
b=int(input("Please give the second number-"))
c=fun(a,b)
print(c)
print("Callable-",callable(fun))

print("-------------3(B)-------------")
print("a is zero-",a==0)
print("b is zero-",b==0)
print("quotient is zero-",c[0]==0)
print("remainder is zero-",c[1]==0)
if(a==0):
    print("a is zero")

print("-------------3(C)-------------")
#adding 4 5 6 in the result
d=[4,5,6]
c=c+d
print(c)
alist=[]
for i in c:
    if i>4:
        alist.append(i)
print("The values greater than 4-",alist)

print("-------------3(D)-------------")
#converted the list to a set
aset=set(alist)
print(aset)

print("-------------3(E)-------------")
#immutable set
immutable_set=frozenset(aset)
print("The required immutable set",immutable_set)

print("-------------3(F)-------------")
#max value from the set
#hash value
maxval=0
for i in immutable_set:
    if i>maxval:
        maxval=i
print("The required max value is-",maxval)
print("The required hash value is-",hash(maxval))

#q4
print("--------------4---------------")
class Student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def __del__(self):
        print("Destructor called,The object is destroyed.")


p1=Student("Tony",7)
print(p1.name)
print(p1.rollnum)

#q5

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

p1=Employee("Mehak",40000)
p2=Employee("Ashok",50000)
p3=Employee("Viren",60000)

print("-------------5(A)---------")
#updating salary of Mehak to 70000
p1.salary=70000
print("The updated salary of Mehak is-",p1.salary)

print("-------------5(B)---------")
#deleting the record of Viren
del p1
print("The record of Viren has been successfully deleted-")


#q6
#here we use the concept of anagrams

print("-------------6-------------")
def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("Please give a word-")
Possible_words=anagram(George_word)
Barbie_word=input("Give a word-")
print("Possible Words-",Possible_words)
print("If Barbie's word lies in the list,then their friendship is real.")

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")
    

        


