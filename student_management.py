import sqlite3
conn=sqlite3.connect("students.db")
cursor=conn.cursor()

def add_students():
    roll_no=int(input("enter your roll number"))
    name=input("enter your name")
    age=int(input("enter your age"))
    cursor.execute("""
        INSERT INTO students VALUES(?,?,?)""",
        (roll_no,name,age)
        )
    conn.commit

    print("Student added sucessfully")

def exit_program():
    conn.close()
    print("Thank you")

def search_students():
    search_roll=int(input("enter the roll no you want to search"))
    cursor.execute(
        "SELECT * FROM students WHERE roll_no=?",
        (search_roll,)    
    )
    rows=cursor.fetchall()
    for row in rows:
        print(row)

def show_all_students():
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

def delete_student():
    delete_roll = int(input("Enter roll number to delete: "))

    cursor.execute("""
        DELETE FROM students
        WHERE roll_no = ?
        """, (delete_roll,))

    conn.commit()

    print("Student deleted successfully!")



while(True):
    print("\n===== Student Management System =====")
    print("1.add students")
    print("2.search student")
    print("3.show all students")
    print("4.delete student")
    print("5.Exit")

    choice=int(input("enter your choice"))

    if(choice==1):
        add_students()
    elif(choice==2):
        search_students()
    elif choice==3:
         show_all_students()
    elif choice==4:
        delete_student()

    
    elif(choice==5):
        exit_program()
        break


    
