#! /usr/bin/env python

import sys, cv2
import numpy as np

menu = ''' Usage:
gen-video-preview.py IMAGE [output image width=720]
 -OR-
gen-video-preview.py VIDEO FRAME [output image width=720]
'''

out_w = 720
tri_w, tri_h = 50, 50

if len(sys.argv) < 2:
    print(menu)
    exit()

filepath = sys.argv[1]
filename, ext = filepath.split('.')
ext = ext.lower()
imgexts = 'bmp dib jpeg jpg jpe jp2 png webp pbm pgm ppm sr ras tiff tif'.split()

if ext not in imgexts: 
    if len(sys.argv) < 3:
        print(menu)
        exit()
    frame = int(sys.argv[2]) 

    cap = cv2.VideoCapture(filepath)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
    ok, img = cap.read()
    cap.release()
    ext = 'jpg'
    if len(sys.argv) > 3:
        out_w = int(sys.argv[3])
else:
    img = cv2.imread(filepath)
    if len(sys.argv) > 2:
        out_w = int(sys.argv[2])

h, w = img.shape[:2]
ratio = out_w/w
out_h = int(h * ratio)

if out_w != w and out_h != h:
    img = cv2.resize(img, (out_w, out_h), interpolation=cv2.INTER_AREA)
    h, w = img.shape[:2]
overlay = np.zeros((h, w, 3))

left = w//2 - tri_w//2
right = left + tri_w

pts = ((left, h//2+tri_h//2), (left, h//2-tri_h//2), (right, h//2))
cv2.fillPoly(overlay, np.int32([pts]), (255,255,255))

out = cv2.addWeighted(img, 1, np.uint8(overlay), 0.9, 0)
cv2.imwrite("%s-preview%d.%s"%(filename,out_w,ext), out)