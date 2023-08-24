
from prettytable import PrettyTable
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tavish99",database="p1")
jarvis=mydb.cursor()

def ta1():
    l1=[]
    sql="select * from attendance1"
    jarvis.execute(sql)
    m1=jarvis.fetchall()
    for i in m1:
        l1.append(i[1])
    print("Good Morning!","\U0001F971")
    month=int(input("Enter the month code here:"))
    l2=[1,2,3,4,5,6,7,8,9,10,12]
    if month in l2:
        date=input("Enter the date here :")
        if date not in l1:
            vql="insert into att values(%s)"
            vata=(date,)
            jarvis.execute(vql,vata)
            print("Enter P for Present and A for absent. Enter AB for half day")
            a3="SELECT * from students"
            jarvis.execute(a3)
            m2=jarvis.fetchall()
            for i in m2:
                l1.append(date)
                atte=input("Enter the attendace here for "+i[1]+':')
                data=(str(month),date,i[0],i[1],atte)
                sql="insert into attendance1 values(%s,%s,%s,%s,%s)"
                jarvis.execute(sql,data)
                mydb.commit()
            main()
        else:
            print("Entry already entered..")
            main()
    else:
        print("Wrong month code try again later..")
        ta1()

def dism():
    print('''Enter the month for which you want the attendance for using the month code here below:
                    1.Jan
                    2.Feb
                    3.March
                    4.Apr
                    5.May
                    6.June
                    7.July
                    8.August
                    9.Sep
                    10.Oct
                    11.Nov
                    12.Dec''')
    monthchoice=int(input("Enter the month code here for report:"))
    monthlist=[1,2,3,4,5,6,7,8,9,10,11,12]
    x1=PrettyTable()
    x1.field_names=["Date","Student Roll",'Student Name','Attendance']
    if monthchoice in monthlist:
        sql="SELECT * from attendance1 where MONTH=%s"
        data=(monthchoice,)
        jarvis.execute(sql,data)
        m1=jarvis.fetchall()    
        for i in m1:
            x1.add_row([i[1],i[2],i[3],i[4]])
        print(x1)
        print()
        main()
    else:
        print("Invalid month code entered...")
        main()

        
def dism1():
    z1=[]
    sql2="select * from students"
    jarvis.execute(sql2)
    m2=jarvis.fetchall()
    for i in m2:
        z1.append(i[0])
    a1=int(input("Enter student roll no to continue:"))
    x1=PrettyTable()
    x1.field_names=['Date','Student Name','Attendance']
    if a1 in z1:
        z2=[]
        sql3="select * from attendance1"
        jarvis.execute(sql3)
        m3=jarvis.fetchall()
        for i in m3:
            z2.append(i[2])
        if a1 in z2:
            sql="select * from attendance1 where SROLL=%s"
            data=(a1,)
            jarvis.execute(sql,data)
            m1=jarvis.fetchall()
            for i in m1:
                x1.add_row([i[1],i[3],i[4]])
            print(x1)
        else:
            print("\n\nRecord is Empty....\n\n")
    else:
        print("\n\nInvalid Roll No\n\n")


def per():
    x1=PrettyTable()
    x1.field_names=['Student Roll no','Student Name','Total Days','Total Days Present','Percentage of Att.']
    s=0
    s1=0
    l1=[]
    sql3="select * from students"
    jarvis.execute(sql3)
    m3=jarvis.fetchall()
    for i in m3:
        l1.append(i[0])
    a1=int(input("Enter the student roll no to continue:"))
    if a1 in l1:
        sql="select * from att"
        jarvis.execute(sql)
        m1=jarvis.fetchall()
        for i in m1:
            s=s+1
        sql2="select * from attendance1 where PA=%s and SROLL=%s"
        data=('P',a1)
        jarvis.execute(sql2,data)
        m2=jarvis.fetchall()
        for  i in m2:
            s1=s1+1
        z1=s1/s*100
        x1.add_row([a1,i[3],s,s1,z1])
        print(x1)
        main()
    else:
        print()
        print("Invalid Student Roll no...")
        print()

    
def per1():
    print("List of students who have passed is:")
    x1=PrettyTable()
    x1.field_names=["Student Roll","Student Name","Percentage"+'%']
    vql="select * from att"
    jarvis.execute(vql)
    v4=jarvis.fetchall()
    s=0
    for i in v4:
        s=s+1
    cql="select * from students"
    jarvis.execute(cql)
    c1=jarvis.fetchall()
    for j in c1:
        s1=0
        sql="select * from attendance1 where PA=%s and SROLL=%s"
        data=('P',j[0])
        jarvis.execute(sql,data)
        m3=jarvis.fetchall()
        for i in m3:
            s1=s1+1
        z1=s1/s*100
        if z1>75:
            x1.add_row([i[2],i[3],z1])
        else:
            pass
    print(x1)
    main()

    
def delete():
    z1=[]
    sql3="select * from students"
    jarvis.execute(sql3)
    m1=jarvis.fetchall()
    for i in m1:
        z1.append(i[0])
    a1=int(input("Enter the SROLL to delete:"))
    if a1 in z1:
        z1.remove(a1)
        b1="delete from students where SROLL=%s"
        data=(a1,)
        jarvis.execute(b1,data)
        mydb.commit()
        b2="delete from attendance1 where SROLL=%s"
        jarvis.execute(b2,data)
        mydb.commit()
        print("Successfully deleted....")
        main()
    else:
        print("This entry does not exist....")
        main()


def order_by():
    z1=[]
    sql="SELECT * from STUDENTS ORDER BY SROLL"
    jarvis.execute(sql)
    m1=jarvis.fetchall()
    for i in m1:
        z1.append(i)
    sql1="truncate students"
    jarvis.execute(sql1)
    sql2="insert into students values(%s,%s)"
    jarvis.executemany(sql2,z1)
    mydb.commit()
    
def addn():
    w1=int(input("Enter the number of students you want to add:"))
    for i in range(w1):  
        z1=[]
        sql3="select * from students"
        jarvis.execute(sql3)
        m1=jarvis.fetchall()
        for i in m1:
            z1.append(i[0])
        a1=int(input("Enter the student roll no to add:"))
        if a1 not in z1:
            a2=input("Enter the student name to add:")
            sql="insert into students values(%s,%s)"
            data=(a1,a2)
            jarvis.execute(sql,data)
            mydb.commit()
            print()
            print("Student added ........")
            print()
            order_by()
        else:
            print("Roll No already exists")
            main()

            
def updaten():
    print(''' U P D A T E    M E N U

        1.Name
            
        2.Attendance for a day of a student.

        3.Exit

            ''')
    a1=int(input("Enter choice here:"))
    z1=[]
    sql3="select * from students"
    jarvis.execute(sql3) 
    m1=jarvis.fetchall()
    for i in m1:
        z1.append(i[0])
    if a1==1:
        a1=int(input("Enter the roll no of the student here:"))
        if a1 in z1:
            a2=input("Enter the new name of the student here:")
            sql="update students set SNAME=%s where SROLL=%s"
            data=(a2,a1)
            jarvis.execute(sql,data)
            mydb.commit()
            sql2="update attendance1 set sname=%s where sroll=%s"
            data=(a2,a1)
            jarvis.execute(sql2,data)
            mydb.commit()
            print("Successfully Updated.")
            print("\U0001F44D")
            main()
        else:
            print("record does not exist...")
            main()
    elif a1==2:
        a1=int(input("Enter the roll no of the student here:"))
        if a1 in z1:
            a2=input("Enter the date here:")
            l2=[]
            sql="select * from attendance1"
            jarvis.execute(sql)
            m2=jarvis.fetchall()
            for i in m2:
                l2.append(i[1])
            if a2 in l2:
                w1=input("Enter the change")
                sql2="update attendance1 set pa=%s where sroll=%s and date=%s"
                data=(w1,a1,a2)
                jarvis.execute(sql2,data)
                mydb.commit()
                print("Successfully Updated.")
                print("\U0001F44D")
                print()
            else:
                print()
                print("Record Empty")
        else:
            print()
            print("Invalid Roll No..")
    elif a1==3:
        print()
        print("Exiting")
        main()

def display():
    print(''' D I S P L A Y   M E N U

        1.Students Table
        
        2.Attendance Table
        
        3.Particular Date
        
        4.Absentees of a Particular Date

        5.Exit
        ''')
    a1=int(input("Enter the choice here:"))
    if a1==1:
        x1=PrettyTable()
        x1.field_names=['Student Roll','Student Name']
        sql1="select * from students"
        jarvis.execute(sql1)
        m1=jarvis.fetchall()
        for i in m1:
            x1.add_row([i[0],i[1]])
        print(x1)
    elif a1==2:
        x2=PrettyTable()
        x2.field_names=['Month Code','Date','Student Roll','Student Name','Attendance']
        sql2="select * from attendance1"
        jarvis.execute(sql2)
        m2=jarvis.fetchall()
        for i in m2:
            x2.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(x2)
    elif a1==3:
        w3=input("Enter the date here:")
        x3=PrettyTable()
        x3.field_names=['Month Code','Date','Student Roll','Student Name','Attendance']
        sql3="select * from attendance1 where date=%s"
        data=(w3,)
        jarvis.execute(sql3,data)
        m6=jarvis.fetchall()
        for i in m6:
            x3.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(x3)
    elif a1==4:
        x3=input("Enter the date here:")
        x4=PrettyTable()
        x4.field_names=['Month Code','Date','Student Roll','Student Name','Attendance']
        sql4="select * from attendance1 where date=%s and pa=%s"
        data=(x3,'A')
        jarvis.execute(sql4,data)
        m7=jarvis.fetchall()
        for i in m7:
            x4.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(x4)      
    elif a1==5:
        main()
    else:
        display()


    while True:
        print('-'*100)
        print('''
    A T T E N D A N C E   M A N A G E M E N T

1.Take Attendance

2.Bring the report for a month
                
3.Bring the report for a particular student
                
4.Attendance Per of a student
                
5.75 percent criteria
                
6.Delete a Student
                
7.Add a Student
                
8.Update details about a student

9.Display Menu

10.Exit

''')
        print('-'*100)
        a4=int(input("Enter your choice here:"))
        if a4==1:
            ta1()
        elif a4==2:
            dism()
        elif a4==3:
            dism1()
        elif a4==4:
            per()
        elif a4==5:
            per1()
        elif a4==6:
            delete()
        elif a4==7:
            addn()
        elif a4==8:
            updaten()
        elif a4==9:
            display()
        else:
            print()
            print("Exiting the Code....")
            print("\U0001F44B")
            print()
            exit()
            

        
def clear():
    for i in range(25):
        print()

        
def pswd():
    pass1=input("Enter the password here:")
    if pass1=="****":
        print("-----Logging you in...")
        clear()
        main()
    else:
        print("--------Wrong Password-------- ")
        print("\U0001F602")
        clear()
        pswd()
pswd()
