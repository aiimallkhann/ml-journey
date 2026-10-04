import numpy as np

#1d array
arr1 = np.array([1,2,3,4,5])
# print(arr1)

#2d array
arr2 = np.array([[1,2,3], [4,5,6]])

# print('\n')

#zero array:
zeroArr = np.zeros((2,3))
# print(zeroArr)

#print('\n')

iden = np.identity(5)
# print(iden)

#print('\n')

arr3 = np.arange(10)
# print(arr3)

#print('\n')

arr4 = np.arange(2, 16)
# print(arr4)

#print('\n')

arr5 = np.arange(5,16,2)
# print(arr5)

#print('\n')

arr6 = np.linspace(10,20,5)
# print(arr6)
# print('\n')

arr7 = arr6.copy()
# print(arr7)

# print('\n')

arr8 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(arr8)
# print(arr8.shape)

# print(arr8.ndim)

# print(arr8.size)
# print(arr8.itemsize)
# print(arr8.dtype)
# print(arr8.astype('float'))

#SLICING INDEXING AND ITERATION:

arr12 = np.arange(24).reshape(6,4)
# print(arr12)
# print('\n')

#-------------for printing cols:
# print(arr12[:,3])

#------------for printing more cols:
# print(arr12[:,1:3])

#------------for printing specific numbers:
# print(arr12[2:4,1:3])
# print('\n')
# print(arr12[4:6,2:4])

# for i in arr12:
#     print(i)

#-----------------for looping through all the elemnts in array:
# for i in np.nditer(arr12):
#     print(i)

#-----------------RESHAPING NUMPY TECHNIQUES-----------------------#
testarr = np.arange(6)
testarr2 = np.arange(4,10)

# print(testarr - testarr2)
# print('\n')
# print(testarr * testarr2)
# print('\n')
# print(testarr2 > 3)

testarr3 = np.arange(6).reshape(2,3)
testarr4 = np.arange(6,12).reshape(3,2)

# print(testarr3.dot(testarr4))

# print('\n')

# print(testarr2.max(), '\n')
# print(testarr2.min(), '\n')

#------------AXIS=0 IS FOR ROW------------#

# print(testarr4.min(axis=0), '\n') 
# print(testarr4.max(axis=1), '\n')
# print(testarr4.sum(axis=0), '\n')
# print(testarr4.mean(), '\n')
# print(testarr4.std())
# print(np.median(testarr4))
# print(np.exp(testarr4).astype(int))
# print(testarr4.ravel())

#-------------RESHAPING NUMPY ARRAY-------------#
# print(testarr4.transpose())
testarr5 = np.arange(12,18).reshape(2,3)
# print('\n')
# print(np.hstack((testarr3,testarr5)))
# print('\n')
# print(np.vstack((testarr3,testarr5)))
# print('\n')
# print(np.hsplit(testarr3,3))
# print('\n')

#-------------INDEXING USING BOOLEAN ARRAYS-------------#
arr = np.random.randint(low=1,high=100,size=20).reshape(4,5)
print(arr)
#this is called indexing through boolen array.
print(arr[arr>50])
arr[(arr>50) & (arr%2!=0)]