class abhi:
    def __init__(obj,name,rollnumber):
        obj.name=name;
        obj.rollnumber=rollnumber;
    def student_marks_detalis(obj):
        obj.mark1=int(input("Enter the marks 1"))
        obj.mark2=int(input("Enter the marks 2"))
        obj.mark3=int(input("Enter the marks 3"))
        obj.mark4=int(input("Enter the marks 4"))
        obj.mark5=int(input("Enter the marks 5"))
        
    def student_info(obj):
        print("Student name",obj.name);
        print("student rolol number",obj.rollnumber);
obj=abhi("Abhi",19)
obj.student_marks_detalis()
obj.student_info()
