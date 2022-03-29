#%matplotlib inline activate magic functions

import cv2
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfile
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk
import os
import sys
image_path = ""


def open_file():
    
   file_img = askopenfile(mode = "rb", filetypes = [("JPG Files","*.jpg"), ("PNG Files","*.PNG")])
   if file_img:
        loaded_img = ImageTk.PhotoImage(Image.open(file_img))
        img = loaded_img
        img_label = Label(image = img, bg = "white")
        img_label.image = img
        img_label.grid(column = 1, row =1)
     
        return img
    
def img_path():
    path = sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                os.path.pardir
            )
        )
    )
    return path
    

def sketch(image_path):
    img = cv2.imread(image_path,cv2.IMREAD_COLOR)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gray_rev = 255 - img_gray

    img_gray_rev = cv2.GaussianBlur(img_gray_rev,(21,21),5,5)
    out = cv2.divide(img_gray, 255-img_gray_rev, scale = 230)

    saved = cv2.imwrite("experimental.jpg", out)
    plt.imshow(out, cmap = "gray")

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return saved
    

if __name__ == "__main__":
   image_path = img_path()
   print(image_path)