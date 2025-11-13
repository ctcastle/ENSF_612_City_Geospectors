import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
import wget 
url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME=2005-01-23T00:00:00Z&BBOX=50.8265,-114.2768,51.2659,-113.8374&CRS=EPSG:4326&' \
'LAYERS=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines_15m&WRAP=day,x&FORMAT=image/jpeg&WIDTH=200&HEIGHT=200&colormaps=,&MARKER=-114.0571,51.0451&ts=1762274844460'
im = wget.download(url,'test.jpg')
ima = cv2.imread(im)
cv2.imshow('Original Imagesodiuhag', ima)

image = cv2.imread('snapshot-2005-01-23T00_00_00Z.jpg') 

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# These values are approximate and may need adjustment based on the specific shade of green
lower_green = np.array([37, 40, 40]) # Hue, Saturation, Value
upper_green = np.array([85, 255, 255])

image_mask = cv2.inRange(image_hsv, lower_green, upper_green)
image_inverted_mask = cv2.bitwise_not(image_mask)
image_result = cv2.bitwise_and(image, image, mask=image_inverted_mask)
image_result = cv2.cvtColor(image_result, cv2.COLOR_BGR2GRAY)

threshold_value = 70  
max_value = 255

ret, image_bitmask = cv2.threshold(image_result, threshold_value, max_value, cv2.THRESH_BINARY)


height, width = image_bitmask.shape
print(f"size: {image.itemsize}")
print(f"height: {height}, width: {width}")
print(f"{cv2.countNonZero(image_bitmask)*.036925:.2f}km^2")

cv2.imshow('Original Image', image)
cv2.imshow('Black and White Bitmask', image_bitmask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Main workflow 
# Generate a dataframe: month, day, year, origin_lat, origin_lon, width_lat, width_lon, base_url, other_params 
# Preselect by month 
# Request images 
# Filter by ML predicted usability (filtering clouds, snow, and amount of contrast between city/surroundings) 
# Perform manual processing/estimation 
# Minimum I want to reduce outlier city centers like airedrie 
# Or perform ML estimation 

# data = np.fromfile('20050708.jpg', dtype=np.int8)
# cv2.imshow('Compressed?', data)
# print(f"data size: {data.shape}")