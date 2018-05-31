# Haar-cascade-traffic-signs
This is repository, that contains a variety of cascades for detecting some traffic signs and program for showing results. It works with images and webcam. There were used two feature desriptors (haar features and local binary patterns).

1.py contains code for getting backgroung (negative) images from image-net.org, converting them to grayscale and certain size, sorting them and creating file bg.txt with description, that's needed for cascade training.

2.py cointains code for cropping and converting to grayscale sample (positive) images.

3.py contains code that shows results of using trained cascades for detecting signes on test images and webcam stream.

signs.docx contains document with signs that can be printed and used for testing program with webcam.

All data for cascades (including all stages, positive and negative images) is stored on yandex disc, links will be provided.
Those files can be used for further training of cascades.

cascade_pesh_lbp14.xml is cacscade file, that was trained for detection of walkway sign, with local binary patterns (lbp) features, 14 stages.
https://yadi.sk/d/z440sxSj3WkrYL

cascade_stop_3_10.xml is cacscade file, that was trained for detection of stop sign, with haar features, 10 stages.
https://yadi.sk/d/dUTD4aKq3WkrYr

cascade_stop_3_15.xml is cacscade file, that was trained for detection of stop sign, with haar features, 15 stages.
https://yadi.sk/d/VUQ1Z2ro3WkrZA

cascade_stop_lbp14.xml is cacscade file, that was trained for detection of stop sign, with local binary patterns (lbp) features, 20 stages.
https://yadi.sk/d/DUelc9L33UgzhL

cascade_zapr_lbp13.xml is cacscade file, that was trained for detection of no entry sign, with local binary patterns (lbp) features, 14 stages.
https://yadi.sk/d/aCSa5BB03Wkt4t

Directories:

Angle test contains some images that were used for testing how angle of a sign affects detection accuracy, because Viola–Jones object detection algorythm highly depends on angles of positive images. It works best within 30 degrees range. 

Sample images contains positive images of signs.

Test images cointains images that were used for testing detection.

Learning screenshots are some screenshots of cascade classifier process, cascades with haar features took 5-7 days for training, with lbp features - 12-26 hours (but this time strongly depends on your hardware).

Process screenshots are screenshots of program detecting signs from image and webcam feed.

Negative images can be downloaded from here: https://yadi.sk/d/Io4c7Jq93WktEq

![screenshot1](https://github.com/Kollais/Haar-cascade-traffic-signs/blob/master/Process%20screenshots/c2.jpg)
![screenshot2](https://github.com/Kollais/Haar-cascade-traffic-signs/blob/master/Process%20screenshots/sk3.jpg)
![screenshot3](https://github.com/Kollais/Haar-cascade-traffic-signs/blob/master/Process%20screenshots/sk4.jpg)




