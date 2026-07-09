studentNames = []
studentMarks = []
def addStudentAndMarks():
    # studentRange = int(input("enter how many student name you want to enter = "))
    global studentNames, studentMarks # both list become global 
    # for i in range (0, studentRange):
    #     print(f"{i+1} Enter Student Name : ")
    #     studentNames.append(input())
    #     print(f"{i+1} Enter Student Marks : ")
    #     studentMarks.append(int(input().strip()))
    i = 0
    print(f"Press 'E' to Exit and 'C' to Continue : ")
    responce = str(input())
    if responce == "E":
        pass
    else:
        while True:

            while True:
                print(f"{i+1} Enter Student Name : ")
                Student_Name = str(input())
                if Student_Name.isalpha():
                    print("DID worked")
                    studentNames.append(Student_Name)
                    break
                else:
                    print("Invalid Input !. Try again")
                    return

                    

            print(f"{i+1} Enter Student Marks : ")
            Studnet_Marks = input()
            while True:
                if Studnet_Marks.isdigit():
                    studentMarks.append(Studnet_Marks)
                    break
                else:
                    print("Invalid Input !. Try again")
                    return
        
            i += 1



# Displaying students
def display():
    for i in range(len(studentNames)):
        print(f"{studentNames[i]} : {studentMarks[i]}")
    
# Highest Marks
def highest_Marks():
    


while True:
    print("\nMenu:")
    print(" 1. Add Student")
    print(" 2. Display Students")
    print(" 3. Highest Marks")
    print(" 4. Lowest Marks")
    print(" 5. Average Marks")
    print(" 6. Exit")
    choice = input("Enter your choice:  ")

    match choice:
        case '1' | 'Add Student':
            addStudentAndMarks()
        case '2' | 'Display Students':
            display()