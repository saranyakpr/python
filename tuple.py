# how to print tuple
myTuple=('red', 'yellow', 'green')
print(myTuple)

# how to print single value in tuple
myTuple1=('black',)
print(type(myTuple1))

# how to add or remove items in tuple
# add
addTuple=('red', 'green', 'blue')
changeList=list(addTuple)
changeList.append('black')
changeTuple=tuple(changeList)
print(changeTuple)

# remove
removeTuple=('apple', 'banana', 'mango', 'orange')
changeList1=list(removeTuple)
changeList1.remove('mango')
changeTuple1=tuple(changeList1)
print(changeList1)

# assign value
tuple1=(1, 2, 3, 4, 5)
(no1, no2, no3, no4, no5)=tuple1
print(no3)

# typle constructor
newTuple=tuple(('red', 'green', 'blue'))
print(newTuple)

# index
tupleIndex=(1, 2, 3, 4, 5, 6)
tupleIndex1=tupleIndex.index(4)
print(tupleIndex1)

#task

# 1.clone or copy a list
copyList=['python', 'java', 'react']
copyList1=copyList.copy()
print(copyList1)

# 2.addition, subtraction, multiplication, division
# addition
a=int(input('Enter a number for addition'))
b=int(input('Enter a number for addition'))
print('addition two numbers:', a+b)

# subtraction
c=int(input('Enter a number for subtraction'))
d=int(input('Enter a number for subtraction'))
print('subtraction two numbers:', c-d)

# multiplication
e=int(input('Enter a number for multiplication'))
f=int(input('Enter a number for multiplication'))
print('multiplication two numbers:', e*f)

# division
g=int(input('Enter a number for division'))
h=int(input('Enter a number for division'))
print('division two numbers:', g/h)

# 3.list add and delete
createList=['saranya', 'ramaraja', 'selvi', 'sakthi', 'satheesh']
createList.append('saran')
createList.append('raja')
createList.pop(0)
createList.pop(0)
print(createList)

# 4.creat empty list
emptyList=[]
emptyList.append('html')
emptyList.append('css')
emptyList.append('js')
del emptyList[2]
print(emptyList)

# 5.not useing append
list1=['red', 'blue', 'green', 'yellow', 'black']
list2=['mango', 'apple', 'orange', 'banana']
list3=list1.extend(list2)
print(list1[3:8])

# 6.find the length of element list
length=['red', 'blue', 'green', 'yellow', 'black']
print(len(length))

# 7.create a list with list() constructor
print(list(('red', 'blue', 'green', 'yellow')))

# 8.ascending, decending
print(sorted(input('Enter the numbers')))
value=input('Enter a numbers')
print(sorted(value,reverse=True))

# 9.create tuble and add, fing length
myTuple=('html', 'css', 'js', 'react')
listChange=list(myTuple)
listChange.append('python')
print(tuple(listChange))
print(len(listChange))

# 10.delete the content in tuple
newTuple=('red', 'green', 'yellow', 'black')
chanList=list(newTuple)
chanList.pop(3)3
print(tuple(chanList))