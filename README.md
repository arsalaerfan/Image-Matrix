# Image-Matrix

Made a dictionary for each color and an empty list with four values, 
a function which takes the image data and the dictonary as parameters which uses a nested loops to loop thorugh 
all image pixels and checks if the values at 0, 1, 2 are between certain ranges and if they are it increments 
each colors list at that index and stores them in the dictionary. We return the dictionary 
at the end of the function after its updated.

Made three seperate empty lists for each r,g,b colors and 
made a function loops through the images binary data and appends to all r,g,b
colors, red[0], green[1], blue[2], then after appending it sorts all three lists seperatly
and is put into one big list and we return the big list at the end of the function.
When we call the function it creates three seperate SVG files for each r,g,b colors
