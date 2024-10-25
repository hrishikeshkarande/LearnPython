my_file = open("friends.txt","a") #name of the file and mode 

print(my_file.readable())

#print(my_file.readline())
#print(my_file.readline())

#print(my_file.readlines())

#for friend in my_file.readlines():
#    print(friend)

my_file.write("\nKabir - 0")



my_file.close()