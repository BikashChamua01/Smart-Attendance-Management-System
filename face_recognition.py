from tkinter import ttk
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Detect Face window")

        title_lbl = Label(
            self.root,
            text="Face recognition",
            font=("times new roman", 32, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(
            x=0,
            y=0,
            width=1530,
            height=50,
        )
        # !st image
        img_top = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), PIL.Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=650, height=700)

        # ==============2nd image=============#
        img_bottom = PIL.Image.open(
            r"D:\ATTENDENCE_PROJECT\images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg"
        )
        img_bottom = img_bottom.resize((950, 700), PIL.Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        s_lbl = Label(self.root, image=self.photoimg_bottom)
        s_lbl.place(x=650, y=50, width=950, height=700)

        # =========Button =============#
        btn1 = Button(
            s_lbl,
            command=self.face_rec,
            text="Face Recognization",
            cursor="hand2",
            font=("times new roman", 16, "bold"),
            bg="green",
            fg="white",
        )
        btn1.place(x=380, y=615, width=200, height=50)

    # ============Attendence Mark ===========#
    # def mark_attendence(self, i, r, n, d):
    #     with open("bikash.csv", "r+", newline="\n") as f:
    #         myDataList = f.readlines()
    #         name_list = []
    #         for line in myDataList:
    #             entry = line.split((","))
    #             name_list.append(entry[0])

    #         if (
    #             (i not in name_list)
    #             and (r not in name_list)
    #             and (n not in name_list)
    #             and (d not in name_list)
    #         ):
    #             now = datetime.now()
    #             d1 = now.strftime("%d/%m/%y")
    #             dtString = now.strftime("%H:%M:%S")
    #             f.writelines(f"\n {i},{r},{n},{d},{dtString},{d1},Present")

    def mark_attendance(self, i, r, n, d):
        with open("Attendence.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if i in name_list or r in name_list or n in name_list or d in name_list:
                print("Attendance already marked for this person.")
            else:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
                print("Attendance marked successfully.")

    # ========Face Recognition ============#

    def face_rec(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbor, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbor)

            coord = []

            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="bikash@1313",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_id=" + str(id)
                )
                n = my_cursor.fetchone()
                if n is None:
                    # Handle the case where no rows were returned
                    n = ""
                else:
                    n = str(n[0])  # convert single element tuple to a string
                n_list = n.split()  # split the string into a list of substrings
                n = "+".join(n_list)  # join the substrings with "+"
                # n=()
                # n = my_cursor.fetchone()
                # print(n)
                # # n=n[0]
                # n = "+".join(n)
                # if(not all(n)):
                #     n= n[0]

                my_cursor.execute(
                    "select Roll from student where Student_id=" + str(id)
                )
                r = my_cursor.fetchone()
                if r is None:
                    # Handle the case where no rows were returned
                    r = ""
                else:
                    r = str(r[0])  # convert single element tuple to a string
                r_list = r.split()  # split the string into a list of substrings
                r = "+".join(r_list)  # join the substrings with "+"

                # r=()
                # r = my_cursor.fetchone()
                # # r= r[0]
                # r = "+".join(r)
                # # if(not all(r)):
                # #     r= r[0]

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                if d is None:
                    # Handle the case where no rows were returned
                    d = ""
                else:
                    d = str(d[0])  # convert single element tuple to a string
                d_list = d.split()  # split the string into a list of substrings
                d = "+".join(d_list)  # join the substrings with "+"
                # d=()
                # d = my_cursor.fetchone()
                # # d= d[0]
                # d = "+".join(d)
                # # if(not all(d)):
                # #     d= d[0]
                my_cursor.execute(
                    "select Student_id from student where Student_id=" + str(id)
                )

                i = my_cursor.fetchone()
                if i is None:
                    # Handle the case where no rows were returned
                    i = ""
                else:
                    i = str(i[0])  # convert single element tuple to a string
                i_list = i.split()  # split the string into a list of substrings
                i = "+".join(i_list)  # join the substrings with "+"
                # i=()
                # i = my_cursor.fetchone()
                # # i = i[0]
                # i = "+".join(i)
                # # if(not all(i)):
                # #     i = i[0]
                if confidence > 77:
                    cv2.putText(
                        img,
                        f"ID:{i}",
                        (x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (237, 140, 140),
                        3,
                    )

                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (237, 140, 140),
                        3,
                    )

                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (237, 140, 140),
                        3,
                    )

                    cv2.putText(
                        img,
                        f"Department:{d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (237, 140, 140),
                        3,
                    )
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # video_cap = cv2.VideoCapture(0)
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # video_cap = cv2.VideoCapture(1)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognization", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        from with_attachment_email import send_emails


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()

       