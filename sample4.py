f = open("sample4.txt", "r+")  # file object

f.write("123")
print(f.read())

f.close()