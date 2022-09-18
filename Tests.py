import numpy as np
from PIL import Image


pyimg = Image.new('RGB',(10,10))
ll = []
for i in range(100):

    ll.append((0,0,255)) # a tuple of RGB values
pyimg.putdata(ll)
pyimg.show() # drag open the pill view window to see (its not large enough)
print(ll)
