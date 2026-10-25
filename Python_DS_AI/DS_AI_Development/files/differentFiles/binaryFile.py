# importing PIL - for opening, manipulating, and saving image files
from PIL import Image 

# Module -  for downloading files from URLs
import urllib.request

# Downloading dataset
url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
fileName = "dog.jpg"

urllib.request.urlretrieve(url, fileName)

# Read image 
img = Image.open('dog.jpg') 
  
# Output Images 
#display(img) #Jupyter Notebook only function
img.show()
print(img.size)       # (width, height) tuple
print(img.format)     # 'JPEG', 'PNG', etc.
print(img.mode)       # 'RGB', 'L' (grayscale), etc.

"""
# Resize
img_resized = img.resize((300, 300))

# Rotate
img_rotated = img.rotate(90)

# Crop (left, top, right, bottom)
img_cropped = img.crop((100, 100, 400, 400))

# Convert to grayscale
img_gray = img.convert('L')

# Save in different format
img.save('dog_copy.png')
"""