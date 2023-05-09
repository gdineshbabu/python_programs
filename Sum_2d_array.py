#  ------ SUM THE ELEMENTS IN 2d-ARRAY AT INDEX 0--------

a = np.array(
    [
    [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ],  
    [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ],  
    ]
)
c=0
for i in range(4):
    c+=a[0,0,i]+a[1,0,i]
print("The Sum of elements in 2d array at the index 0 is :",c)
