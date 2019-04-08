import os

fd = "myname.txt"
fd2 = "printname.txt"
file = open(fd, 'w')
file.write("hello")
file.close()
file = open(fd, 'r')
text = file.read()

file = open(fd2, 'w')
file.write(text)
file.close()
file = open(fd, 'r')
text2 = file.read()
print(text2)


