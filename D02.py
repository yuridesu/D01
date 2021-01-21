import numpy as np
array1 = np.array(range(30))
array=array1.reshape(5,6)
array.sort()
np.where(array%6==1)
