# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# # kivy.require("1.0.1")

# class meomeo(App):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
    
#     def build(self):
#         return Label(text="Dau tay time")

# meomeo = meomeo()
# meomeo.run()




from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

# reading the image
img = imread('chess.jpg')
plt.axis("off")
plt.imshow(img)
print(img.shape)
resized_img = resize(img, (128*4, 64*4))
plt.axis("off")
plt.imshow(resized_img)
print(resized_img.shape)
fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")