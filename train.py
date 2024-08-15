from tkinter import ttk
from PIL import ImageTk
from student import Student
import PIL.Image
from tkinter import *
import os
import numpy as np
import cv2
from tkinter import messagebox


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation system")

        # ========Background image========#
        bg = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\background1.jpg")
        bg = bg.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # =====Title=========
        title_lbl = Label(
            bg_img,
            text="Train dataset Window",
            font=("times new roman", 35, "bold"),
            bg="darkblue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1530, height=49)

        # ========Button===========#
        b1 = Button(bg_img,command=self.train_classifier,text="Train Data", bg="yellow",fg="black")
        # bg_img,command=self.train_classifier text="Train data", cursor="hand2",bg="yellow",fg="black"
        b1.place(x=650, y=100, width=220, height=50)

    # ========Training data============ #
    def train_classifier(self):
        data_dir=(r"D:\ATTENDENCE_PROJECT\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=PIL.Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')  #datatype
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13  #Window will be closed when enter key is pressed
        
        # We are converting array to numpy to get 88 percent better performance
        ids=np.array(ids)

        # ============ Train The classifier and save=============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result","Training dataset completed")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
