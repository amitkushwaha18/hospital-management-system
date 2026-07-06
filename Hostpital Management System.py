from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.NoOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.Storage_Advice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.PatientId=StringVar()
        self.NHSNumber=StringVar()
        self.PatientName=StringVar()
        self.DOB=StringVar()
        self.Address=StringVar()
        self.BloodPressure=StringVar()
        self.Medication=StringVar()

        




        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="+HOSPITAL MANAGEMENT SYSTEM+", fg="red", bg="white", font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ======================== DATA FRAME ========================

        Dataframe=Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)



        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                font=("times new roman",12,"bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)



        DataframeRight=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                font=("times new roman",12,"bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)


        #======================== BUTTONS FRAME ====================================

        Buttonframe=Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)



        #======================== DETAILS FRAME ====================================

        Detailsframe=Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)



        # ========================= DATA FRAME LEFT ===================================

        lblNameTablet=Label(DataframeLeft, text="Names of Tablets", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)


        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.NameOfTablets, state="readonly",
                                                    font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"]=("Aspirin", "Cetirizine", "Amoxicilline", "Ciprofloxacine", "Paracetamol", "Corona Vaccine", "Acetaminophen", "adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)


        lblref=Label(DataframeLeft,font=("arial", 12, "bold"), text="Reference No :", padx=2)
        lblref.grid(row=1,column=0, sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13, "bold"), textvariable=self.Ref, width=35)
        txtref.grid(row=1, column=1)


        lblDose=Label(DataframeLeft,font=("arial", 12, "bold"), text="Dose :", padx=2, pady=4)
        lblDose.grid(row=2,column=0, sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets=Label(DataframeLeft,font=("arial", 12, "bold"), text="No Of Tablets :",padx=2, pady=6)
        lblNoOfTablets.grid(row=3,column=0, sticky=W)
        txtNoOfTablets=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.NoOfTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot=Label(DataframeLeft,font=("arial", 12, "bold"), text="Lot :",padx=2, pady=6)
        lblLot.grid(row=4,column=0, sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate=Label(DataframeLeft,font=("arial", 12, "bold"), text="Issue Date :", padx=2, pady=6)
        lblIssueDate.grid(row=5,column=0, sticky=W)
        txtIssueDate=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.IssueDate, width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate=Label(DataframeLeft,font=("arial", 12, "bold"), text="Exp Date :", padx=2, pady=6)
        lblExpDate.grid(row=6,column=0, sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial", 12, "bold"), text="Daily Dose :", padx=2, pady=4)
        lblDailyDose.grid(row=7,column=0, sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial", 12, "bold"), text="Side Effect :", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0, sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13, "bold"),textvariable=self.SideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo=Label(DataframeLeft,font=("arial", 12, "bold"), text="Further Information :", padx=2)
        lblFurtherInfo.grid(row=0,column=2, sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("arial",12, "bold"),textvariable=self.FurtherInformation, width=35)
        txtFurtherInfo.grid(row=0, column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial", 12, "bold"), text="Blood Pressure :", padx=2, pady=6)
        lblBloodPressure.grid(row=1,column=2, sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",12, "bold"),textvariable=self.BloodPressure, width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage=Label(DataframeLeft,font=("arial", 12, "bold"), text="Storage_Advice :", padx=2, pady=6)
        lblStorage.grid(row=2,column=2, sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",12, "bold"),textvariable=self.Storage_Advice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine=Label(DataframeLeft,font=("arial", 12, "bold"), text="Medication :", padx=2, pady=6)
        lblMedicine.grid(row=3,column=2, sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",12, "bold"),textvariable=self.Medication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId=Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Id :", padx=2, pady=6)
        lblPatientId.grid(row=4,column=2, sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",12, "bold"),textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial", 12, "bold"), text="NHS Number :", padx=2, pady=6)
        lblNhsNumber.grid(row=5,column=2, sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",12, "bold"),textvariable=self.NHSNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName=Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Name :", padx=2, pady=6)
        lblPatientName.grid(row=6,column=2, sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",12, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial", 12, "bold"), text="Date Of Birth :", padx=2, pady=6)
        lblDateOfBirth.grid(row=7,column=2, sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",12, "bold"), textvariable=self.DOB, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Address :", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2, sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",12, "bold"), textvariable=self.Address, width=35)
        txtPatientAddress.grid(row=8, column=3)


        #========================== DATA FRAME RIGHT ==============================

        self.txtPrescription=Text(DataframeRight, font=("arial", 12, "bold"), width=46, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #=========================== BUTTONS =========================================


        btnPrescription = Button(Buttonframe, command=self.iPrescription, text="Prescription", bg="green", fg="white",
                         font=("arial", 12, "bold"))
        btnPrescription.grid(row=0, column=0, sticky="nsew")

        btnPrescriptionData = Button(Buttonframe, command=self.iPrescriptionData, text="Prescription Data", bg="green", fg="white",
                             font=("arial", 12, "bold"))
        btnPrescriptionData.grid(row=0, column=1, sticky="nsew")

        btnUpdate = Button(Buttonframe, command=self.update_data, text="Update", bg="green", fg="white",
                   font=("arial", 12, "bold"))
        btnUpdate.grid(row=0, column=2, sticky="nsew")

        btnDelete = Button(Buttonframe, command=self.idelete, text="Delete", bg="green", fg="white",
                   font=("arial", 12, "bold"))
        btnDelete.grid(row=0, column=3, sticky="nsew")

        btnClear = Button(Buttonframe, command=self.clear, text="Clear", bg="green", fg="white",
                  font=("arial", 12, "bold"))
        btnClear.grid(row=0, column=4, sticky="nsew")

        btnExit = Button(Buttonframe, command=self.iExit, text="Exit", bg="green", fg="white",
                 font=("arial", 12, "bold"))
        btnExit.grid(row=0, column=5, sticky="nsew")

        # =============== IMPORTANT LINE =================================

        for i in range(6):
            Buttonframe.grid_columnconfigure(i, weight=1)

        
        #======================== SCROLLBAR ====================================

        scroll_x=ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe, columns=("NameOfTable", "Ref", "Dose", "NoOfTablets", "Lot", "IssueDate",
                                                                "ExpDate", "DailyDose", "Storage_Advice", "NHSNumber", "PName", "Dob", "Address", "BloodPressure", "Medication", "PatientId", "FurtherInformation", "SideEffect"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("NameOfTable", text="Name Of Table")
        self.hospital_table.heading("Ref", text="Reference No.")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NoOfTablets", text="No Of Tablets")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("IssueDate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Exp Date")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("Storage_Advice", text="Storage_Advice")
        self.hospital_table.heading("NHSNumber", text="NHS Number")
        self.hospital_table.heading("PName", text="Patient Name")
        self.hospital_table.heading("Dob", text="DOB")
        self.hospital_table.heading("BloodPressure", text="Blood Pressure")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("PatientId", text="Patient ID")
        self.hospital_table.heading("FurtherInformation", text="Further Information")
        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("Address", text="Address")

        for col in self.hospital_table["columns"]:
            self.hospital_table.column(col, width=100, stretch=True)

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()




        # ======================== FUNTIONALITY DECLARATION =============================================


        # ========================== Prescription Data Button ==================================================
    def iPrescriptionData(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@Amit7800",
                database="Mydata"
            )

            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.NameOfTablets.get(),
                    self.Ref.get(),
                    self.Dose.get(),
                    self.NoOfTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.Storage_Advice.get(),
                    self.NHSNumber.get(),
                    self.PatientName.get(),
                    self.DOB.get(),
                    self.BloodPressure.get(),
                    self.Medication.get(),
                    self.PatientId.get(),
                    self.FurtherInformation.get(),
                    self.SideEffect.get(),
                    self.Address.get()
                )
            )

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))


    # =================================== update Button ===================================================================

    def update_data(self):
        if self.Ref.get() == "":
            messagebox.showerror("Error", "Reference No is required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@Amit7800",
                    database="mydata"
                )

                cursor = conn.cursor()

                cursor.execute("""
                    UPDATE hospital SET
                    NameOfTablets=%s,
                    Dose=%s,
                    NoOfTablets=%s,
                    Lot=%s,
                    IssueDate=%s,
                    ExpDate=%s,
                    DailyDose=%s,
                    Storage_Advice=%s,
                    NHSNumber=%s,
                    PatientName=%s,
                    DOB=%s,
                    BloodPressure=%s,
                    Medication=%s,
                    PatientId=%s,
                    FurtherInformation=%s,
                    SideEffect=%s,
                    Address=%s
                    WHERE Reference_No=%s
                """, (
                    self.NameOfTablets.get(),
                    self.Dose.get(),
                    self.NoOfTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.Storage_Advice.get(), 
                    self.NHSNumber.get(),
                    self.PatientName.get(),
                    self.DOB.get(),
                    self.BloodPressure.get(),
                    self.Medication.get(),
                    self.PatientId.get(),
                    self.FurtherInformation.get(),
                    self.SideEffect.get(),
                    self.Address.get(),
                    self.Ref.get()   # ✅ WHERE condition
                ))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Record Updated Successfully")

            except Exception as e:
                messagebox.showerror("Error", str(e))

    # =================================================== Prescription Button ===============================================================================

    def iPrescription(self):
        self.txtPrescription.delete("1.0", END)

        self.txtPrescription.insert(END, "Name Of Tablets:\t\t" + str(self.NameOfTablets.get()) + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t" + str(self.Ref.get()) + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + str(self.Dose.get()) + "\n")
        self.txtPrescription.insert(END, "No Of Table:\t\t" + str(self.NoOfTablets.get()) + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + str(self.Lot.get()) + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t" + str(self.IssueDate.get()) + "\n")
        self.txtPrescription.insert(END, "Exp Dat:\t\t" + str(self.ExpDate.get()) + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t" + str(self.DailyDose.get()) + "\n")
        self.txtPrescription.insert(END, "Storage_Advice :\t\t" + str(self.Storage_Advice.get()) + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t" + str(self.NHSNumber.get()) + "\n")
        self.txtPrescription.insert(END, "Patient Nam:\t\t" + str(self.PatientName.get()) + "\n")
        self.txtPrescription.insert(END, "DOB:\t\t\t" + str(self.DOB.get()) + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + str(self.BloodPressure.get()) + "\n")
        self.txtPrescription.insert(END, "Medication:\t\t\t" + str(self.Medication.get()) + "\n")
        self.txtPrescription.insert(END, "Patient Id:\t\t\t" + str(self.PatientId.get()) + "\n")
        self.txtPrescription.insert(END, "FurtherInformation:\t\t\t" + str(self.FurtherInformation.get()) + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + str(self.SideEffect.get()) + "\n")
        self.txtPrescription.insert(END, "Address:\t\t" + str(self.Address.get()) + "\n")


    # ================================== Delete Button ====================================================================

    def idelete(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@Amit7800",
                database="Mydata"
            )

            cursor = conn.cursor()
            query="delete from hospital where Reference_No=%s"
            value=(self.Ref.get(),)
            cursor.execute(query, value)

            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Delete", "Patient has been deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))




    # ==================================== Clear Button ================================================================

    def clear(self):
        self.NameOfTablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.Storage_Advice.set("")
        self.PatientId.set("")
        self.NHSNumber.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Address.set("")
        self.DailyDose.set("")
        self.Medication.set("")
        self.BloodPressure.set("")
      
        self.txtPrescription.delete("1.0", END)


    # ===========================================================================================================================================


    def fetch_data(self):
        conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@Amit7800",
                database="Mydata"
            )

        cursor = conn.cursor()

        cursor.execute("select * from hospital")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameOfTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NoOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Storage_Advice.set(row[8])
        self.NHSNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DOB.set(row[11])
        self.Address.set(row[12])
        self.BloodPressure.set(row[13])
        self.Medication.set(row[14])
        self.PatientId.set(row[15])
        self.FurtherInformation.set(row[16])
        self.SideEffect.set(row[17])


    #================================= Exit Button ======================================================

    def iExit(self):
        self.iExit=messagebox.askyesnocancel("Hospital Management System", "Confirm you want to exit")
        if self.iExit>0:
            root.destroy()
            return
        
    # ==========================================================================================================



root = Tk()
ob = Hospital(root)
root.mainloop()

