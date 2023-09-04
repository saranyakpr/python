# how to print dictionaries
myDict={'name':'saran', 'age':22}
print(myDict)

# how to find length
print(len(myDict))

# how to get key in dict(direct, get)
print(myDict["age"])

# using get method
print(myDict.get('age'))

# how to get all values
print(myDict.values())

# how to get all keys
print(myDict.keys())

# how to get key and values
print(myDict.items())

# how to check key in there
if "name" in myDict:
    print('yes name in this dict')
else:
    print("no name not found")

# how to change values
myDict['age']=18
print(myDict)

# how to add another key and values(nrml, update)
myDict['gender']='female'
print(myDict)

# update
myDict.update({'rollnum':21})
print(myDict)

# how to delete items in dict
myDict.pop("name")
print(myDict)

# delete
del myDict['age']
print(myDict)

# iterate (how to get value)
iterateDict={'name':'saran', 'age':21}
for item in iterateDict:
    print(iterateDict[item])

# how to get key
iterateDict1={'name':'saran', 'age':21}
for name in iterateDict1:
    print(name)

# how to get key and values
iterateDict2={'name':'saran', 'age':21}
for i,j in iterateDict2.items():
    print(i,j)

# copy
copyDict={'name':'saran', 'age':21}
copyDict1=copyDict.copy()
print(copyDict1)

# nested dict
fruits={
    'mango':{
        'color':'yellow',
        'price':150
    },
    'apple':{
        'color':'red',
        'price':200
    }
}
print(fruits)

# fromkeys
x=('name1', 'name2', 'name3')
y='saran'
keyDict=dict.fromkeys(x,y)
print(keyDict)

# setdefault
orange={
    'color':'orange',
    'price':150
}
setDict=orange.setdefault('price', 150)
print(setDict)


























