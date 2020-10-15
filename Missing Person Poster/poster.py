# load desired font for the poster
import matplotlib.font_manager as fm

def findFont(name='Arial'):
    possiblefonts = fm.findSystemFonts()
    return [f for f in possiblefonts if name in f]
prop = fm.FontProperties(fname='Arial.ttf')

# set the font to that font
import matplotlib
matplotlib.rcParams['font.family'] = prop.get_name()

# import various tools
import glob, os
import matplotlib.pyplot as plt, imageio, numpy as np
from PIL import Image

def poster(string='Missing Person Poster', filename='missing.jpg',
            size=(4.62, 6.93), margin=0, dpi=100):

    # define some scales
    xsize = float(size[0])
    ysize = float(size[1])
    aspect = ysize/xsize

    # load the image
    image = imageio.imread(filename)
    
    # create the plot
    plt.figure('poster', figsize=size, dpi=dpi)
    a = plt.subplot()
    a.cla()
    plt.setp(a.get_xticklabels(), visible=False)
    plt.setp(a.get_xticklines(), visible=False)
    plt.setp(a.get_yticklabels(), visible=False)
    plt.setp(a.get_yticklines(), visible=False)
    plt.subplots_adjust(left=margin/xsize, right=1.0 - margin/xsize, top=1.0 - margin/ysize, bottom=margin/ysize)

    # draw the background image
    a.imshow(image, interpolation='nearest', extent=[0, xsize, 0, ysize])

    name = input("Enter name of the missing person: ")
    contact = input("Enter the name of contact if the missing person is found: ")
    contact = 'PLEASE CONTACT ' + contact + ' IF FOUND'
    contact_nmbr = input("Enter contact number: ")
    contact_nmbr = 'Phone Number: +91-' + contact_nmbr
    age = input("Age of missing person: ")
    age = 'Age = ' + age
    height = input("Height of missing person: ")
    height = 'Height = ' + height
    weight = input("Weight of missing person: ")
    weight = 'Weight = ' + weight
    last_seen_location = input("Missing person last seen location: ")
    last_seen_location = 'Last seen Location = ' + last_seen_location
    profile_pic = input("Enter the name of the image of Missing person: ")

    a.text(2.31, 1.4, name.upper(), fontsize=20, ha='center', weight='bold', color='red')
    a.text(2.31, 0.5, contact.upper(), fontsize=12, ha='center', weight='bold', color='orangered')
    a.text(2.31, 0.35, contact_nmbr.upper(), fontsize=12, color='orangered', ha='center', weight='bold', va='top')
    a.text(2.31, 0.95, last_seen_location, fontsize=10, color='black', ha='center', weight='bold')
    a.text(2.31, 1.15, age + ' | ' + height + ' | ' + weight, fontsize=10, color='black', ha='center', weight='bold')    
    
    filename = string.replace(' ', '').replace('\n','') + '.png'
    print("Saving poster as", filename)
    plt.savefig(filename)
    plt.draw()
    
    img = Image.open(profile_pic).convert("RGBA")
    img = img.resize((320, 331), Image.ANTIALIAS)
    background = Image.open("MissingPersonPoster.png").convert("RGBA")
    background.paste(img, (71, 166), img)
    background.save('MissingPersonPoster.png',"PNG")

poster()