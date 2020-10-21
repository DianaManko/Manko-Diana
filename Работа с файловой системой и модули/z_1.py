file = open("purchase_log.txt")
onstring = file.read().split("\n")[:-1]
dict = dict()

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
file.close()
print (dict)
