

import cv2
import matplotlib.pyplot as plt

# Função que transforma um arquivo válido de imagem dando-lhe um aspecto de desenho rascunhado
def sketch(file_nm):
    img = cv2.imread(file_nm,cv2.IMREAD_COLOR)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gray_rev = 255 - img_gray

    img_gray_rev = cv2.GaussianBlur(img_gray_rev,(21,21),5,5)
    out = cv2.divide(img_gray, 255-img_gray_rev, scale = 230)
    # Para isso fazê-mos com que o software leia os tons de
    # preto e branco e os inverta, delineando a imagem
    saved = cv2.imwrite(f"sketch_{file_nm}", out)
    plt.imshow(out, cmap = "gray")

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return saved

def colored_draw(file_nm):
    img = cv2.imread(file_nm, cv2.IMREAD_COLOR)
    
    img_plot = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    out = cv2.stylization(img, sigma_s=40, sigma_r=0.5)
    out_plot = cv2.stylization(img_plot, sigma_s=40, sigma_r=0.5)
    saved = cv2.imwrite(f"colored_draw_{file_nm}", out)
    plt.imshow(out_plot)

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return out

if __name__ == "__main__":
    print(colored_draw("HT.jpg"))
   