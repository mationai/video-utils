## Python Command Line Video Utilities

Python Command Line Utilities for videos

### Generate an Embedded Video preview image that works in markdown

Currently, to embed a video such as youtube video, you need to include the iframe into the html. This is a problem in markdown as iframes are not allowed.

[Stack Overflow](https://stackoverflow.com/questions/11804820/embed-a-youtube-video) has a nice solution around it. Instead of inserting the iframe, insert a video preview image to indicate to user it is a video. The image will however be a link to the youtube site instead of embedded in the page. It is a nice hack. However, it requires the user to capture a screen shot of the video.  An easier way is to generate that image with a command line utility instead.

#### Requirements
`cv2` and `numpy`

#### Usage
``` 
video-play-thumb.py IMAGE [output image width=720]
 -OR-
video-play-thumb.py VIDEO FRAME [output image width=720]
```

This will generate a video preview image from either an image or a video. The preview indication is the "Play" triangle icon in the center of image. Sample output:

![](assets/out-yellow-720thumb.jpg "Embedded Video Preview Image")

