# these are created outside of a function and can be used both inside and outside of a function

my_car = ("volvo")
def myfunc() :
    # print("My best car is a " + my_car)
#myfunc()
    
    #creating a variable inside  a function with the same name as the global variable
    
    my_house =("najjera")
def myfunc() :
        my_house =("bwate")
        print("My house is in " + my_house)
myfunc()
