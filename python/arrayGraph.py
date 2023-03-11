import sys
import numpy as np

array = [["a",[1,2]],
         ["b",[3,4]],         
         ["c",[5,6]]]

if __name__=='__main__':
    a = np.arange(16).reshape(4,4)

    print(a)
    print(array[0][1])
    # mainFunc()
