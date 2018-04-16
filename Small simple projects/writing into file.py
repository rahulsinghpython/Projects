###############################################
# writing into files

cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

#################################################
# strip function

print("adelaide".strip('a'))

###################################################
# appending files in python

with open("cities.txt", "a") as city_file:

    x = 1

    for x in range(1, 13):
        print("{} times 2 is {}".format(x, x*2), file= city_file)
        x += 1

