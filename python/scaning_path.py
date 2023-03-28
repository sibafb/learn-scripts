import os

filepath = './dir/subdir/filename.txt'

print(os.path.splitext(os.path.basename(filepath))[0])
# filename

dirpath = './scanSample/'

dir_list = os.listdir(path= './scanSample/')
print(dir_list)
# ['dirA', 'dirB']

for directory in dir_list:
    file_list = os.listdir(dirpath + directory)
    print(file_list)
    for sample_file in file_list:
        print(sample_file)
# ['samplea.csv', 'sampleb.csv']
# samplea.csv
# sampleb.csv
# ['samplec.csv']
# samplec.csv