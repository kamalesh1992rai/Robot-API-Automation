# Reading data from the file
obj = open("D:\PY232.txt",'r')
print(obj.tell())

obj.seek(5)
print(obj.tell())