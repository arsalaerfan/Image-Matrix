#Author: Erfanullah Arsala and Joel Terran
#Date: 9/22/19
#CST205
#Code description:
'''
Made a dictionary for each color and an empty list with four values, 
a function which takes the image data and the dictonary as parameters which uses a nested loops to loop thorugh 
all image pixels and checks if the values at 0, 1, 2 are between certain ranges and if they are it increments 
each colors list at that index and stores them in the dictionary. We return the dictionary 
at the end of the function after its updated.

'''

import pickle

#myBin makes a empty dict for each r,g,b color and holds four values 
myBin = {'red':[0, 0, 0, 0],
         'green':[0, 0, 0, 0],
         'blue':[0, 0, 0, 0]}

#get matrix binary data with pickle
count = pickle.load(open("image_matrix", "rb"))

#function to modify the myBin dict, increments each value if its within the certian range 
def histogram(count, myBin):
  #use nested loop to loop over all values to image_matrix
  for pix in count:
    for i in pix:

      #if the first value in data tuple is 0-63 we increment the first red index value by 1
      if i[0] <= 63:
        myBin['red'][0] += 1
      #if number is 64-127 we increment the second red index value by 1
      elif (i[0] >= 64) and (i[0] <= 127): 
        myBin['red'][1] += 1
      #if number is 128-191 we increment the third red index value by 1
      elif (i[0] >= 128) and (i[0] <= 191):
        myBin['red'][2] += 1
      #if number is 192-255 we increment the fourth red index value by 1 
      elif (i[0] >= 192) and (i[0] <= 255): 
        myBin['red'][3] += 1

      #if the second value in data tuple is 0-63 we increment the first green index value by 1
      #we do the exact same fo both geen and blue as we did for red
      if i[1] <= 63:
        myBin['green'][0] += 1
      elif (i[1] >= 64) and (i[1] <= 127): 
        myBin['green'][1] += 1
      elif (i[1] >= 128) and (i[1] <= 191):
        myBin['green'][2] += 1
      elif (i[1] >= 192) and (i[1] <= 255): 
        myBin['green'][3] += 1
      
      #if the thrid value in data tuple is 0-63 we increment the first blue index value by 1
      #we do the exact same fo both geen and blue as we did for red
      if i[2] <= 63:
        myBin['blue'][0] += 1
      elif (i[2] >= 64) and (i[2] <= 127):
        myBin['blue'][1] += 1
      elif (i[2] >= 128) and (i[2] <= 191):
        myBin['blue'][2] += 1
      elif (i[2] >= 192) and (i[2] <= 255):
        myBin['blue'][3]+= 1
  #return the dictionary after updating each r,g,b lists
  return myBin

#call function with image data and the dict
histogram(count, myBin)
