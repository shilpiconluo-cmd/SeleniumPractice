file = open("../../test.txt")
print(file.read())  # print all content
file.close()
file = open("../../test.txt")
print(file.readline()) # print first line
file.close()
file = open("../../test.txt")
print(file.read(6)) # print first 6 charcaters
file.close()

file = open("../../test.txt")
line = file.readline()
while line!="":
    print(line)
    line = file.readline()

file.close()


