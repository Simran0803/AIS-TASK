1) grade code
p=50
O: p>75
A : 60 < p>75
B: 50<p<60
C: 35<p<50
fail:p<35

Ans:
p=50
if p>75:
    print("Grade:o")
elif 60<p<=75:
    print("Grade:A")
elif 50<p<60:
    print("Grade:B")
elif 53>p<=50:
    print("Grade: C")
else:
    print("Grade:Fail")

Output:
Grade: C

-------------------------------------------------------------------------------------------

2) n divisible by 2 or 3 ,n=7 ,2 divisble, 3 not ,divisible by 2,and 3
divisible by 3, not 2, not divisible by 2, and 3    
Ans:
n=7
if n%2==0 and n%3!=0:
    print("divisible by 2, not 3")
elif n%2==0 and n%3==0:
    print("divisible by 2 and 3")
elif n%3==0 and n%2!=0:
    print("divisible by 3,not 2")
else:
    print("not divisible by 2 and 3")



Output:
not divisible by 2 and 3
-------------------------------------------------------------------------------------------


1)print odd value between 20 and 80, without using if. Using for loop only.
Ans:
for n in range(21,81,2):
    print(n)

Output
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79

-------------------------------------------------------------------------------------------


2) creat a list of 1 to 20 number using for loop [1,2,3..20]
Ans:
numbers=[]
for i in range(1,21):
    numbers.append(i)
print(numbers)

Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

-------------------------------------------------------------------------------------------


3)create a  list of 20 to 1 value using  for loop (dont Use Reverse)
[20,19,18,...3,2,1]
Ans:
num=[]
for i in range(20,0,-1):
    num.append(i)
print(num)

Output
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

-------------------------------------------------------------------------------------------



4)take Cube of odd values between 20 to 40.
Ans:
for i in range(20,40):
    if i%2!=0:
        print(i**3)

Output
9261
12167
15625
19683
24389
29791
35937
42875
50653
59319

-------------------------------------------------------------------------------------------

5)take 5 freinds name in list name=[a,b,c,d,e]
take corresponding ages in second list age = [20,21,23,25,24].
Ans:
name=["a","b","c","d","e"]
age=[20,21,22,23,24]
for i in range(0,len(age)):
    print("My name is",name[i],"my age is",age[i])
Output
My name is a my age is 20
My name is b my age is 21
My name is c my age is 22
My name is d my age is 23
My name is e my age is 24

-------------------------------------------------------------------------------------------

Solve Using if and for loop  and data types methods ;

 
1.Given a list, write a Python code  to swap first and last element of the list.
Ans:
n=[1,2,3,4,5]
l=len(n)
n[0], n[-1]=n[-1], n[0]
print(n)
Output:
[5, 2, 3, 4, 1]

-------------------------------------------------------------------------------------------

2.write code count lenght of string
Ans:
i=sorted("simran patil")
print(len(i))

Output:
12

-------------------------------------------------------------------------------------------


3.Write a Python program to get the sum of a only non-negative integer. ex, [1,4,-5,-20,10] ans is 15
Ans:
a=[1,4,-5,-20,10]
total=0
for i in range(0,len(a)):
    if a[i]>0:
        total=total+a[i]
print(total)

Output:
15

-------------------------------------------------------------------------------------------

4.write code of factorial.

a=int(input("Enter a number:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

Output:
Enter a number:3
6
    










