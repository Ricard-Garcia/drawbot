#Some basics of python in Drawbot

#Print "Hello World!"
print "Hello World!"

#Colours
fill(0,0,0.8) #Always use a dot not a comma
              #To convert 0-255 RGB values to 0-1, divide the (f.e.) 135 / 255
stroke(1,05,0.4)
strokeWidth(20)


#Draw an ellipses
oval(500,500,500,500)
oval(0,500,500,500)
oval(500,0,500,500)

stroke(None) #Without stroke width
oval(0,0,500,500)

#RG logic
print 2 ** 24
