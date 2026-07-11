studentNames = []
studentMarks = []
# Add student function:
def addStudentAndMarks():
    # studentRange = int(input("enter how many student name you want to enter = "))
     
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
            Studnet_Marks = input().strip()
            while True:
                if Studnet_Marks.isdigit():
                    studentMarks.append(int(Studnet_Marks))
                    break
                else:
                    print("Invalid Input !. Try again")
                    return
        
            i += 1

# Main  function
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
        case '1' | 'Add Student' | 'Add':
            addStudentAndMarks()
        case '2' | 'Display Students' | 'Display':
            print(studentNames, studentMarks)
        case '3' | 'Highest Marks' | 'Highest':
            print("The highest marks = ",max(studentMarks))
        case '4' | 'Lowest Marks' | 'Lowest':
            print("The lowest Marks = ",min(studentMarks))
        case '5' | 'Average' | 'Average Marks':
            average = (sum(studentMarks)//len(studentMarks))
            print(average)
        case '6' | 'Exit':
            break
        case _:
            print("invalid@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@@@@")
