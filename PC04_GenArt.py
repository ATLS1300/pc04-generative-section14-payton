#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:52:01 2021

@author: paytonobrien
"""

import turtle
import random

turtle.colormode(255)
turtle.Turtle()
turtle.Screen()
turtle.bgcolor(0,0,0)

turtle.shape ("turtle")
turtle.width(10)


palette = [(30,63,32),(52,88,48),(74,120,86),(148,236,190)]

#first square
turtle.goto(0,0)
turtle.pendown()
turtle.color(30,63,32)
turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.up()

#2nd square
turtle1 = turtle.Turtle()
turtle1.width(10)
turtle1.up()
turtle1.goto(100,70) 
turtle1.pendown()
turtle1.color(52,88,48)
turtle1.begin_fill()

for i in range(4):
    turtle1.forward(100)
    turtle1.left(90)
turtle1.end_fill()
turtle1.up()

#3rd square
turtle1.goto(100,-70) 
turtle1.down()
turtle1.color(74,120,86)
turtle1.begin_fill()
    
for i in range(4):
    turtle1.forward(100)
    turtle1.left(90)
turtle1.end_fill()
turtle1.up()

#4th square
turtle.goto(-100,70) 
turtle.down()
turtle.color(80,200,120)
turtle.begin_fill()
    
for i in range(4):
    turtle.forward(100)
    turtle.left(90)   
turtle.up()
turtle.end_fill()
    
#5th square
turtle.goto(-100,-70) 
turtle.down()
turtle.color(random.choice(palette))
turtle.begin_fill()
    
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.up()

turtle.ht()
turtle1.ht()
turtle.done()
    
    
    