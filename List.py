# how to print list
myList=['python', 'java', 'html', 'css']
print(myList)

# how to length get 
print(len(myList))

# how to get type
print(type(myList))

# list constructor
newList=list(('saran', 'selvi', 'ramaraja', 'sakthi', 'satheesh'))
print(newList)

# range
print(myList[1:4])
print(myList[1:4:2])

# if else
if 'react' in myList:
    print('yes there is in that')
else:
    print('no there')

# change list items
myList[3:4]=('c++', 'react')
print(myList)

# how to add items(append, insert, extend)
# append
addList=['mango', 'apple', 'banana', 'watermelon']
addList.append('kiwi')
addList.append('orange')
print(addList)

# insert
addList.insert(1,'orange')
print(addList)

# extend
addList1=['red', 'black', 'blue', 'yellow']
addList.extend(addList1)
print(addList)

# how to remove items(remove, pop, del, clear)
removeList=['red', 'blue', 'black', 'yellow', 'white']
# remove
removeList.remove('black')
print(removeList)
# pop
removeList.pop(3)
print(removeList)
# clear
clearList=removeList.clear()
print(removeList)

# loop in list
loopList=['red', 'orange', 'yellow', 'blue', 'green']
for x in loopList:
    print(x)

# list comprehension
loopList1=['red', 'orange', 'yellow', 'blue', 'green']
loopList2=[]
for i in loopList1:
    if 'r' in i:
        loopList2.append(i)
print(loopList2)

# sort
sortList=[5, 3, 7, 4, 1, 9]
sortList.sort()
print(sortList)

# sort descending order
sortList.sort(reverse=True)
print(sortList)

# how to copy list
copyList=[1, 2, 3, 4, 5]
copyList1=copyList.copy()
print(copyList1)

# another way of copy
copyList2=list(copyList)
print(copyList2)

# join
joinList1=[1, 2, 3, 4, 5]
joinList2=[5, 4, 3, 2, 1]
print(joinList1+joinList2)

# count
countList=[1, 2, 3, 4, 3, 2, 3]
countList1=countList.count(3)
print(countList1)


#task

# 1. area of circle
area=int(input('Enter r value'))
circle=3.14*area*area
print('area of circle value is :',circle)

# 2. reverse order
firstName=input('Enter first name')
lastName=input('Enter last name')
print(firstName[::-1],end=' ')
print(lastName[::-1],end='  ')

# 3. reverse an integer
num=(input('Enter number'))
print(num[::-1], end=' ')

# 4.swap two number
a=1
b=2
temp=a
a=b
b=temp
print(a,b)

# 5.square value
square=int(input('Enter a number'))
print(square*square)

# 6.cube value
cube=int(input('Enter a number'))
print(cube*cube*cube)

# 7.square root value
root=int(input('Enter a number'))
print(root**.5)

# 8.lowercase to uppercase
name='saran'
print(name.upper())

# 9.join method
str3='white'
str4='wash'
str5=(str3,str4)
print('-'.join(str5))

# 10.without join method
str1='white'
str2='moon'
print(str1 + str2)

# 11.ascending
ascendingValue=['apple', 'mango', 'banana', 'orange']
ascendingValue.sort()
print(ascendingValue)

# 12.descending
descendingValue=['apple', 'mango', 'banana', 'orange']
descendingValue.sort(reverse=True)
print(descendingValue)
















