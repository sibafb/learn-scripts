import numpy as np

filepath = 'data/sample_numpy.csv'
if __name__ == '__main__':
    a = np.loadtxt(filepath,delimiter=',')
    print(a)
    
    rows, columns = a.shape

    print("Rows = ",rows)
    print("Columns = ", columns)

    print(np.vsplit(a, [2]))
    print(np.hsplit(a,[1]))