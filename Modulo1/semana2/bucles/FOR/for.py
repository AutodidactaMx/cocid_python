# Iterar sobre una lista
print("List")
l = ["datos", "for", "datos"]
for i in l:
    print(i)
 
# Iterar sobre una tupla
print("\nTuple ")
t = ("datos", "for", "datos")
for i in t:
    print(i)
 
# Iterar sobre un string
print("\nString ")
s = "datos"
for i in s:
    print(i)
 
# Iterar sobre un diccionario
print("\nDictionary ")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))