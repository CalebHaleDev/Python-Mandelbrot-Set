print("Hello World. This is my Mandelbrot set generator")
import math #alternatively, "from math import *" where I think * means everything, a empty placeholder
import sys

#notes that might be useful for future updates:
#negative index position accesses lists from the end forward (first to last, second to last, third to last, etc.)
#colon can be used for a selection, i.e. print(list[1:4])
#list.extend(source) can be used to a add another list to a list, like append - which adds values
#dictionary.get(key, default value) allows automatic default values to be returned, unlike dictionary[key] 
#experiment with enumeration keywords and printing lists easier

def roundDown(n):
    return int("{:.0f}".format(n))

def iterate(value, coord):      #this squares a complex number and adds another to it
    i = value[0]
    r = value[1]
    addi = coord[0]
    addr = coord[1]
    return 2*i*r+addi, r**2-i**2+addr

def print_set(set, precision, sensitivity, coordinate_range):
    set_width = int((coordinate_range[0][1]-coordinate_range[0][0])*precision)
    print("width is: "+str(set_width))
    point_iterator = 0
    #changing the number below changes the logarithmic scale of the graph.
    #Lower numbers for more range (detail), but if you exceed 9 the double-digits will break the image. high sensitivity means low constant.
    ln_to_log_constant = math.log(10/sensitivity)
    display_array = []
    for row in range(int((coordinate_range[1][1]-coordinate_range[1][0])*precision)):
        display_array.append([])

    for data_point in sorted(set):
        if set[data_point]==0:                      #for each point, find the value
            data = 0
        else:
            data = round(math.log(set[data_point])/ln_to_log_constant)
        display_array[-1*(point_iterator%set_width)-1].append(str(data))    #add the data point to the current row
        point_iterator+=1
    
    for row in display_array:       #display each row
        for item in row:
            sys.stdout.write(str(item))
        print()

    return


    #direct print testing copy
    for data_point in sorted(set): 
        if set[data_point]==0: data = 0
        else: data = round(math.log(set[data_point])/ln_to_log_constant)
        sys.stdout.write(str(data_point)+"is"+str(data))   
        point_iterator+=1
        sys.stdout.write("r"+str(point_iterator%set_width))
        if point_iterator%set_width==0:     #make newline after each line
            print() 


def generate_set(precision, gamemode, sensitivity, coordinate_range):
    precision = int(precision)  #determines the nths to calculate. .1 is tenths (precision 10), .001 is thousandths (precision 1000), etc.
    sensitivity = int(sensitivity)  #determines the log scale of digit displays
    mandelbrot = dict()
    max_iterations = max(min(15*precision,10000),1000)

    print("generating, please wait...")
    for i in range(int(coordinate_range[0][0]*precision), int(coordinate_range[0][1]*precision)):
        for j in range(int(coordinate_range[1][0]*precision), int(coordinate_range[1][1]*precision)):
            coord = i/precision, j/precision #this cycles through all x, y values between the graph range
            iterations = 0
            result = iterate(coord, coord)
            while(iterations<max_iterations and result[0]**2+result[1]**2<4):   #generate each point
                result = iterate(result, coord)
                iterations+=1
            mandelbrot[coord] = iterations      #store each point

            #uncomment for high iteration data
            #if(iterations>.75*max_Iterations and iterations<max_Iterations): print(str(iterations)+" iterations from "+str(coord))
            #uncomment for extreme-filtered data
            #if(iterations!=0 and iterations!=max_Iterations): print(str(iterations)+" iterations from "+str(coord))
            #uncomment for raw data
            #print(str(iterations)+" iterations from "+str(coord))
    

    print("\nprecision "+str(precision)+" set generated with size of: "+str(len(mandelbrot))+" out of "+str((int(coordinate_range[0][1]*precision)-int(coordinate_range[0][0]*precision)) * (int(coordinate_range[1][1]*precision-int(coordinate_range[1][0]*precision)))))
    #uncomment to print the whole set
    #print("the set is: " + str(mandelbrot))

    #if (gamemode==1):   #unless gamemode is manual, print stats. if it's manual, ask
    #    if(input("type yes if you'd like to see more data: ")!="yes"): return   #if data not wanted, stop, otherwise continue

    if((coordinate_range[0][1]-coordinate_range[0][0])*precision<=160):    #print the visual if there's room
        print_set(mandelbrot, precision, sensitivity, coordinate_range)
    else:
        print("visual too large to print")

    #print stats:
    running_total = 0
    for data_point in mandelbrot:
        running_total += mandelbrot[data_point]
    data_average = running_total/len(mandelbrot)
    area_average = data_average/precision**2
    print("totals are: "+str(running_total)+"       the average is: "+str(data_average)+"   and the weighted average is: "+str(area_average))
    print()


def print_help():
    print("Welcome!")
    print("What is the Mandelbrot set?")
    print("The Mandelbrot set is a display of the results of repeatedly squaring and adding numbers with complex values.")
    print("(that means it has both imaginary and real parts, like how a mixed number has a whole part and a fraction part)")
    print()
    print("How does the program work?")
    print("you can print the set with different precisions (different height and width of the image, like pixel size)")
    print("and you can adjust the sensitivity (different digits display for the values, so you can see more or less change)")
    print("as well as the starting and stopping points for where you want to look, what parts of the graph. There's nothing past the -2 to 2 range")
    print()
    print("Hope you enjoy!")
    print()


#main function:
user_input = ""
x_range = -2, 2
y_range = -2, 2
while(user_input!="0"):
    print()
    print("enter 0 to quit")
    print("enter 1 to generate the mandelbrot set with custom settings")
    print("enter 2 to generate the set with a series of settings")
    print("enter 3 for help")
    #print("enter 4 to change the ranges of the display")

    #generate_set uses the inputs (precision, gamemode, sensitivity, coordinate_range)
    #precision is the number of digits (resolution), and sensitivity is the range of values (contrast/variety)
    user_input = str(input("pick your action: "))
    if (user_input=="1"):       #custom graph
        precision = input("enter your level of precision: (max displayable is 160 total)")
        sensitivity = input("enter your level of sensitivity: ")
        if input("use default range? (Y/N) ")=="N":         #ask for coordinates
            x_range = float(input("starting X? ")), 2
            x_range = x_range[0], float(input("stopping X? "))
            y_range = float(input("starting Y? ")), 2
            y_range = y_range[0], float(input("stopping Y? "))
        else:
            x_range = -2, 2
            y_range = -2, 2
        coordinate_range = x_range, y_range
        generate_set(precision, 1, sensitivity, coordinate_range)   #need to adjust printing display for different ranges
    if(user_input=="2"):
        x_range = -2, 2
        y_range = -2, 2
        coordinate_range = x_range, y_range
        for i in range(1,6): #1,6
            generate_set(10*i, 2, i, coordinate_range)
    if(user_input=="3"):
        print_help()
   
print("Have a great day!")
