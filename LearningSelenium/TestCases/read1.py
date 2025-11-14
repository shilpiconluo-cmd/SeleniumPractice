file = open("../../test.txt")
for line in file.readlines():  # print all content using readlines n for loop
    print(line)
    if "India" in line:
        break

file.close()


file = open("../../test.txt")
count =0
for line in file.readlines():  # print all content using readlines n for loop
    print(line)
    count= count+1
    if count==2:
        break

file.close()