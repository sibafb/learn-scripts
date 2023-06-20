import os

if __name__ == '__main__':
    filepath = './dir/subdir/filename.ext'
    print(os.path.basename(filepath))

    print(os.path.splitext(os.path.basename(filepath))[0])

    