from tkinter import ttk
from PIL import ImageTk
from student import Student
import PIL.Image
from tkinter import *
import os
import cv2
from tkinter import messagebox
import numpy as np
from face_recognition import Face_recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation system")
        # First image on the top
        img = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\aec.jpeg")
        img = img.resize((1530, 200), PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=1, width=1530, height=200)

        # Background image
        img3 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\bg3.jpg")
        img3 = img3.resize((1530, 710), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="FACE RECOGNIZATION ATTENDENCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # STUDENT BUTTON
        img4 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\student.jpg")
        img4 = img4.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2"
        )
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        # DETECT FACE BUTTON
        img5 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\detection.jpg")
        img5 = img5.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(
            bg_img, command=self.face_data, image=self.photoimg5, cursor="hand2"
        )
        b2.place(x=500, y=100, width=220, height=220)

        b2_2 = Button(
            bg_img,
            command=self.face_data,
            text="Take Attendance",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b2_2.place(x=500, y=300, width=220, height=40)

        # ATTENDANCE FACE BUTTON
        img6 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\attendance.jpg")
        img6 = img6.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_3 = Button(
            bg_img,
            text="Atttendance",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b3_3.place(x=800, y=300, width=220, height=40)

        # Help Desk BUTTON
        img7 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\helpdesk.jpg")
        img7 = img7.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_4 = Button(
            bg_img,
            text="Help Desk",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b4_4.place(x=1100, y=300, width=220, height=40)

        # Train Face BUTTON
        img8 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\train4.jpg")
        img8 = img8.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(
            bg_img, command=self.train_classifier, image=self.photoimg8, cursor="hand2"
        )
        b5.place(x=200, y=380, width=220, height=220)

        b5_5 = Button(
            bg_img,
            command=self.train_classifier,
            text="Train Data",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b5_5.place(x=200, y=580, width=220, height=40)

        # Photos BUTTON
        img9 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\photos.webp")
        img9 = img9.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b6.place(x=500, y=380, width=220, height=220)

        b6_6 = Button(
            bg_img,
            command=self.open_img,
            text="Photos",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b6_6.place(x=500, y=580, width=220, height=40)

        # Developers BUTTON
        img10 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\developers.jpg")
        img10 = img10.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)

        b7_7 = Button(
            bg_img,
            text="Developers",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b7_7.place(x=800, y=580, width=220, height=40)

        # Exit BUTTON
        img11 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\exit1.jpg")
        img11 = img11.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)

        b8_8 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b8_8.place(x=1100, y=580, width=220, height=40)

    # =========Functions Buttonns ============ #
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # =======Open Image folder ==========#
    def open_img(self):
        os.startfile("data")

    # ========Training data============ #
    def train_classifier(self):
        data_dir = r"D:\ATTENDENCE_PROJECT\data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = PIL.Image.open(image).convert("L")  # Gray scale image
            imageNp = np.array(img, "uint8")  # datatype
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13  # Window will be closed when enter key is pressed

        # We are converting array to numpy to get 88 percent better performance
        ids = np.array(ids)

        # ============ Train The classifier and save=============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", "Training dataset completed")

    # ============Face recognition data=======#
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
