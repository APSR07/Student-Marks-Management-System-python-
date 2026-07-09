studentNames = []
studentMarks = []
# Add student function:
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

def display():
    for i in range(len(studentNames)):
        print(f"{studentNames[i]} : {studentMarks[i]}")
    
# Highest Marks
def highest_Marks():
    high = 0
    max = int(studentMarks[0])
    for i in range(len(studentMarks)):
        cur_val = int(studentMarks[i])            # so if current is highest then it will stay high, if not then we update it
        if cur_val > max:
            max = cur_val
            high = i
    print(f"Hightest Marks is : {studentMarks[high]} by {studentNames[high]}.")
            

def lowest():
    high = 0
    max = int(studentMarks[0])
    for i in range(len(studentMarks)):
        cur_val = int(studentMarks[i])            
        if cur_val < max:           # copy and pasted same thing just change the symbol, > to <
            max = cur_val 
            high = i
    print(f"Hightest Marks is : {studentMarks[high]} by {studentNames[high]}.")

def average():
    sum = 0
    count = 0
    for i in range(len(studentMarks)):
        sum += int(studentMarks[i])
        count = int(studentMarks[-1])

    print(f"The Average of Students are : {sum / count}")


def close():
    raise SystemExit

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
            display()
        case '3' | 'Highest Marks' | 'Highest':
            highest_Marks()
        case '4' | 'Lowest Marks' | 'Lowest':
            lowest()
        case '5' | 'Average' | 'Average Marks':
            average()
        case '6' | 'Exit':
            close()
        case _:
            print("invalid@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@@@@")
