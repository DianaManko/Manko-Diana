import csv
ok = 'latvian','Lithuania','Estonia'
with open('power.csv') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter=','))[1:]
    spamreaderok = list(filter(lambda a: a[0] == ok, spamreader))
    c = sum(map(lambda x: int(x[2]), spamreaderok))
    print(int(c))
