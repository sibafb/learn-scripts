import numpy as np

filepath = 'data/sample_numpy.csv'
if __name__ == '__main__':
    a = np.loadtxt(filepath,delimiter=',')
    print(a)
    # [[1. 2. 3.]
    #  [4. 5. 6.]
    #  [7. 8. 9.]]

    rows, columns = a.shape
    print("Rows = ",rows)
    print("Columns = ", columns)
    # Rows =  3
    # Columns =  3

    print("np.vsplit(a, [2])\n" + str(np.vsplit(a, [2])))
    print("np.hsplit(a,[1])\n" + str(np.hsplit(a,[1])))
    # [array([[1., 2., 3.],
    #    [4., 5., 6.]]), array([[7., 8., 9.]])]
    # [array([[1.],
    #    [4.],
    #    [7.]]), array([[2., 3.],
    #    [5., 6.],
    #    [8., 9.]])]

    hnparray = np.array([])
    for num in range(5):
        hnparray = np.append(hnparray, [num, num ,num])

    print("hnparray\n" + str(hnparray))
    # hnparray
    # [0. 0. 0. 1. 1. 1. 2. 2. 2. 3. 3. 3. 4. 4. 4.]

    vnparray = np.empty((0,3),float)
    for num in range(5):
        vnparray = np.append(vnparray, [[num, num ,num]],axis=0)

    print("nparray\n" + str(vnparray))
    # nparray
    # [[0. 0. 0.]
    #  [1. 1. 1.]
    #  [2. 2. 2.]
    #  [3. 3. 3.]
    #  [4. 4. 4.]]



    
