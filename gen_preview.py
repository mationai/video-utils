#! /usr/bin/env python

import sys, cv2, os
import numpy as np


def menu(kind=''):
    return '''Usage:
gen_%spreview.py IMAGE [output image width=720]
 -OR-
gen_%spreview.py VIDEO FRAME [output image width=720]
Eg:
gen_%spreview.py path/to/video.mp4 1
''' % (kind, kind, kind)

def preview_img_name_ext(kind=''):
    if len(sys.argv) < 2:
        print(menu(kind))
        exit()

    out_w = 720
    filepath = sys.argv[1]
    headpath, name_ext = os.path.split(filepath)
    filename, ext = name_ext.split('.')
    ext = ext.lower()
    imgexts = 'bmp dib jpeg jpg jpe jp2 png webp pbm pgm ppm sr ras tiff tif'.split()

    if ext not in imgexts: 
        if len(sys.argv) < 3:
            print(menu(kind))
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
    return img, filename, ext

def markdown_text(filepath, vidlink='https://youtu.be/VIDEO_ID'):
    return '''Markdown text:\n
![Alt text](PATH_TO/%s)](%s "Text")
''' % (filepath, vidlink)

if __name__ == '__main__':
    img, filename, ext = preview_img_name_ext()
    h, w = img.shape[:2]
    overlay = np.zeros((h, w, 3))

    tri_w, tri_h = 50, 50
    left = w//2 - tri_w//2
    right = left + tri_w

    pts = ((left, h//2+tri_h//2), (left, h//2-tri_h//2), (right, h//2))
    cv2.fillPoly(overlay, np.int32([pts]), (255,255,255))

    out = cv2.addWeighted(img, 1, np.uint8(overlay), 0.9, 0)
    filepath = "%s-preview%d.%s"%(filename, w, ext)
    cv2.imwrite(filepath, out)

    print('Preview image saved to %s'%filepath)
    print(markdown_text(filepath, 'VIDEO_URL'))
