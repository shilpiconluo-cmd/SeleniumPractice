with open(r"C:\Selenium\GitHub account.txt", "r") as file:
    lines = file.readlines()  # returns a list of all lines
    for line in lines:
        print(line.strip())  # strip removes \n at end

with open(r"C:\Selenium\GitHub account.txt", "w") as file1:
    file1.writelines("hi m here")