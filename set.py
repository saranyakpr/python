# how to print set
mySet={'red', "green", 'yellow'}
print(mySet)

# how to print length
print(len(mySet))

# set can't accept duplicat
newSet={1, 2, 3, 4, 3 ,6}
print(newSet)

# con't count duplicate length
print(len(newSet))

# how to iterate
createSet={'red', 'green', 'blue', 'yellow'}
for item in createSet:
    print(item)

# iterate string
setString=('saran')
for item in setString:
    print(item)

# how to add item (add)
setItem={'saran', 'selvi'}
setItem.add('ramaraja')
print(setItem) 

# how to add two array (update, union)
setItem1={1 ,2 ,3 , 4}
setItem2={5, 6, 7, 8}
setItem1.update(setItem2)
print(setItem1)

# union
unionSet1={1, 2, 3}
unionSet2={4, 5, 6}
unionSet=unionSet1.union(unionSet2)
print(unionSet)

# how to remove in set (remove, discard, clear)
# remove
removeSet={1, 2, 3, 4, 5}
removeSet.remove(3)
print(removeSet)

# discard
discardSet={1, 2, 3, 4, 5}
discardSet.discard(2)
print(discardSet)

# clear
clearSet={1, 2, 3, 4, 5}
clearSet.clear()
print(clearSet)

# copy
copySet={1, 2, 3, 4, 5}
copySet1=copySet.copy()
print(copySet1)

# task
# 1.create set 
newSet={'html', 'css', 'js'}
print(newSet)

# 2.iterate over sets
for i in newSet:
    print(i)

# 3.remove items from set
delSet={'html', 'css', 'js'}
deleSet=delSet.remove('css')
print(type(delSet))

# 4.add items in set
setAdd={'saran', 'selvi'}
setAdd.add('ramaraja')
print(setAdd)

# 5.create union of sets
setUnion1={1, 2, 3}
setUnion2={4, 5, 6}
setUnion3=setUnion1.union(setUnion2)
print(setUnion3)

# 6.remove all elements from set
setRemove={'saran', 'selvi', 'ramaraja', 'sakthi', 'satheesh'}
setRemove.clear()
print(setRemove)

# 7.find the length of set
setRemove1={'saran', 'selvi', 'ramaraja', 'sakthi', 'satheesh'}
print(len(setRemove1))

# 9.convert a tuple to a list
creatTup=('red', 'orange', 'blue')
creatTup1=str(creatTup)
print(creatTup1)

# 10.vaue of rectangle, cylinder
# rectangle= A=wl
l=3
w=5
area=w*l
print(area)

# cylinder vol=22/7*r*h*2
r=5
h=6
vol=22/7*r*h*2
print(vol)



























































