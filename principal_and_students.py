'''cse,ece,mech,eee,principal'''
class cse:
    def students_info_cse(self):
        name = "Vijay"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
        name = "Somesh"
        age = "19"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
        name = "Sai"
        age = "20"
        year = "2nd year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")

class ece:
    def student_info_ece(self):
        name = "Golla"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
        name = "Vivek"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
class mech:
    def student_info_mech(self):
        name = "Harsha"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
        name = "Anil"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
class eee:
    def student_info_eee(self):
        name = "Rithwik"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
        name = "Adil"
        age = "18"
        year = "1st year"
        print("STUDENT_INFO :\n"
              " Name: ", name, "\n",
              "Age: ", age, "\n",
              "Year: ", year, "\n")
class principal(mech,eee,cse,ece):
    pass



obj = principal()
obj.student_info_ece()
obj.student_info_eee()
obj.student_info_mech()
obj.students_info_cse()



