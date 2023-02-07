print("Hello World. This is my Mandelbrot set generator")
import math
import random
import sys

def roundDown(n):
    return int("{:.0f}".format(n))

def iterate(value, coord):      #this squares a complex number and adds another to it
    return value[0]**2-value[1]**2+coord[0], 2*value[0]+coord[1]

def print_set(set, precision):
    rows = list()
    set_height = 4*precision    #int(math.sqrt(len(set)))
    for row in range(set_height): rows.append("")
    point_iterator = 0
    for data_point in sorted(set):
        if set[data_point]==0:
            data = 0
        else:
            data = round(math.log(set[data_point]))
        sys.stdout.write(str(data))
        point_iterator+=1
        if point_iterator%set_height==0: print()
        """
        rows[set_height-1-point_iterator%set_height] = str(rows[set_height-1-point_iterator%set_height])+str(data,10)
        point_iterator+=1
        """


"""
    set_width = math.sqrt(set)
    set_height = set_width
    for row in range(set_height):
        line = []
        for point in range(set_width):
            print()
"""

def generate_set(precision, gamemode):
    precision = int(precision)
    mandelbrot = dict()
    #determines the nths to calculate. .1 is tenths (precision 10), .001 is thousandths (precision 1000), etc.
    max_Iterations = max(min(15*precision,10000),1000)

    print("generating, please wait...")
    for i in range(0,4*precision):
        for j in range(0,4*precision):
            coord = (i-2*precision)/precision, (j-2*precision)/precision #this cycles through all x, y values between 0 and 2
            iterations = 0
            result = iterate(coord, coord)
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

    
    #print(enumerate([*mandelbrot]))    experimentation

    if(4*precision<160): print_set(mandelbrot, precision)
"""
    running_total = 0
    for data_point in mandelbrot:
        running_total += mandelbrot[data_point]
    data_average = running_total/len(mandelbrot)
    area_average = data_average/precision**2
    print("totals are: "+str(running_total)+"       the average is: "+str(data_average)+"   and the weighted average is: "+str(area_average))
    """


#this was used to test the sorted dictionary in a loop
"""
def addTestpoint(coordinate, value):
    test[coordinate] = value

test = dict()

for i in range(10):
    data = random.sample(range(1,10),3)
    coordinate = (data[0]-5)/10,(data[1]-5)/10
    addTestpoint(coordinate, data[2])

print("test is "+str(test))

for i in sorted(test):
    print(i)
"""
#tested logarithms
"""
for num in range (1,10):
    print("log of "+str(10*num)+" is "+str(math.log(10*num,10)))
    """

print(len("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))

user_input = ""
while(user_input!="0"):
    print()
    print("enter 0 to quit")
    print("enter 1 to generate the mandelbrot set with custom settings")
    print("enter 2 to generate the set with a series of settings")

    user_input = str(input("pick your action: "))
    if (user_input=="1"): generate_set(input("enter your level of precision: "), 1)
    if(user_input=="2"):
        for i in range (2,5): generate_set(i**3, 2)
        

print("Have a great day!")
