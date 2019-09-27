import requests
import itertools
from PIL import Image
from random import shuffle
import time, sys
from IPython.display import clear_output
import math

def main():
    return 0

    

def update_progress(progress):
    bar_length = 50
    
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float) or progress < 0:
        progress = 0
    elif progress >= 1:
        progress = 1
        
    block = int(round(bar_length*progress))
    
    clear_output(wait = True)
    
    text = "Progress: [{0}] {1:.3f}%".format( "#" * block + "-" * (bar_length - block), 
        progress * 100)
    print(text)

image_path = 'Images/'
image_name = 'ProfArnav.jpg'
im = Image.open(image_path + image_name)
pix = im.load()