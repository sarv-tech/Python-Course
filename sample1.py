# File Operations 

#open, read & close

# f = open("data.txt", "r")
# data.txt => file name => file path
# r => mode
# r - read mode
# w - write mode


f = open("sample.txt", "r")  # file object

data = f.read()
print(type(data))
print(data)


data = f.readline()
print(data)

data = f.readline()
print(data)
f.close()

f = open("sample.txt", "w") 
f.write("123")
f.close()