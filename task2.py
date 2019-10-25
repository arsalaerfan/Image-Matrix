#Author: Erfanullah Arsala and Joel Terran
#Date: 9/22/19
#CST205
#Code description:
'''
Made three seperate empty lists for each r,g,b colors and 
made a function loops through the images binary data and appends to all r,g,b
colors, red[0], green[1], blue[2], then after appending it sorts all three lists seperatly
and is put into one big list and we return the big list at the end of the function.
When we call the function it creates three seperate SVG files for each r,g,b colors

'''

import pickle
import hw1_hist_plotter as hp

#get image with pickle
image = pickle.load(open("image_matrix", "rb"))

#make three empty lists for r,g,b values
red = []
green = []
blue = []


#use nested loop to append all data from image into r,g,b lists
def histogram(image):
	for val in image:
		for i in val:
			#append all values of data into r,g,b lists, red[0], green[1], blue[2]
			red.append(i[0])
			green.append(i[1])
			blue.append(i[2])
	#after we append everything into three seperate lists we sort each one
	red.sort()
	green.sort()
	blue.sort()
	#stores all sorted r,g,b lists in one big list called myList
	myList = [red,green,blue]
	#return myList with all three r,g,b lists in one big list
	return myList


#call the hw1_hist_plotter with myList as a paramater which holds the r,g,b lists
hp.hist_plotter(histogram(image))



