# list.sort()는 inplace로 None을 return하고
# sorted(list)는 sorted 새로운 list를 return합니다

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)

print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))

print(fruits)
fruits.sort()
print(fruits)


