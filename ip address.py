

userinput = input("Please enter an ip address")
print("you've entered {}".format(userinput))

length = 0
segment = 1

for i in userinput:
    if i == ".":
        print("segment {} has {} characters".format(segment, length))
        segment += 1
        length = 0

    else:
        length += 1

if i != ".":
    print("segment {} has {} characters".format(segment, length))