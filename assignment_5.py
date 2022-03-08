#assignment 5

#question 1
from tkinter import*
#created a function to calculate the tax by aquiring the values using .get()
def getvals():
    tax=(int(netprice.get())-int(originalcost.get()))*100/int(originalcost.get())
    print("The tax is",tax)
    return tax
    
win=Tk()
win.title("Gst Tax Finder Calculator")
win.geometry('600x300')
#labels
lbl=Label(win,text="Tax Calculator")
lbl.pack()
lbl1=Label(win,text="Net Price")
lbl1.place(x=57,y=57)
lbl2=Label(win,text="Original Cost")
lbl2.place(x=57,y=117)
#entry and variables
netprice=StringVar()
originalcost=StringVar()
en1=Entry(win,textvariable=netprice)
en1.place(x=177,y=57)
en2=Entry(win,textvariable=originalcost)
en2.place(x=177,y=117)
#Button
Button(text="Submit",command=getvals).place(x=177,y=177)
win.mainloop()
#question 1 completed

#question 2
from tkinter import*
import calendar
def showcalendar():
    new_win=Tk()
    new_win.config(background="white")
    new_win.title("Calendar")
    new_win.geometry("500x600")
    year=int(year1.get())
    cal_co=calendar.calendar(year)
    cal_year=Label(new_win,text=cal_co).grid(row=5,column=1,padx=20)
    new_win.mainloop()
    
win=Tk()
win.geometry("600x300")
win.title("Calendar")
#Label
lbl=Label(win,text="Calendar",bg="red",fg="white").pack()
lbl1=Label(win,text="Enter an Year").place(x=257,y=77)
#Entry
year1=StringVar()
en1=Entry(win,textvariable=year1).place(x=207,y=107)
#Button
button=Button(win,text="Submit",command=showcalendar).place(x=257,y=137)
win.mainloop()
#question 2 completed

#question 3
from tkinter import*
root=Tk()
root.title("Calculator")
root.geometry("600x300")
#Function - here i created functions where they get the numbers and print after 
#performing the calculation
def sumvals():
    print("The sum is-",int(number1.get())+int(number2.get()))
def multiplyvals():
    print("The product is-",int(number1.get())*int(number2.get()))
def subtractvals():
    print("The subraction is-",int(number1.get())-int(number2.get()))         
def dividevals():
    print("The division is-",int(number1.get())/int(number2.get()))    
    
#Label
lbl11=Label(root,text="A Basic Calculator").place(x=187,y=10)
lbl22=Label(root,text="First write the numbers then select the operation").place(x=117,y=50)
lbl1=Label(root,text="Number 1").place(x=117,y=117)
lbl2=Label(root,text="Number 2").place(x=117,y=177)
#Entry
number1=StringVar()
number2=StringVar()
en1=Entry(root,textvariable=number1).place(x=187,y=117)
en2=Entry(root,textvariable=number2).place(x=187,y=177)
#Button
sumbutton=Button(root,text="+",command=sumvals).place(x=150,y=237)
multiplybutton=Button(root,text="*",command=multiplyvals).place(x=210,y=237)
subtractbutton=Button(root,text="-",command=subtractvals).place(x=270,y=237)
divisionbutton=Button(root,text="/",command=dividevals).place(x=330,y=237)
root.mainloop()
#question 3 completed

#question 4
def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        
        return quicksort(less)+equal+quicksort(greater) 
    else:  
        return array

k=0
a=[]  #list to store marks of the students
while k<1:
    marks=int(input("Enter the marks-"))
    a.append(marks)
    yes_no=input("Please enter y if you want to go further to stop press n-")
    if yes_no=='n':
        k=1
a=quicksort(a)
print(a)
#question 4 completed

#question 5
#(a)
print("----------(a)----------")
a=[]
n=0
#you can input as many elements you would like to have
while n<1:
    x=int(input("Give a number:"))
    a.append(x)
    yes_no=input("if you want more elements in the array press y for yes,n for no:")
    if yes_no=='n':
        n=1        
#now we have an array and we will sort it    
#using bubble sort
def bubble_sort(a):
    z=len(a)
    while z>0:
        for i in range(len(a)-1):
            if a[i]>=a[i+1]:
                temp=a[i+1]
                a[i+1]=a[i]
                a[i]=temp
            else:
                continue    
        z-=1
bubble_sort(a)
print(a)
print("The array has been successfully sorted")
#(b)
print("-------------(b)----------")
print("Now binary search-")
def binary_search(low,high,a,b):
    while low<=high:
        mid=(low+high)//2
        if b>mid:
            return binary_search(a[mid+1],high,a,b)
        elif b<mid:
            return binary_search(low,a[mid-1],a,b)
        else:
            return mid
    return 0
b=int(input("Please give a number you want to search-"))
c=binary_search(0,len(a)-1,a,b)
if c==0:
    print("Error,Number not found in the array.")
else:
    print("Number found-",c,"is the index of the given element")

#(c)
print("---------------(c)-----------")
print("No. of times the given number occurs--")
count=0
for i in a:
    if i==b:
        count+=1
    else:
        continue
print(count)
#question 5 completed
