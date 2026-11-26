

import  mysql.connector


class Hospital_db:
    def __init__(self):
        try:

            self.con=mysql.connector.connect(user="root",
                                             password="aleena",
                                             host="localhost",
                                             database="hospital_management")
        except:
            print("connection failed")
            self.con=None

    def create(self,patient_name,age,phone,department,doctor_name,appointment_date):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="insert into patients(patient_name,age,phone,department,doctor_name,appointment_date) values(%s,%s,%s,%s,%s,%s)"
            data=(patient_name,age,phone,department,doctor_name,appointment_date)
            cursor.execute(query,data)
            self.con.commit()
            print("patient registered successfully")
        except Exception as e:
            print("failed to register")
        finally:
            cursor.close()

    def view(self):
        if self.con is None:
            return

        try:
            cursor=self.con.cursor()
            query="select patient_id,patient_name,age,phone,department,doctor_name,appointment_date from patients"
            cursor.execute(query)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print("No records to display")
        except Exception:
            print("No records")
        finally:
            cursor.close()

    def search(self,patient_id):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="select patient_id,patient_name,age,phone,department,doctor_name,appointment_date from patients where patient_id=%s"
            cursor.execute(query,(patient_id,))
            records=cursor.fetchone()
            if records:
                print(records)
            else:
                print("No record")
        except Exception:
            print("no record found")
        finally:
            cursor.close()

    def update(self,patient_id,appointment_date):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="update patients set appointment_date=%s where patient_id=%s"
            data=(appointment_date)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount > 0:
                print("patient_id",patient_id,"updated successfully")
            else:
                print("No records to update")
        except Exception:
            print("No records to update")
        finally:
            cursor.close()


    def delete(self,patient_id):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="delete from patients where patient_id=%s"
            cursor.execute(query,patient_id)
            self.con.commit()
            if cursor.rowcount >0:
                print(patient_id," Patient_id deleted successfully")
            else:
                print("Patent_id",patient_id,"not found")
        except Exception:
            print("no records to delete")
        finally:
            cursor.close()

    def summary(self):
        if self.con is None:
            return
        try:
            cursor=self.con.cursor()
            query="select avg(age),patient_name,department count(*) from patients group by patient_name, departments"
            data=(patient_name,age,department)
            cursor.execute(query,data)
            self.con.commit()
            records=cursor.fetchall()
            if records:
                print(records)
            else:
                print("nothing to display")
        except Exception:
            print("No records to display")
        finally:
            cursor.close()


h=Hospital_db()

while(True):
    print("HOSPITAL MANAGEMENT")
    print("1.Register Patient")
    print("2.View Appointments")
    print("3.search Patient")
    print("4.Update Appointment date")
    print("5.Delete Patient Record")
    print("6.Department Summary")
    print("7.Exit")

    ch=int(input("enter the choice:"))
    if ch==1:
        patient_name=input("enter the patient_name:")
        age=int(input("enter the age:"))
        phone=int(input("enter the phone number:"))
        department=input("enter the department:")
        doctor_name=input("enter the doctor name:")
        appointment_date=input("enter the appointment date:")
        h.create(patient_name,age,phone,department,doctor_name,appointment_date)

    elif ch==2:
        h.view()

    elif ch==3:
        patient_id=int(input("enter the patient_id:"))
        h.search(patient_id)

    elif ch==4:
        patient_id=int(input("enter the patient id:"))
        appointment_date=input("enter the appointment date:")
        h.update(patient_id,appointment_date)

    elif ch==5:
        patient_id=int(input("enter the patient id:"))
        h.delete(patient_id)

    elif ch==6:
        h.summary()

    else:
        print("exiting...")
        break







