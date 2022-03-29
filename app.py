import tkinter as tk
import funcs
f_selector = 0

root = tk.Tk()
root.geometry("600x500")
canvas = tk.Canvas(root, width = 600,  height = 500)
canvas.grid(rowspan = 12, columnspan = 12)
root.iconbitmap("logo.ico")
    
def display_raw_img_button():
    button_raw_img = tk.Button(root, text = "Search image", command = lambda:funcs.open_file(), height = 2, width = 10, pady = 15 )
    button_raw_img.grid(column =5, row = 0)
    
    return button_raw_img
    
def display_selectors():     
    f_selector = tk.IntVar()

    r1 = tk.Radiobutton(root, text = "Sketch", variable = f_selector, value = 0 ).grid(column = 0, row = 3)
    r2 = tk.Radiobutton(root, text = "Colored draw", variable = f_selector, value = 1 ).grid(column = 0, row = 4)
    r3 = tk.Radiobutton(root, text = "Old photo", variable = f_selector, value = 2 ).grid(column = 0, row = 5)
    
    return f_selector    



def display_new_image_button():
    button_new_image = tk.Button(root, text = "Generate new image", command = lambda:retrieve_sel_op(), height = 2, width =10, pady = 15  )

    button_new_image.grid (column = 0, row = 8)
    
    return button_new_image
    
def retrieve_sel_op():
    sel = display_selectors()
   
    if sel.get() == 0:
        func = funcs.sketch(funcs.img_path())
        
    elif sel.get() == 1:
        pass
    elif sel.get() == 2:
       pass
 
    return func

    
display_raw_img_button()
display_selectors()
#retrieve_sel_op()
display_new_image_button()    
#funcs.sketch(funcs.img_path())
root.mainloop()

