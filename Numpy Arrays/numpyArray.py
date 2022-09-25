#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:22:20 2022

@author: abhay
"""

a = [1,2,3,4,5]
print(a*2)      # outputs the list two times
# but for image processing we need to multiply each element inside a list

newList = []

for i in a:
    '''print(i*2, end = " ")   # we get individual elements and that is a problem'''
    newList.append(i*2)
    
print(newList)
# still not a good idea as we have to type it again and again

#========#
# we use list comprehension

# advantage of comprehension is that we can use if else easily

compList = [i*2 for i in a]
print(compList)

listChk = [i**2 for i in a if i%2 == 0]
print(listChk)


# NUMPY ARRAYS

import numpy as np

'''
    We can get the shape of the arrays
'''

# 2-d array

list2d = [[1,2,3], [3, 4, 5]]

npArray = np.array(a)
print(npArray)

# converted to row and column matrix
list2darray = np.array(list2d)
print(list2darray)

# math operations in numpy arrays

print(npArray*2)   # does not repeat the list twice instead changes the values inside

# creating an array with all zeroes

zero = np.zeros((3, 4))
print(zero)

# creating an array with same values

value = np.full((3,3), 5)
print(value)


#=============#
# slicing in numpy

array = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
print(array)

print(array[:2])    #prints the first two rows
print(array[:, :2]) # all rows but only the first two columns
print(array[:2, 1:3])   #here 1 is inclusive but 3 in exclusive

# integer indexing

arr = np.array([[1,2], [3,4], [5,6]])
print(arr[2][1])    #prints the secon coulmn value for the third row (index from 0)

print(np.array([arr[0,0], arr[1,1], arr[2,0]]))

#===============#
# more maths on numpy arrays

x = np.array([[1,2], [3,4]], dtype=np.float64)  # we can define data types for arrays
y = np.array([[5,6], [7,8]], dtype=np.float64)

print(x)
print(y)

print(x+y)  # adds individual elements of each array
print(np.add(x, y))
print(np.multiply(x, y))    # this in not matrix multiplication but element wise multiplication

print(np.sum(x, axis = 0))    # sums all the elements in the array

'''
    axis = 0 ==> sums all the elements column wise
    axis = 1 ==> sums all the elements row wise
'''

# transposing a matrix
print(x)
print(x.T)

# adding array of two different sizes

firstArray = np.array([[1,2,3],[4,5,6], [7,8,9]])
secondArray = np.array([2,0,2])

print(firstArray + secondArray) # secondArray get added the each row of the firstArray

'''
    This phenomena is called broadcasting
'''

#=======================#
# reading images and maths on it

# Scipy for basic image processing

import cv2 as cv
img = cv.imread("../images/test.jpg")
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()