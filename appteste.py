#%matplotlib inline activate magic functions
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image


# Função que gera uma usa uma imagem com o nome descrito na string da linha dez (mesmo diretorio do app) e
# Salva as alterações feitas criando uma nova imagem com o nome da linha 20
def sketch():
    img = cv2.imread("woman.jpg",cv2.IMREAD_COLOR)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gray_rev = 255 - img_gray

    img_gray_rev = cv2.GaussianBlur(img_gray_rev,(21,21),5,5)
    out = cv2.divide(img_gray, 255-img_gray_rev, scale = 230)

    saved = cv2.imwrite("Drawn_woman.jpg", out)
    plt.imshow(out, cmap = "gray")

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return saved
print(sketch())