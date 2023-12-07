# used to store multipy items in one variable
animals = ["cows", "goose", "goats", "pigs,", "sheep"]
#print(animals)
#to get the length or know how many values ar in a list
#print(len(animals))
#print( animals[-1]) # prints the last item on the list

#animals.insert(2,"rabbits") # gives position of an item in a list
#print(animals)
     # adding animals 2 to our original animals list
animals2 =[ "birds", "fish"]
animals.extend(animals2)
print(animals)

#print(animals[4]) #indexing

animals[3] = "rabbit" #replacing an item in my list
#print(animals)

animals.remove("sheep") #removing an item
#print (animals)

#adding an item
animals.append("fox")
#
# 
# print(animals)

animals.pop() # removes the last item
#print(animals)

animals.sort()
#print(animals)

#print(type(animals)) # to know the data type of your list

#creating a list

food=["pumpkin" "rice" "posho" "piza"]
#print(food)

#print (food[0])
food[0]="chicken"

