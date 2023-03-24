import csv


if __name__=='__main__':
    with open('data/sample.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(', '.join(row))
            # 1, 2, 3
            # 4, 5, 6
            # 7, 8, 9