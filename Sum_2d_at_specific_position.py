# ------ SUM THE ARRAY ELEMENTS AT HE SPECIFIC POSITION ------

import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
c=0
for i in range(len(a)):
    c+=a[i,2]
print("The sum of the elements at the index 2 is:",c)
