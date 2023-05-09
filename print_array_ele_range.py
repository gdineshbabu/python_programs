# to print the array elements in the range

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("The  elements from 1-4  :",a[:4])  # print the first 4 elements
print("The  elements from 1-10 :",a[:10]) # to print from 1-10 in the array
print("The elements from 4-10  :",a[3:10]) # print the elements from 4-10
print("The next by next elements:",a[::2])  # to print the next by next elements
print("The elements from 4-10 using negative value  :",a[-9:10]) # print the elements from 4-10 using an a negative value
