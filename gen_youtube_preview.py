#! /usr/bin/env python

import sys, cv2
from os import path
from PIL import Image
from gen_preview import preview_img_name_ext, markdown_text

rect_w, rect_h = 79, 55

if __name__ == '__main__':
    img, filename, ext = preview_img_name_ext('youtube_')
    h, w = img.shape[:2]

    left = w//2 - rect_w//2
    top = h//2 - rect_h//2

    filepath = "%s-preview%d.%s"%(filename, w, 'png') # paste will produce artifacts if save in compressed jpg 
    cv2.imwrite(filepath, img)
    img = Image.open(filepath)


    icon = path.join(path.dirname(path.realpath(__file__)), "assets/play-mq.png")
    play = Image.open(icon)#"assets/play-mq.png")
    # play = Image.open("assets/play-mq.png")
    img.paste(play, (left, top), play)
    img.save(filepath)

    print('Preview image saved to %s'%filepath)
    print(markdown_text(filepath))
