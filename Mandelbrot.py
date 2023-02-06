print("Hello World. This is my Mandelbrot set generator")
#import math

def roundDown(n):
    return int("{:.0f}".format(n))

def iterate(value, coord):
    return value[0]**2-value[1]**2+coord[0], 2*value[0]+coord[1]

def generate_Set(precision):
    precision = int(precision)
    mandelbrot = dict()
    #determines the nths to calculate. .1 is tenths (precision 10), .001 is thousandths (precision 1000), etc.
    max_Iterations = 10*precision

    print("generating, please wait...")
    for i in range(0,2*precision):
        #for j in range(0,2*precision):     #I'm about to change the coordinate system so it isn't as resource-intense
        coord = i%(2*precision)/(precision), roundDown(i/(2*precision))/(precision) #this cycles through all x, y values between 0 and 2
        iterations = 0
        result = iterate(coord, coord)
        while(iterations<max_Iterations and result[0]**2+result[1]**2<4):   #generate each point
            result = iterate(result, coord)
            iterations+=1
        mandelbrot[coord] = iterations      #store each point
        #uncomment for filtered data
        #if(iterations!=0 and iterations!=max_Iterations): print(str(iterations)+" iterations from "+str(coord))
        #uncomment for raw data
        #print(str(iterations)+" iterations from "+str(coord))
        
    print("set generated with size of: "+str(len(mandelbrot))+" out of about "+str((precision*2)**2-(precision-1)))
    #uncomment to print the whole set
    #print("the set is: " + str(mandelbrot))

user_input = ""
while(user_input!="0"):
    print()
    print("type 0 to quit")
    print("type 1 to generate the mandelbrot set")
    user_input = str(input("pick your action: "))
    if (user_input=="1"):
        generate_Set(input("enter your level of precision: "))

print("Have a great day!")
