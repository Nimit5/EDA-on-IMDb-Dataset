import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Hello")
x=[1,2,3,4,5]
y=[10,20,30,20,10]
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()
