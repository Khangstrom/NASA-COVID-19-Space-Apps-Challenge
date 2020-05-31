#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Space Apps 2020 Challenge
Food Will Hunting - Khang Nguyen, Rebecca Walters, Emily Faithful
"""

from PIL import Image
from PIL import ImageFilter
from os import chdir

chdir('...') # directory address
im = Image.open('map.png') # name of file

# size of image
h, w = im.size[1], im.size[0]

# convert image to b&w only
im_bw = im.convert('1')
im_bw_dilated = im_bw.filter(ImageFilter.ModeFilter(3))

# finding number of black pixels (corresponding to 50%+ of land
# being used for agriculture
i = 0
for x in range(w):
    for y in range(h):
        if im_bw_dilated.getpixel((x,y)) == 0:
            i = i + 1

green_area = (i/(h*w)) * 100
print("At least {:.2f}% of this land is used for agricultural purposes.".format(green_area))


