import csv


if __name__=='__main__':
    with open('data/sample.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(', '.join(row))