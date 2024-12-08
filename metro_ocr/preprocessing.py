from PIL import Image
import cv2
from pytesseract import pytesseract
import numpy as np

pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

image_path = "bmap_metro.png"
image = cv2.imread(image_path)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([50, 50, 25])
upper = np.array([180, 255, 50])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imwrite('sat_fix.png', result)

'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 215, 255, cv2.THRESH_BINARY)

pro_img = "pro_bmap_metro.png"
cv2.imwrite(pro_img, thresh)

Image.fromarray(thresh)

_, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_img = "otsu_bmap_metro.png"
cv2.imwrite(otsu_img, otsu_thresh)

Image.fromarray(otsu_thresh)


ocr_result = pytesseract.image_to_string(Image.open(pro_img))
print(ocr_result)

import re

# Extract potential station names
lines = ocr_result.split("\n")
station_names = [line.strip() for line in lines if len(line.strip()) > 2]

# Remove duplicates
station_names = list(set(station_names))
print("Extracted Station Names:", station_names)
print(len(station_names))



man_station = ['Adarsh Nagar', 'Azadpur', 'Model Town', 'Guru Teg Bahadur Nagar', 'Vishwavidyalaya', 'Vidhan Sabha', 'Civil Lines', 'Kashmere Gate', 'Chandni Chowk', 'Chawri Bazar', 'New Delhi', 'Rajiv Chowk', 'Patel Chowk', 'Central Secretariat', 'Udyog Bhawan', 'Lok Kalyan Marg', 'Jor Bargh', 'Dilli Haat-INA', 'AIIMS', 'Green Park', 'Hauz Khas', 'Malviya Nagar', 'Saket', 'Qutab Minar', 'Majlis Park', 'Shalimar Bagh', 'Netaji Subhash Palace', 'Shakurpur', 'Punjabi Bagh West', 'ESI-Basaidarapur', 'Rajouri Garden', 'Mayapuri', 'Naraina Vihar', 'Delhi Cantt', 'Durgabai Desmukh South Campus', 'Sir M. Vishweshwaraiah Moti Bagh', 'Bhikaji Cama Place', 'Sarojini Nagar', 'South Extension', 'Lajpat nagar', 'Vinobapuri', 'Ashram']
'''