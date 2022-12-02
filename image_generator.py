import requests
import find_images
import os

# Might need logic to create the directory if it does not exist
LOCATION = "../../Pictures/Desktop_Images/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

if(not(os.path.exists(LOCATION))):
    os.mkdir(LOCATION)

image_srcs = find_images.find_random_images()

for i in range(0, len(image_srcs)):
    try:
        response = requests.get(image_srcs[i], headers=HEADERS)

        with open(LOCATION+'img'+str(i)+'.png', 'wb') as f:
            f.write(response.content)
        del response
    except Exception as e:
        print(e)