# arr=[12,23,2,21,2,21]
# key =2
# print(key in arr)
# print(key not in arr)


arr2=[12,2,32,3221,1]
arr3=[12,2,32,3221,1]
print(arr2[0] is arr3[0])
a=0
print("posi" if a>0 else"neg" "neg"if a<0 else "zero")

arr1=[10,20,30,40]
arr2=[10,20,30,40]
arr3=arr1
print(id(arr3))
print(id(arr1))
arr1[0]=233
print(arr3)
print(arr1[0])
print(arr3[0])


