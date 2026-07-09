studentNames = []
studentMarks = []
# Add student function:
def addStudentAndMarks():
    studentRange = int(input("enter how many student name you want to enter = "))
    global studentNames, studentMarks # both list become global 
    for i in range (0, studentRange):
        print(f"{i+1} Enter Student Name : ")
        studentNames.append(input())
        print(f"{i+1} Enter Student Marks : ")
        studentMarks.append(int(input().strip()))

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
        case 'add student':
            addStudentAndMarks()
        
        case 'display student':
            print(studentNames)
            print(studentMarks)
        
        case 'highest marks':
            print(max(studentMarks))

        case 'lowest marks':
            print(min(studentMarks))

        case 'average marks':
            print((sum(studentMarks)/len(studentMarks)))
        
        case 'exit':
            break

        case _:
            print("invalid@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@@@@")
