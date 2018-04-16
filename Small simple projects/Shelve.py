# shelves example
import shelve

# with shelve.open("bikes", writeback= True) as bike:
# ^^^^ this forces the shelve to update when you close it instead of using cache so you can append directly.
# the appending method below is much better than the writeback method cause it uses alot of memory especially in big files
# shelves must be run as a string
with shelve.open("bikes") as bike:
    bike["make"] = "yamaha"
    bike["model"] = "r15"
    bike["color"] = "black"
    bike["size"] = 150
    bike["looks"] = ["sexy", "sleek"]
# --------------------------------
# appending something that is already in the database
    templist = bike["looks"]
    templist.append("sporty")
    bike["looks"] = templist
# --------------------------------


    # print(bike["size"])
    # print(bike["make"])


    for x in range(1,100):
        dict_key = input("please enter the make/model/color/size/looks:")
        if dict_key in bike:
            description = bike[dict_key]
            print(description)
        else:
            print("we dont have that category")
        if dict_key == "quit":
            break

            
