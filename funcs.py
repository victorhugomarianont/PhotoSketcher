

import cv2
import matplotlib.pyplot as plt
import numpy as np

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
    
def old_photo(file_nm):
        
        
    mean = 0
    var = 10
    sigma = var ** 1.2
    img = cv2.imread(file_nm, cv2.IMREAD_COLOR)
    gaussian = np.random.normal(mean, sigma, (img.shape))  

    noisy_image = np.zeros(img.shape, np.float32)
    
    noisy_image = img + gaussian

    cv2.normalize(noisy_image, noisy_image, 0, 224, cv2.NORM_MINMAX, dtype=-1)
    old_img = noisy_image
    old_img = np.array(old_img, dtype=np.float64) # converting to float to prevent loss
    old_img = cv2.transform(old_img, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    old_img[np.where(old_img > 255)] = 255 # normalizing values greater than 255 to 255
    old_img = old_img.astype(np.uint8)
    
    saved = cv2.imwrite(f"OldLook_{file_nm}", old_img)
    old_img_out = old_img 
    old_img_out = cv2.cvtColor(old_img, cv2.COLOR_BGR2RGB)
    

    
    plt.imshow(old_img_out)
    plt.show()
    cv2.waitKey(0)
    
    
    
    
if __name__ == "__main__":
    print(old_photo("HT.jpg"))
   