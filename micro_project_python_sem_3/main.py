# import os
class DatabaseMethod:
    def __init__(self,studentsdata):
        self.studentsdata = studentsdata
    def __printone__(self,data):
        print(f"En_no: {data[0]}")
        print(f"Firstname: {data[1]}")
        print(f"Lastname: {data[2]}")
        print(f"Phone NO: {data[3]}")
    def __check_en_no__(self,data):
        if len(self.studentsdata):
            for i,j in enumerate(self.studentsdata):
                if j[0] == data:
                    return {"status":True,"index":i}
            else:
                return {"status":False,"index":None}
        else:
            return {"status":False,"index":None}
    def Check_En_no(self,en_no):
        if len(self.studentsdata):
            for i in self.studentsdata:
                if i[0] == en_no:
                    return True
            else:
                return False
        else:
            return False
    def add(self,data):
        self.studentsdata.append(data)
    def printdata(self):
        if len(self.studentsdata):
            for i in self.studentsdata:
                print(f"En_no: {i[0]}")
                print(f"Firstname: {i[1]}")
                print(f"Lastname: {i[2]}")
                print(f"Phone NO: {i[3]}")
                print("--------")
        else:
            print("No Record Found")
    def find(self,command):
        if len(self.studentsdata):
            for student in self.studentsdata:
                if command == str(student[0]) or command.lower() == student[1].lower() or command.lower()== student[2].lower() or command == str(student[3]):
                    self.__printone__(student)
            else:
                print("No Record found")
        else:
            print("No Record found")
    def update(self):
        Student_En_No = int(input("Enter Student En_No: "))
        checkdata = self.__check_en_no__(Student_En_No)
        if checkdata["status"]:
            self.__printone__(self.studentsdata[checkdata["index"]])
            print("En No 1, Firstname 2, Lastname 3, Phone No 4")
            userinput = int(input("Enter what do you whant to update: "))
            match userinput:
                case 1:
                    try:
                        new_en_no = int(input("Enter new En_No: "))
                        if not self.Check_En_no(new_en_no):
                            self.studentsdata[checkdata["index"]][0] = new_en_no
                            print("Updated successfully")
                        else:
                            print("Enrollment already exists")
                    except:
                        print("Enter only Number")
                case 2:
                    new_fname = input("Enter new Firstname: ")
                    self.studentsdata[checkdata["index"]][1] = new_fname
                    print("Updated successfully")
                case 3:
                    new_lname = input("Enter new Lastname: ")
                    self.studentsdata[checkdata["index"]][2] = new_lname
                    print("Updated successfully")
                case 4:
                    try:
                        new_phone_no = int(input("Enter new Phone No: "))
                        self.studentsdata[checkdata["index"]][3] = new_phone_no
                        print("Updated successfully")
                    except:
                        print("Enter only Number")
                case _:
                    print("Wrong command")
        else:
            print("No Record found")
    def delete(self):
        Student_En_No = int(input("Enter Student En_No: "))
        checkdata = self.__check_en_no__(Student_En_No)
        if checkdata["status"]:
            userinput = input("Are you sure y/n:")
            if userinput == "y":
                self.studentsdata.pop(checkdata["index"])
                print("Record deleted")
            else:
                print("Record not deleted")
        else:
            print("No Record found")

# index 0 = En_no, index 1 = Firstname, index 2 = Lastname, index 3 = Phone no
# studentdata = [
#                0 [ En_no , firstname , lastname , phone_no ]
#                1 [ En_no , firstname , lastname , phone_no ] 
#                      0         1           2          3       ]

COM_SEM_3 = DatabaseMethod([])

while 1:
    userinput = input("Enter your command: ")
    if userinput == "add":
        try:
            En_no = int(input("Enter Student Enrollment Number: "))
            Student_F_name = input("Enter Student Firstname: ")
            Student_L_name = input("Enter Student Lastname: ")
            Student_Phone_no = int(input("Enter Student Phone Number: "))
            if En_no and Student_F_name and Student_L_name and Student_Phone_no:
                if COM_SEM_3.Check_En_no(En_no) != True:
                    COM_SEM_3.add([En_no,Student_F_name,Student_L_name,Student_Phone_no])
                    print("Record added successfully")
                else:
                    print("Enrollment already exists")
            else:
                print("fill all input field")
        except:
            print("Enter only Number in En_no field and Phone No field")
    elif userinput == "show all":
        COM_SEM_3.printdata()
    elif userinput == "find":
        filtercommand = input("Enter En_no or Fname or Lname or Phone No: ")
        COM_SEM_3.find(filtercommand)
    elif userinput == "update":
        COM_SEM_3.update()
    elif userinput == "delete":
        COM_SEM_3.delete()
    # elif userinput == "clear":
    #     os.system("cls")
    else:
        print("Wrong command")
    print("------------------------------------------------")