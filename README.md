# Licence_number_detection

This repositery has a method to detect number of licence plate. It use a pre trained yolo-licence-plate detection method to detect number plate. Then crop Region of interest from the image.
Then detect Text in the image using pytesseract

![html page](pic1.JPG "html page")

![Sample Input](pic.JPG "Input Image")
![Output](pic2.JPG "Sample final Output")

## How to employ?

You can download the weight file from [this](https://drive.google.com/file/d/1vXjIoRWY0aIpYfhj3TnPUGdmJoHnWaOc/ "this") link.

###Step to follow
clone the repositery

install all requirements from requirements.txt

run server.py

Can see its working at "http://ec2-18-224-29-99.us-east-2.compute.amazonaws.com/"
```

## used yolo-licence-plate detection model 
1. S. Khazaee, A. Tourani, S. Soroori, A. Shahbahrami, and C. Y. Suen, “**A Real-time License-Plate Detection Method using a Deep Learning Approach**,” 2nd International Conference on Pattern Recognition and Artificial Intelligence, Zhongshan, 2020. ([link](https://users.encs.concordia.ca/~icprai20/ "link"))

