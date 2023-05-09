# convert 1d array into 2d array using of reshape and find the sum of the elements in the array 
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(4,3)
print("The reshaped array :\n",b)
c=b.reshape(2,6)
print("\nThe reshaped 2d array from 1d array is :\n",c)
d=0
for i in range(len(c[0])):
    d+=c[0,i]+c[1,i];
print("\nThe sum of the elements in the array is :",d)
