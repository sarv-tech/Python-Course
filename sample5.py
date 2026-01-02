f = open("sample5.txt", "a+")  # file object

f.write("123")
print(f.read())

f.close()