# Author: SolarCoder
# Instagraam | @solarcoder

from cv2 import imread, imwrite, threshold, THRESH_BINARY, COLOR_RGB2GRAY, cvtColor, resize, adaptiveThreshold, ADAPTIVE_THRESH_GAUSSIAN_C

PATH = "./python.jpg" # path to image

image = imread(PATH) # read image

image_height = image.shape[0] # get image height
image_width = image.shape[1] # get image width

# width in characters of terminal
#WIDTH = 179
WIDTH = 60
percent = WIDTH / image_width

# calculate height with percenttage
HEIGHT = int(image.shape[0] * percent)

# converting to grayscale
gray_scale = cvtColor(image, COLOR_RGB2GRAY)


# binary threshold
ret, converted = threshold(gray_scale, 200, 255, THRESH_BINARY)

# adaptive gaussian threshold
#converted = adaptiveThreshold(gray_scale, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 11, 2)

# resize to 179 pixels wide, with respective height 


resized = resize(converted, (WIDTH, HEIGHT))

   # resized = resize(image, (WIDTH, HEIGHT))

# outputting image to file
imwrite("sample_output.jpg", resized)

print(resized)
# printing to terminal
for row in resized:
    # counting pixel index in row
    for pixel_count, pixel in enumerate(row):
        if pixel == 0:
            print("0", end="")
        else:
            print(" ", end="")

        # make a new line once we reach the end of the row
        if pixel_count > WIDTH:
            print("\n")
        pixel_count += 1



