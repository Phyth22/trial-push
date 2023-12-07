#dicctionaries ..storing and accessing values in a dictionary

student = {'name':'Agatha', 'age': 25,'courses':['math','compscie']}
#print(student) #Accessing our dictionary

#print(student['age']) #accessing only one value

#print(student['courses'])
#print(student.get('name')) # another method of accesing a value in a dictionary

#updating our dictionary
student.update({'name':'faith','age':'30','phone': 755086820})
#print(student)

# deleting a value in a dictionary
del student['phone']
#print(student)
#age = student.pop('age')
#print(student)

# finding the lenghr of the dic
#print(len(student))

#to print out only the keys
#print(student.keys()) here we are only printing out the keys in the dic

#print(student.values()) here weare printing out the values in a dic

#print(student.items()) # and here we are printing out the keys and valuesin our dic

# for looping
for key in student:
   # print(key)
    
    for key,value in student.items():
        print(key,value)