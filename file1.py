import os

fd = "xyz.txt"
file = open(fd, 'a')
file.write("new string \n")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
