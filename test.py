import json

print('777 111')
print('777 888 11999')

with open('ihub_parameters.json', "rb") as PFile:
    data = json.loads(PFile.read().decode('utf-8'))

print(data["processId"])
print(data["ovUrl"])
print(data["logLevel"])

f = open("guru99.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()