
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: Yousif Aqrawe
#    Student name: nxxxxxxx
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = False):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#






#Building style 'A'
def building_a(num_levels, under_construction):
    setheading(0)
    pd()
    width(2)
    pencolor('black')
    fillcolor('maroon')
    begin_fill()
    pd()
    fd(200)
    left(90)
    fd(25)
    right(10)
    fd(15)
    left(100)
    fd(210)
    left(110)
    fd(15)
    right(20)
    fd(25)
    left(90)
    end_fill()
    pencolor("black")
    width(3)
    right(90)

    #Draw the doors and number of them
    for building_A in range(6): # there are 6 doors in this building
        fillcolor('khaki') 
        begin_fill()
        pd()
        right(180)
        fd(15)
        circle(-16.7,extent =180)
        fd(15)
        end_fill()
    pu()
    left(180)
    fd(40)
# the levels (draw them and set their numbers)
#-1 means (the hight would also unclude the first level that has 6 doors in
#this buildng)
    for level in range(num_levels -1):
        pd()
        fillcolor('brown')
        begin_fill()
        setheading(90)
        fd(25)
        right(10)
        fd(25)
        left(100)
        fd(208.5)
        left(100)
        fd(25)
        right(10)
        fd(25)
        end_fill()
        for building_A in range (9): # numbers of windows on level around this building
            fillcolor('gold')
            begin_fill()
            pd()
            right(180)
            fd(25)
            circle(-11.1,extent =180)
            fd(25)
            end_fill()
        pu()
        right(180)
        fd(50)
        
    #either this building has not been completing 
    if under_construction == "X":
        setheading(90)
        left(90)
        fd(150)
        
    #or the building has built and completed     
    else: 
        pu() 
        right(90)
        fd(4)
        left(80)
        pd()
        fillcolor('brown') #roof color
        pencolor('brown')
        begin_fill()
        fd(40)
        left(100)
        fd(20)
        right(100)
        fd(40)
        left(100)
        fd(195)
        left(100)
        fd(40)
        right(100)
        fd(20)
        left(100)
        fd(40)
        end_fill()
        left(80)
        #Set the clock and its color 
        pencolor('maroon')
        fillcolor('white')
        pu()
        fd(130)
        left(90)
        fd(40)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        left(90)
        fd(30)
        pd()
        width(5)
        right(30)
        fd(15)
        right(180)
        fd(15)
        width(3)
        left(60)
        fd(20)
        pu()
        
#building style 'B'
def building_b(num_levels, under_construction):
    setheading(90)
    pencolor('white')
    fillcolor('white')
    pu()
    right(90)
    fd(30)
    pd()
    begin_fill()
    fd(140)
    left(90)
    fd(45)
    left(90)
    fd(140)
    left(90)
    fd(45)
    end_fill()
    left(90)
    fillcolor('brown')
    begin_fill()
    fd(60)
    left(90)
    fd(40)
    right(90)
    fd(20)
    right(90)
    fd(40)
    end_fill()
    right(90)
    fd(15) 
    right(90)
    pu()
    fd(23)
    dot(5,'yellow')
    fd(23)
# the levels (draw them and set their numbers)
#-1 means (the hight would unclude the first level that has a door
    for level in range(num_levels -1):
        setheading(90)
        width (1)
        pencolor('white')
        left(90)
        fd(65)
        right(90)
        pd()
        fillcolor('royalblue')
        begin_fill()
        fd(35)
        right(90)
        fd(140)
        right(90)
        fd(35)
        right(90)
        fd(140)
        end_fill()
# the windows for the level
        pencolor('black')
        pu()
        right(90)
        fd(21)
        right(90)
        fd(65)
        left(90)
        fd(10)
        left (90)
        fd(60)
        left (90)
        fd(5)
        left(90)      
#the number of windows in each building
        for windows in range (5):
            pd()
            pencolor('black')
            fillcolor('white')
            begin_fill()
            right(90)
            fd(20)
            left(90)
            fd(20)
            left(90)
            fd(20)
            left(90)
            fd(20)
            left(180)
            pu()
            fd(26.5)
            fd(0.97)
            pd()
            end_fill()
            pu() 
        left(177)
        fd(77.7)
        right(90)
        fd(5)
#either this building has not completed yet
    if under_construction == "X":
       
        setheading(180)
        fd(45)

# or this building has completed  and (set the roof)
    else:
        pencolor('black')
        width(3)
        left(91)
        fd(22)
        pd()
        right(88)
        fd(20)
        right(110)
        pu()
        fd(57)
        pd()
        fillcolor('white')
        left(110)
        fd(20)
        begin_fill()
        right(90)
        fd(35)
        left(90)
        fd(35)
        left(90)
        fd(120)
        left(90)
        fd(35)
        left(90)
        fd(90)
        end_fill()
        pu()
        left(180)
        fd(90)
        right(170)
        fd(65)
        pd()
        pencolor('Black')
        #title of the roof for this building
        write("MICKEY MOUSE " , False, font=("Arial",10,"bold"),align="center")
        pu()
        left(40)
        fd(35)
        setheading(90)
        pd()
        # draw the MICKEY MOUSE's head
        fillcolor('black')
        begin_fill()
        setheading(0)
        circle(20)
        end_fill()
        begin_fill()
        pu()
        left(50)
        fd(45)
        pd()
        circle(10)
        end_fill()
        left(119)
        pu()
        fd(39)
        pd()
        setheading(90)
        begin_fill()
        circle(10)
        end_fill()
        pu()

#building style 'C'
def building_c(num_levels, under_construction):
    setheading(0)
    pencolor('white')
    fillcolor('white')
    setheading(0)
    left(180)
    fd(10)
    pd()
    begin_fill()
    right(90)
    fd(50)
    right(90)
    fd(220)
    right(90)
    fd(50)
    right(90)
    fd(220)
    end_fill()
    left(180)
# Draw the building_c's door
    pencolor('white')
    fillcolor('red')
    width(2)
    begin_fill()
    pu()
    fd(85)
    left(90)
    pd()
    fd(45)
    right(90)
    fd(50)
    right(90)
    fd(45)
    right(90)
    fd(50)
    end_fill()
    right(180)
    fd(25)
    left(90)
    fd(45)
    pu()
    left(90)
    fd(5)
    right(90)
    fd(6)
# the levels (draw them and set their numbers)
#-1 means (the hight would unclude the first level that has door
    for level in range(num_levels -1):
        pd()
        left(90)
        fd(104)
        pencolor('black')
        fillcolor('red')
        begin_fill()
        right(90)
        fd(49)
        right(90)
        fd(219)
        right(90)
        fd(50)
        end_fill()    
        right(90)
        fd(220)
        right(180)
        fd(10)
        left(90)
        pu()
        fd(5)
# draw 3 windows for the other level/s 
        for window in range (3):
            fillcolor('white')
            begin_fill()
            pd()
            fd(40)
            right(90)
            fd(55)
            right(90)
            fd(40)
            right(90)
            end_fill()
            fd(55)
            right(90)
            fd(20)
            right(90)
            fd(55)
            left(90)
            fd(20)
            left(90)
            fd(27.5)
            left(90)
            fd(40)
            left(90)
            pu()
            fd(45)
            left(90)
            end_fill()
        right(180)
        fd(5)
        right(90)
        fd(122.5)
        right(90)
        fd(51)
    # either the building is not completed and it is under construction
    if under_construction == "X":
        setheading(180)
        fd(45)
        pd()

    #or draw the building's roof and it has completed 
    else:
        width(1)
        pu()
        right(90)
        fd(5)
        pd()
        left(180)
        pencolor('white')
        fillcolor('white')
        begin_fill()
        fd(110)
        right(90)
        fd(25)
        right(90)
        fd(80)
        left(90)
        fd(25)
        right(90)
        fd(60)
        right(90)
        fd(25)
        left(90)
        fd(80)
        right(90)
        fd(25)
        right(90)
        fd(105)
        end_fill()
        pencolor('red')
        #building's roof title
        write("POKEMON " , False, font=("Arial",16,"bold"),align="center")
        #Set the POKEMON's ball 
        pencolor('white')
        fd(50)
        pd()
        right(90)
        pu()
        fd(95)
        pd()
        setheading(270)
        pd()
        pencolor('white')
        fillcolor('white')
        begin_fill()
        circle(47, extent= 180)
        end_fill()
        left(90)
        width(5)
        pencolor('black')
        setheading(90)
        pencolor('red')
        fillcolor('red')
        begin_fill()
        circle(47,extent=180)
        end_fill()
        left(90)
        pencolor('black')
        fd(32)
        fillcolor('white')
        begin_fill()
        setheading(270)
        circle(15)
        end_fill()
        left(90)
        pu()
        fd(10)
        pd()
        setheading(270)
        width(2)
        pencolor('grey')
        circle(5)
        width(5)
        left(90)
        pu()
        fd(18)
        pu()
        fd(2)
        pd()
        pencolor('black')
        fd(32)
        end_fill()
        pu()
#building style 'D'
def building_d(num_levels, under_construction):
    pencolor('pink')
    fillcolor('pink')
    setheading(90)
    begin_fill()
    right(90)
    fd(60)
    pd()
    left(90)
    fd(45)
    right(90)
    fd(80)
    right(90)
    fd(45)
    right(90)
    fd(80)
    end_fill()
    #draw the door of this building
    width(1)
    pencolor('black')
    left(180)
    pu()
    fillcolor('purple')
    begin_fill()
    fd(20)
    left(90)
    pd()
    fd(15)
    circle(-20, extent=180)
    fd(15)
    right(90)
    fd(40)
    end_fill()

# the levels (draw them and set their numbers)
#-1 means (the hight would unclude the first level that has door)
    for level in range(num_levels -1):
        width(2)
        setheading(180)
        pu()
        fd(22)
        pencolor('grey')
        fillcolor('darkred')
        begin_fill()
        right(90)
        fd(45)
        pd()
        right(90)
        fd(82)
        left(90)
        fd(45)
        left(90)
        fd(82)
        left(90)
        fd(45)
        end_fill()
        fillcolor('salmon') #windows color
        begin_fill()
        left(110)
        pu()
        fd(15)
        pd()
        left(70)
        fd(10)
        circle(-25,extent= 180)
        fd(10)
        right(90)
        fd(50)
        end_fill()
        right(180)
        fd(25)
        left(90)
        fd(35)
        pu()
        left(120)
        fd(25)
        pd()
        left(150)
        fd(43)
        pu()
        right(77)
        pu()
        fd(13)
        pd()
        right(103)
        fd(50)
        pu()
        right(90)
        fd(30)
        pu()
        right(90)
        fd(11)
        left(270)
        fd(45)
        right(90)
        fd(2.3)   
    pu()
    fd(22)
    right(90)
    fd(45)
    #either the building has not completed (in pregress) 
    if under_construction == "X":
        
        left(90)
        fd(5)
        setheading(180)
        fd(5)
        
    #or the building has not completed yet (Draw the roof)
    else :
        pd()
        fillcolor('salmon')
        begin_fill()
        fd(20)
        circle(-41,extent=180)
        fd(20)
        end_fill()
        right(115)
        pu()
        fd(40)
        pencolor('purple')
        write("HOTEL " , False, font=("Arial",14,"bold" ),align="center")
        pu()
        right(55)
        fd(45)
        pd()
        #draw 'welcome board'
        fillcolor('black')
        pencolor('black')
        begin_fill()
        left(80)
        fd(50)
        right(90)
        fd(30)
        right(90)
        fd(110)
        right(90)
        fd(30)
        right(90)
        fd(60)
        end_fill()
        pu()
        right(170)
        fd (10)
        pencolor('RED')
        #Set the WELCOME's name on the roof. 
        write("WELCOME " , False, font=("Arial",14,"bold" ),align="center")

# Erect buildings as per the provided city plan
def build_city(site):
    print('We have to draw', len(site), 'buildings!')
    for building in site:
# set the sizes (location) 
        if building[0] == 1:
            goto(-325,0)
        elif building[0] == 2:
            goto(-75,0)
        elif building[0] == 3:
            goto (175,0)
        elif building[0] == 4:
            goto (-475,-25)
        elif building [0] == 5:
            goto (-225,-25)
        elif building [0] == 6:
            goto(25,-25)
        elif building [0] == 7:
            goto(275,-25)
        elif building[0] == 8:
            goto(-375,-50)
        elif building[0] == 9:
            goto(-125, -50)
        else:
            building[0] == 10
            goto(125,-50)
    
        
       #building Details 
        if building[1] == 'A':
            building_a(building[2], building[3])
        elif building[1] == 'B':
            building_b(building[2], building[3])
        elif building[1] == 'C':
            building_c(building[2], building[3])
        else:
            building[1] == 'D'
            building_d(building[2], building[3])
        
        #if work is not completed (under construction )
        if building[3] == "X":
            #set under construction board
            pencolor('yellow')
            fillcolor('yellow')
            begin_fill()
            right(90)
            pu()
            fd(3)
            pd()
            fd(50)
            right(90)
            fd(100)
            right(90)
            fd(50)
            right(90)
            fd(100)
            end_fill()
            right(155)
            fd(60)
            pencolor('Black')
            #Set the titles of under construction board
            write("DANGER " , False, font=("Arial",11,"bold" ),align="center")
            right(115)
            pu()
            fd(13)
            pd()
            write("Construction  " , False, font=("Arial",9,"bold"),align="center")
            pu()
            fd(13)
            write("Work in progress  " , False, font=("Arial",9,"bold"),align="center")
            left(180)
            pd()
            pencolor('grey')
            fillcolor('white')
            width(1)
            pu()
            fd(41.5)
            begin_fill()
            right(90)
            pencolor('black')
            fd(47)
            pd()
            left(90)
            fd(60)
            left(90)
            fd(102)
            left(90)
            fd(60)
            end_fill()
            fd(42)
            left(90)
            fd(102)
            left(90)
            fd(55)
            pu()
            #set the Caution traingle 
            fillcolor('yellow')
            left(90)
            begin_fill()
            width(5)
            pu()
            fd(30)
            pd()
            fd(45)
            right(118.5)
            fd(45)
            right(118.5)
            fd(45)
            right(110)
            end_fill()
            pu()
            fd(18.5)
            #set the "!" sign for Caution traingles
            write("! " , False, font=("Arial",20,"bold"),align="center")
            pu()
            # or Draw the roof for each building
        else:
            building[3] = "O"
            width (1)
            
        

        
            
                      

        
            
    
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Yousif's city, (City Hall, Mickey Mouse, Pokemon, five stars Hotel) ")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
##build_city(fixed_plan_4) # <-- used for code development only, not marking
build_city(random_plan(15)) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()#

#--------------------------------------------------------------------#

