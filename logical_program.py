# 1.count odd even num
num=[1, 2, 3, 4, 5, 6, 7, 8,9]
odd=[]
even=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('this is even number count', len(even))
print('this is odd number count', len(odd))

# 2.range
for x in range(6):
   if x%3!=0:
      print(x)

# 3.divisible by 7 and multible by 5 range 1500 between 2700
for i in range(1500, 2700):
    if i%7==0 and i%5==0:
        print(i)

# 4.divisible by 7 and multible by 5 range 500 between 1000
for item in range(500, 1000):
    if item%7==0 and item%5==0:
        print(item)

# 5.odd index value remove
value='saran'
print(value[::2])

# 6.check the number positive or not
positiveNumbers=[1, -2, 3, -4, 5, -6, 7]
for e in positiveNumbers:
    if 0<=e:
        print('this is positive numbers', e)
    else:
        print('this is not positive numbers', e)

# 7.get 5 subject marks in user and find average
tamil=int(input('enter tamil mark'))
english=int(input('enter english mark'))
maths=int(input('enter maths mark'))
science=int(input('enter science mark'))
social=int(input('enter social mark'))
total=tamil+english+maths+science+social
average=total/5
print(average)

# 8.prime or not
primeNum=int(input('enter a number'))
for a in range(2, primeNum):
    if primeNum%a==0:
        print(primeNum,'is not prime number')
        break
    else:
        print(primeNum, 'is prime number')
        break

# 9.palindrome or not
num1=input('enter number for palindrome')
if num1==num1[::-1]:
    print(num1,'is palindrome number')
else:
    print(num1,'is not a palindrome number')

# 10.factorial
factorial=int(input('enter a number'))
fact=1
for f in range(factorial+1):
    if f!=0:
        fact*=f
print(fact)

# 11.find the name in the list
nameList=input('enter a name')
nameList1=['saran', 'selvi', 'raja']
if nameList in nameList1:
    print(nameList,'is in the list')
else:
    print(nameList,'is not in the list')

# 12.delete vowle in given string
string1=input('enter a string')
emptStr=[]
vowels="AEIOUaeiou"
for i in range(len(string1)):
    if string1[i] not in vowels:
       emptStr+=string1[i]
print(emptStr)

# 13.multiple integers into a single integer
mulNum=[1, 2, 3, 4]
singNum=[]
for i in mulNum:
    singNum+=str(i)
print('single value',int (singNum))

#15.check dictionary empty or not
dictList={}
if len(dictList)==0:
    print('this dictionary is empty')
else:
    print('this dictionary is not empty')










