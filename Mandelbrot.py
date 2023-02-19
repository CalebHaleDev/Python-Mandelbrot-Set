print("Hello World. This is my Mandelbrot set generator")
import math #alternatively, "from math import *" where I think * means everything, a empty placeholder
#import random
import sys

#notes that might be useful for future updates:
#negative index position accesses lists from the end forward (first to last, second to last, third to last, etc.)
#colon can be used for a selection, i.e. print(list[1:4])
#list.extend(source) can be used to a add another list to a list, like append - which adds values
#tuples can't be changed or altered
#dictionary.get(key, default value) allows automatic default values to be returned, unlike dictionary[key] 
#experiment with enumeration keywords and printing lists easier

def roundDown(n):
    return int("{:.0f}".format(n))

def iterate(value, coord):      #this squares a complex number and adds another to it
    return value[0]**2-value[1]**2+coord[0], 2*value[0]+coord[1]

def print_set(set, precision):
    set_height = 4*precision
    point_iterator = 0
    
    for data_point in sorted(set):
        if set[data_point]==0:                      #for each point, find the value
            data = 0
        else:
            data = round(math.log(set[data_point]))
        sys.stdout.write(str(data))                 #and print the value without going to a new line
        point_iterator+=1
        if point_iterator%set_height==0: print()    #make newline after each line

def generate_set(precision, gamemode):
    precision = int(precision)  #determines the nths to calculate. .1 is tenths (precision 10), .001 is thousandths (precision 1000), etc.
    mandelbrot = dict()
    max_Iterations = max(min(15*precision,10000),1000)

    print("generating, please wait...")
    for i in range(-2*precision, 2*precision):
        for j in range(-2*precision, 2*precision):
            coord = i/precision, j/precision #this cycles through all x, y values between 0 and 2
            iterations = 0
            result = iterate(coord, coord)  #can tuples be redefined?
            while(iterations<max_Iterations and result[0]**2+result[1]**2<4):   #generate each point
                result = iterate(result, coord)
                iterations+=1
            mandelbrot[coord] = iterations      #store each point

            #uncomment for high iteration data
            #if(iterations>.75*max_Iterations and iterations<max_Iterations): print(str(iterations)+" iterations from "+str(coord))
            #uncomment for extreme-filtered data
            #if(iterations!=0 and iterations!=max_Iterations): print(str(iterations)+" iterations from "+str(coord))
            #uncomment for raw data
            #print(str(iterations)+" iterations from "+str(coord))
    
    print("\nprecision "+str(precision)+" set generated with size of: "+str(len(mandelbrot))+" out of "+str((precision*4)**2))
    #uncomment to print the whole set
    #print("the set is: " + str(mandelbrot))

    if (gamemode==1):   #unless gamemode is manual, print stats. if it's manual, ask
        if(input("type yes if you'd like to see more data: ")!="yes"): return   #if data not wanted, stop, otherwise continue

    if(4*precision<160):    #print the visual if there's room
        print_set(mandelbrot, precision)

"""         print stats:
    running_total = 0
    for data_point in mandelbrot:
        running_total += mandelbrot[data_point]
    data_average = running_total/len(mandelbrot)
    area_average = data_average/precision**2
    print("totals are: "+str(running_total)+"       the average is: "+str(data_average)+"   and the weighted average is: "+str(area_average))
    """

#main function:
user_input = ""
while(user_input!="0"):
    print()
    print("enter 0 to quit")
    print("enter 1 to generate the mandelbrot set with custom settings")
    print("enter 2 to generate the set with a series of settings")

    user_input = str(input("pick your action: "))
    if (user_input=="1"):
        generate_set(input("enter your level of precision: "), 1)
    if(user_input=="2"):
        for i in range (2,5):
            generate_set(i**3, 2)
        
print("Have a great day!")
