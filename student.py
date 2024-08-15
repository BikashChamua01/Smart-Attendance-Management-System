from tkinter import ttk
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation system")

        # ========= Variables =========#
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phn = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First image on the top
        img = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\smart-attendance.jpg")
        img = img.resize((510, 130), PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=1, width=510, height=130)
        # Second image on the top
        img1 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\face-recognition.png")
        img1 = img1.resize((510, 130), PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=1, width=510, height=130)
        # Third image on the top
        img2 = PIL.Image.open(
            r"D:\ATTENDENCE_PROJECT\images\gettyimages-1022573162.jpg"
        )
        img2 = img2.resize((510, 130), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=1, width=510, height=130)

        # Background image
        img3 = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\bg3.jpg")
        img3 = img3.resize((1530, 710), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="Student Management System",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # FRAME
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # ==========LEFT LABEL FRAME =============#
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=10, y=10, width=760, height=580)

        img_left = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\student_img.jpg")
        img_left = img_left.resize((720, 130), PIL.Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)

        # CURRENT COURSE
        current_course_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("times new roman", 12, "bold"),
        )
        current_course_frame.place(x=5, y=135, width=745, height=120)
        # DEPARTMENT
        dep_label = Label(
            current_course_frame,
            text="Department",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=0,
        )
        dep_label.grid(
            row=0,
            column=0,
            padx=10,
            sticky=W,
        )
        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_dep,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Department",
            "CSE",
            "Mechanical",
            "Civil",
            "Electrical",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        # COURSE
        course_label = Label(
            current_course_frame,
            text="Course",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
        )
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_course,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        course_combo["values"] = ("Select Course", "B.Tech", "BE", "MCA", "M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, sticky=W)
        # YEAR
        year_label = Label(
            current_course_frame,
            text="Yaer",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
        )
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        year_combo["values"] = (
            "Select year",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, sticky=W)

        # SEMESTER
        sem_label = Label(
            current_course_frame,
            text="Semester",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
        )
        sem_label.grid(row=1, column=2, padx=10, sticky=W)
        sem_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_sem,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        sem_combo["values"] = (
            "Select Semester",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
        )
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Second frame inside left frame
        # Class Student Information
        class_student_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Class Student Information",
            font=("times new roman", 12, "bold"),
        )
        class_student_frame.place(x=5, y=260, width=745, height=290)

        # StudentID
        studentID_label = Label(
            class_student_frame,
            text="StudentID:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        studentID_label.grid(row=0, column=0, padx=10, pady=3, sticky=W)
        studentID_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_id,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        studentID_entry.grid(row=0, column=1, padx=10, pady=3, sticky=W)

        # Student Name
        studentName_label = Label(
            class_student_frame,
            text="Student Name:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        studentName_label.grid(row=0, column=2, padx=10, pady=3, sticky=W)
        studentName_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        studentName_entry.grid(row=0, column=3, padx=10, pady=3, sticky=W)

        # Class Division
        classDivision_label = Label(
            class_student_frame,
            text="Class Division:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        classDivision_label.grid(row=1, column=0, padx=10, sticky=W)

        division_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_div,
            font=("times new roman", 12, "bold"),
            width=18,
            state="readonly",
        )
        division_combo["values"] = ("Select Division", "A", "B", "C", "D")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=10, sticky=W, pady=3)

        # classDivision_entry = ttk.Entry(
        #     class_student_frame,
        #     textvariable=self.var_div,
        #     width=20,
        #     font=("times new roman", 12, "bold"),
        # )
        # classDivision_entry.grid(row=1, column=1, padx=10, pady=3, sticky=W)

        # ROLL NUMBER
        roll_label = Label(
            class_student_frame,
            text="Roll No:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        roll_label.grid(row=1, column=2, padx=10, sticky=W)
        roll_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        roll_entry.grid(row=1, column=3, padx=10, pady=3, sticky=W)

        # GENDER
        gender_label = Label(
            class_student_frame,
            text="Gender:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 12, "bold"),
            width=18,
            state="readonly",
        )
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, sticky=W, pady=3)

        # gender_entry = ttk.Entry(
        #     class_student_frame,
        #     textvariable=self.var_gender,
        #     width=20,
        #     font=("times new roman", 12, "bold"),
        # )
        # gender_entry.grid(row=2, column=1, padx=10, pady=3, sticky=W)

        # DOB
        dob_label = Label(
            class_student_frame,
            text="DOB:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        dob_label.grid(row=2, column=2, padx=10, pady=3, sticky=W)
        dob_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=10, pady=3, sticky=W)

        # Email
        email_label = Label(
            class_student_frame,
            text="Email:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        email_label.grid(row=3, column=0, padx=10, pady=3, sticky=W)
        email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        email_entry.grid(row=3, column=1, padx=10, pady=3, sticky=W)

        # Phone No
        phn_label = Label(
            class_student_frame,
            text="Phone No:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        phn_label.grid(row=3, column=2, padx=10, pady=3, sticky=W)
        phn_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phn,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        phn_entry.grid(row=3, column=3, padx=10, pady=3, sticky=W)

        # Address
        Address_label = Label(
            class_student_frame,
            text="Address:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        Address_label.grid(row=4, column=0, padx=10, pady=3, sticky=W)
        Address_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        Address_entry.grid(row=4, column=1, padx=10, pady=3, sticky=W)

        # Teacher Name
        teacher_label = Label(
            class_student_frame,
            text="Teacher Name:",
            font=("times new roman", 12, "bold"),
            bg="white",
            padx=10,
            pady=3,
        )
        teacher_label.grid(row=4, column=2, padx=10, pady=3, sticky=W)
        teacher_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        teacher_entry.grid(row=4, column=3, padx=10, pady=3, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Take student Photo",
            value="Yes",
        )
        radiobtn1.grid(row=10, column=0, pady=2)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="No photo sample",
            value="No",
        )
        radiobtn2.grid(row=10, column=1, pady=2)

        # Button frame
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=10, y=200, width=720, height=32)

        # Save btn
        save_btn = Button(
            btn_frame1,
            command=self.add_data,
            text="Save",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17,
        )
        save_btn.grid(row=0, column=0)
        # update btn
        update_btn = Button(
            btn_frame1,
            command=self.update_data,
            text="Update",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17,
        )
        update_btn.grid(row=0, column=1)
        # delete btn
        delete_btn = Button(
            btn_frame1,
            command=self.delete_data,
            text="Delete",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17,
        )
        delete_btn.grid(row=0, column=2)

        # reset btn
        delete_btn = Button(
            btn_frame1,
            command=self.reset_data,
            text="Reset",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17,
        )
        delete_btn.grid(row=0, column=3)

        btn_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame2.place(x=10, y=233, width=720, height=32)
        # Take photo sample btn
        takePhoto_btn = Button(
            btn_frame2,
            command=self.generate_dataset,
            text="Take Photo Sample",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=35,
        )
        takePhoto_btn.grid(row=0, column=0)
        # Update photo sample btn
        takePhoto_btn = Button(
            btn_frame2,
            text="Update Photo Sample",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=35,
        )
        takePhoto_btn.grid(row=0, column=1)

        # ========== RIGHT LABEL FRAME=========== #
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        right_frame.place(x=780, y=10, width=680, height=580)

        img_right = PIL.Image.open(r"D:\ATTENDENCE_PROJECT\images\studentInfo.jpg")
        img_right = img_right.resize((670, 130), PIL.Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=2, y=0, width=670, height=130)

        # ===========Search System========= #
        search_frame = LabelFrame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        search_frame.place(x=3, y=135, width=670, height=70)

        search_label = Label(
            search_frame,
            text="Search by:",
            font=("times new roman", 15, "bold"),
            padx=10,
            pady=3,
            bg="white",
            fg="green",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            font=("times new roman", 12, "bold"),
            width=15,
            state="readonly",
        )
        search_combo["values"] = ("roll no", "name", "Phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=20, font=("times new roman", 12, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, pady=3, sticky=W)
        # Buttons to search
        search_btn = Button(
            search_frame,
            text="Search",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=7,
        )
        search_btn.grid(row=0, column=3, padx=2)
        # update btn
        showAll_btn = Button(
            search_frame,
            text="Show All",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=7,
        )
        showAll_btn.grid(row=0, column=4, padx=2)

        # ====Table Frame ===========#
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=210, width=670, height=350)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Div")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ========== Function Declaration =============#

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error !", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="bikash@1313",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phn.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Students Details Has been added Successfully"
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ========Fetch Data ============#
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="bikash@1313",
            database="face_recognizer",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =======Get Cursor ===========#
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phn.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # ===========Update Function ==============#
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno(
                    "Update",
                    "Do You want to update this student details",
                    parent=self.root,
                )
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="bikash@1313",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,`Div`=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phn.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )
                else:
                    if not update:
                        return

                messagebox.showinfo(
                    "Success", "Student Details Updated Successfully", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # ==========Delete Data==========#
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id Must be Mentioned")
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do You want to delete the data of this student?",
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="bikash@1313",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "delete from student where Student_id=%s",
                        (self.var_std_id.get(),),
                    )
                else:
                    return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted", "Deletion successful", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # ============ RESET FUNCTION =========#
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phn.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # =============Generate Data set or take Photo Sample====================#
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="bikash@1313",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute(
                    "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,`Div`=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phn.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1,
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ======Load Predefine data on face frontal open cv ======#
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray, 1.3, 5
                    )  # Scaling facotr=1.3  Minimum neighbor=5

                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                # cap = cv2.VideoCapture(0)
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = (
                            "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        )
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result", "Generating data set completed")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
