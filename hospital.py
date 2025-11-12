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
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        
        
        self.Nameoftable=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        


        #=================Dataframe=====================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        
        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                                 font=("ariel",12,"bold"),text="patient information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                          font=("times new roman",12,"bold"),text="prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)
       
        # ============================ button frame==========================================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

       # ============================ Detail frame===========================================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # ============================DataframeLeft===========================================

        lblNameTablet=Label(DataframeLeft,text="Name of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftable,state="readonly",
                                                    font=("times new roman",12,"bold"),width=33)
                                                                                
        comNametablet["values"]=("Nice","corona vaccine","accellofennac","addrenall","amlodpiline","activan")  
        comNametablet.grid(row=0,column=1) 

        lblRef = Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2, pady=6)
        lblRef.grid(row=1, column=0, sticky=W)
        txtRef = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ref,width=35)
        txtRef.grid(row=1, column=1)

        lblDose=Label(DataframeLeft,font=("ariel", 12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("ariel", 13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("ariel",12,"bold"),text="No of Tablets::",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("ariel",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("ariel",12,"bold"),text="Issue  Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.Issuedate,width=35)
        txtLot.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("ariel",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("ariel",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("ariel",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("ariel",12,"bold"),text="Further Information",padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("ariel",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("ariel",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("ariel",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtstorage=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txtstorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("ariel",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("ariel",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("ariel",12,"bold"),text="NHS NUMBER:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("ariel",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("ariel",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("ariel",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("ariel",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)



        #  ===========================DataframeRight===================================
        self.txtPrescriptionText=Text(DataframeRight,font=("ariel",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescriptionText.grid(row=0,column=0)


        # =============================Button======================================
        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("ariel",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("ariel",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)


        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("ariel",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)


        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("ariel",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)


        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("ariel",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("ariel",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnExit.grid(row=0,column=5)


        # ==============================Table=======================================
        # ========================Scrollbar=========================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                    "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill="x")  
        scroll_y.pack(side=RIGHT,fill="y")                         
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS NUMBER")
        self.hospital_table.heading("pname",text="PATIENT NAME")
        self.hospital_table.heading("dob",text="DATE OF BIRTH")
        self.hospital_table.heading("address",text="ADDRESS")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100) 
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        




        # =======================Functionality Declaration===============================
        def iPrescriptionData(self):
            if self.Nameoftablets.get() == "" or self.ref.get() == "":
               messagebox.showerror("Error", "All fields are required")
            else:
                conn = mysql.connector.connect(host="localhost",username="root",passwords="Test@123",database="Mydata")
    
                my_cursor = conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
                                                                                                              self.Nameoftablets.get(),
                                                                                                              self.ref.get(),
                                                                                                              self.Dose.get(),
                                                                                                              self.NoofTablets.get(),
                                                                                                              self.Lot.get(),
                                                                                                              self.Issuedate.get(),
                                                                                                              self.ExpDate.get(),
                                                                                                              self.DailyDose.get(),
                                                                                                              self.StorageAdvice.get(),
                                                                                                              self.NhsNumber.get(),
                                                                                                              self.Pname.get(),
                                                                                                              self.Dob.get(),
                                                                                                              self.Address.get(),
                                                                                                              self.PatientId.get(),
                                                                                                              self.DoctorName.get()

                                                                                                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","record has been inserted")
root = Tk()
ob = Hospital(root)
root.mainloop() 