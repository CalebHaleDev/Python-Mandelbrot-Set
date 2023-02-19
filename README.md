# Python-Mandelbrot-Set Overview

Purpose: Create and analyze the Mandelbrot set! This project is meant for me to practice learning Python and using it to analyze data. Hopefully I can get something ready to display the results in a graph for easier viewing of the results. Even with just printing digits, you can see what it is generating. I designed it to print at varied levels of detail and noticed what it printed wasn't the Mandelbrot set (a fractal-like shape creating my graphing the results of repeatedly squaring complex numbers and adding a constant to it each iteration). I didn't find a free data set for the Mandelbrot set, so I decided to generate my own copies with the desired precision. I wrote this software mainly to learn and practice python by analyzing the Mandelbrot set, but it was fun trying to figure out where I went wrong in generating the set. I have previously made my own Mandelbrot generator, so I decided to compare the code for each. That revealed my mistake was in the complex number multiplication, which after fixing gave the right data.

Demo video:
[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

What's the average number of iterations per point? According to increasing precision, the answer seemed to converge to a value between 96.6 and 97.7...
10 - 102.239375
20 - 97.345
30 - 97.74145833333333
40 - 96.6703515625
50 - 96.5031
60 - 96.61713541666667
70 - 102.0007780612245
...but as I continued the value diverged again. Still unknown.

What's the area of the inner shape?
Google says it's about 1.506484 but I never got the answer from my project. I experimented with different triggers/qualifications for what to mark, but the program wouldn't recognize more than one data point for any of the criteria I tried.

# Development Environment

I used Visual Studio Code to write the program, importing math (for the logarithm digit printing) and sys (for the same-line printing of each digit).

# Useful Websites

Helpful websites:
* [Python Documentation](https://docs.python.org/3.11/tutorial/index.html)
* [rounding down in python](https://favtutor.com/blogs/round-down-python#:~:text=The%20truncate%20method%2C%20also%20known,"Round%20Down%20in%20Python")
* [taking the square root in python](https://www.w3schools.com/python/ref_math_sqrt.asp#:~:text=The%20math.,square%20root%20of%20a%20number) (I redesigned the program so I didn't need this, and it was simpler on the computer)
* [Python comments](https://www.w3schools.com/python/python_comments.asp)
* [squaring in python](https://flexiple.com/python/python-square/)
* [Python beginners course](https://www.youtube.com/watch?v=rfscVS0vtbw)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Learn why the image is rotated (image values, no longer a display issue)
* Learn why 0s are recognized and countable (get counters working for data analysis)
* Get the custom range system working
* Troubleshoot bug where blank spaces are displayed

