import sys

if __name__=='__main__':
    print(len(sys.argv))
    assert len(sys.argv) == 3, "usage: python args.py arg1 arg2"

    print ("sys.argv[0]:", sys.argv[0])
    print ("sys.argv[1]:", sys.argv[1])
    print ("sys.argv[2]:", sys.argv[2])

    """
    $ python args.py aaa "bbb"
    3
    sys.argv[0]: args.py
    sys.argv[1]: aaa
    sys.argv[2]: bbb
    """