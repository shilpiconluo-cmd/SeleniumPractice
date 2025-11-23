with open("test.txt","r") as reader:
    content =reader.readlines()  # store all content in list
    reversed(content)  #reverse all content
    with open("test.txt","w") as writer:
        for line in reversed(content):
            writer.write(line)


