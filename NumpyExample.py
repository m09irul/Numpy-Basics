import numpy as np

arr1D = np.array([1,2,3,4,5])
arr2D = np.array([[1,2],[3,4],[5,6]])
arr3D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr5D = np.array([1,2,3,4], ndmin = 5)

print(np.__version__)

print("Data Type of the 1D array: ",type(arr1D))
print("Type of the 1D array: ",arr1D.dtype)
print("Data Type of the 2D array: ",type(arr2D))
print("Type of the 2D array: ",arr2D.dtype)
print("Type of the 3D array: ",type(arr3D))
print("Data Type of the 3D array: ",arr3D.dtype)

print("\n____NOTE: index starts from 0____ \n\n")
print("1D array info: \n")
print(arr1D)
print("3th element  of the array is: ", arr1D[3])
print("Sliced from index 1 to till 5: ", arr1D[1:5])
print("Sliced from index 2 to rest: ", arr1D[2:])
print("Sliced from index start to till 3: ", arr1D[:3])
print("Sliced from the index 2 from the end to index 1 from the end: ", arr1D[-3:-1])
print("Return every other element from index 0 to index 4 with step 2: ", arr1D[0:5:2])
print("array elements:")
for x in arr1D:
  print(x)
print("dimension: ",arr1D.ndim)
print("\n")

print("2D array info: \n")
print(arr2D)
print("1st element of 2nd dimension of the array is: ", arr2D[1,0])
print("From the second element, slice elements from index 0 to index 0:", arr2D[1, 0:1])
print("From 1st and 2nd elements, return index 1:", arr2D[0:2, 1])
print("From 1st and 2nd elements, slice index 0 to index 1, this will return a 2-D array:", arr2D[0:2, 0:2])
print("array elements:")
for x in arr2D:
  print(x)
print("dimension: ",arr2D.ndim)
print("\n")

print("3D array info: \n")
print(arr3D)
print("1st element of 2nd dimension of 1st dimension of the array is: ", arr3D[0,1,0])
print("array elements:")
for x in arr3D:
  print(x)
print("dimension: ",arr3D.ndim)
print("\n")

print("5D array info: \n")
print(arr5D)
print("3th element of 1st dimension of 1st dimension of 1st dimension of 1st dimension of the array is: ", arr5D[0,0,0,0,3])
print("array elements:")
for x in arr5D:
  print(x)
print("\ndimension: ",arr5D.ndim)
print("\n")

print("__________Google ase ki korte__________ :3")
