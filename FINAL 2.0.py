import mysql.connector
mydb=mysql.connector.connect(user='root', passwd='12345', host='localhost', auth_plugin='mysql_native_password',database="BankDB") 
mycursor=mydb.cursor(buffered=True)


print('1.REGISTER')
print()
print('2.LOGIN')
print()
n=int(input('enter your choice='))
print()
if n== 1:
     name=input('Enter a Username=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     print('USER created succesfully')


print("*"*110)
print("\n")
print("\t\t\t\t\t\t WELCOME TO United BANK 2021")
print("\t\t\t\t\t\t .........................................")
print("")
print("\t\t\t\t\t\t   यूनाइटेड बैंक 2021 मैं आप का स्वागत है!")
print("\t\t\t\t\t\t   ....................................... ")
print("")
print("\t\t\t\t\t\t ST. JOSEPH'S SR. SEC. SCHOOL")
print("\t\t\t\t\t\t The Bank that begins with 'U'")
def Menu():
    print("="*100)                                                                      
    print("\t\t\t\t\t\tMAIN MENU")
    print("="*100)
    print("\t\t\t\t\t 1.Insert Record/Records")
    print("\t\t\t\t\t ............................................")
    print("\t\t\t\t\t 2.Display Records")
    print("\t\t\t\t\t ...............................")
    print("\t\t\t\t\t 3.Search Record Details ")
    print("\t\t\t\t\t ...........................................")
    print("\t\t\t\t\t 4.Update Record")
    print("\t\t\t\t\t .............................")
    print("\t\t\t\t\t 5.Delete Record")
    print("\t\t\t\t\t ............................")
    print("\t\t\t\t\t 6.Transactions Debit")
    print("\t\t\t\t\t ....................................")
    print("\t\t\t\t\t 7.Transactions Credit")
    print("\t\t\t\t\t .....................................")
    print("\t\t\t\t\t 8.foreign exchange")
    print("\t\t\t\t\t .....................................")
    print("\t\t\t\t\t 9.Exit")
    print("\t\t\t\t\t ..........")
    print("="*100)
    
def Create(): 
    try:
        mycursor.execute('create table bank(passwrd integer(4),username varchar(20),ACCNO varchar(10),NAME varchar(20),DESIGNATION varchar(30),MOBILE_NO varchar(10),EMAIL varchar(30),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(20),SALARY integer(15))') 
        print("Table Created")       
    except: 
        print("Table Exist") 

def Insert():
    while True:
        x=int(input("Enter num of records:"))
        for i in range(1,x+1):
            print("\t\t\t\tEnter record of person",i,"")

            while True:                
                Acc=input("Enter the Employee's Number:-")
                x= len(Acc)                         
                if x!=5:
                    print("Employee Number should of 5 digit only....")
                    pass
                elif x==5:
                    print("Employee Numver Saved....")
                    break
            Name=input("Enter Employee's Name:-")
            Desig=input("Enter Employee's Designation:-")
            while True:                
                Mob=input("Enter Employee's Mobile Number:-")
                z= len(Mob)
                if z!=10:
                    print("Employee's Mobile Number should of 10 digit only....")
                    pass                        
                else:
                    break
            while True:
                email=input("Enter Employee's Email:-")
                if len(email)<=30 and email[-10:]=='@gmail.com' or email[-10:]=='@yahoo.com':
                    break

                elif len(email)>30 or len(email)<=30 and email[-10:]!='@gmail.com' or email[-10:]!='@yahoo.com':
                    print("Employee's Email should of 30 characters and should contain '@gmail.com' or '@yahoo.com' only....")
                    pass        
              
                
            Add=input("Enter Employee's Address:-") 
            City=input("Enter Employee's City:-") 
            Country=input("Enter Employee's Country:-")
            Sal=input("Enter Employee's Monthly Salary:-")          
            Rec=[name,passwd,Acc,Name.upper(),Desig.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Sal] 
            Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(Cmd,Rec) 
            mydb.commit()
            
        ch=input("\t\t\t\tPress N/n to Exit this Option....") 
        if ch=='N' or ch=='n': 
            break 

        
def MenuSort():
    print("\t\t\t\t\t1.Sort as per Account Number")
    print("\t\t\t\t\t2.Sort as per Customer Name")
    print("\t\t\t\t\t3.Sort as per Customer Balance")
    print("\t\t\t\t\t             4.Back") 





def DispSortAcc():
    try: 
        cmd="select * from BANK order by ACCNO" 
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","DESIGNATION","MOBILE_NO","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","SALARY"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist") 
        

def DispSortName(): #Function to Display records as per ascending order of Name
    try:
        cmd="select * from BANK order by NAME"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","DESIGNATION","MOBILE_NO","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","SALARY"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist") 
def DispSortBal(): #Function to Display records as per ascending order of Balance
    try:
        cmd="select * from BANK order by BALANCE"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","DESIGNATION","MOBILE_NO","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","SALARY"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist") 

def DispSearchAcc():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the accountno to be searched")
        x= len(ch)
        if x!=5:
            print("Employee Number should of 5 digit only....")
            pass
        
        for i in S:
            if i[0]==ch:
                print("="*125)
                F="%15s %15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ACCNO","NAME","DESIGNATION","MOBILE_NO","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","SALARY"))
                print("="*125)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
        else:
            print("Record Not found")

    except:
        print("Table doesn't exist") 


def Update(): 
    #try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name")
                    i[1]=i[1].upper()
                ch=input("Change Designation(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Designation")
                    i[2]=i[2].upper()                    
                ch=input("Change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter Mobile")
                ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter email")
                    i[4]=i[4].upper()
                ch=input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter Address")
                    i[5]=i[5].upper()
                ch=input("Change city(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter City")
                    i[6]=i[6].upper()
                ch=input("Change Country(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=input("Enter country")
                    i[7]=i[7].upper()
                ch=input("Change SALARY(Y/N)")
                if ch=='y' or ch=='Y':
                    i[8]=float(input("Enter SALARY"))
                cmd="UPDATE BANK SET NAME=%s,DESIGNATION=%s,MOBILE_NO=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,SALARY=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
            else:
                print("Record not found")
    #except:
        #print("No such table") 


def Delete(): #Function to delete the details of a customer
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Deleted")
                break
        else:
            print("Record not found")
    except:
        print("No such Table") 


def Debit(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc=input("Enter the account no from which the money is to be debited")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("Enter the amount to be withdrawn"))
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE BANK SET SALARY=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("Amount Debited")
                    break
                else:
                    print("There must be min balance of Rs 5000")
                    break
        else:
            print("Record Not found")
    except:
        print("Table Doesn't exist") 


def Credit():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        acc=input("Enter the account no from which the money is to be debited")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("Enter the amount to be credited"))
                i[7]+=Amt
                cmd="UPDATE BANK SET SALARY=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Credited")
                break
        else:
            print("Record Not found")
    except:
        print("Table Doesn't exist") 

def fe():
    import mysql.connector
    mydb=mysql.connector.connect(user='root', passwd='12345', host='localhost', auth_plugin='mysql_native_password',database="BankDB") 
    mycursor=mydb.cursor(buffered=True)

    print("*"*110)
    print("\n")
    while True:
        Acc=input("Enter the Employee's Number:-")
        x= len(Acc)                         
        if x!=5:
            print("Employee Number should of 5 digit only....")
            pass
        elif x==5:
            print(" DON'T DISTURB WHILE PROCESSING")
            break
    while True:
        email=input("Enter Employee's Email:-")
        if len(email)<=30 and email[-10:]=='@gmail.com' or email[-10:]=='@yahoo.com':
            break

        elif len(email)>30 or len(email)<=30 and email[-10:]!='@gmail.com' or email[-10:]!='@yahoo.com':
            print("Employee's Email should of 30 characters and should contain '@gmail.com' or '@yahoo.com' only....")
            print("DON'T DISTURB WHILE PROCESSING")
            pass
    while True:
        Mob=input("Enter your Mobile Number:-")
        z= len(Mob)
        if z!=10:
            print("Mobile Number should be of 10 digit only....")
            pass                        
        elif z==10:
            print("DON'T DISTURB WHILE PROCESSING")
            break
    print(" WE")
    print(" \tSUPPORT")
    print(" \t\tONLY ")
    print(" \t\t\tGIVEN ")
    print(" \t\t\t\tCURRENCY")
    print(" \t\t\t\t\tFOR")
    print(" \t\t\t\t\t\tEXCHANGE ")
    print(" \t\t\t\t\t\t\tPROCESS")
    c=input("ENTER THE CURRENCY WHICH U HAVE:-")
    print("*"*110)
    if c=='indian' or c=='INDIAN':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=a/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD) is=",q)
            print("*"*110)
        elif ch==2:
            d=a/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=a/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=a/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=a/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=a/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=a/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=a/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=a/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=a/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)
    elif c=='dollar' or c=='DOLLAR':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=a*74.01
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*74.01)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*74.01)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*74.01)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*74.01)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*74.01)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*74.01)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*74.01)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*74.01)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*74.01)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)
    elif c=='euro' or c=='EURO':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=a*90.41
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*90.41)/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD)is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*90.41)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*90.41)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*90.41)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*90.41)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*90.41)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*90.41)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*90.41)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*90.41)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)
    elif c=='ruble' or c=='RUBLE':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=a*0.98
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*0.98)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*0.98)/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*0.98)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*0.98)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*0.98)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*0.98)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*0.98)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*0.98)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*0.98)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)


    elif c=='rufiyaa' or c=='RUFIYAA':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*4.79)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*4.79)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:                                 
            d=(a*4.79)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*4.79)/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD) is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*4.79)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*4.79)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*4.79)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*4.79)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*4.79)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*4.79)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)


    elif c=='riyal' or c=='RIYAL':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*19.70)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*19.70)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*19.70)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*19.70)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*19.70)/74.01
            q=round(d,0)
            print("The amount in UNITED STATES DOLLAR(USD) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*19.70)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*19.70)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*19.70)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*19.70)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*19.70)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)


    elif c=='dinar' or c=='DINAR':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tunited states dollar(usd)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*241.45)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*241.45)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*241.45)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*241.45)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*241.45)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*241.45)/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD)is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*241.45)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*241.45)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*241.45)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*241.45)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)


    elif c=='pound' or c=='POUND':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*98.59)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*98.59)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*98.59)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*98.59)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*98.59)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*98.59)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*98.59)/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*98.59)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*98.59)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*98.59)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)


    elif c=='shilling' or c=='SHILLING':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUnited States dollar(USD)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*0.020)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*0.020)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*0.020)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*0.020)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*0.020)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*0.020)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*0.020)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*0.020)/74.01
            q=round(d,0)
            print("The amount in United States dollar(USD) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*0.020)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*0.020)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)


    elif c=='franc' or c=='FRANC':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tUNITED STATES DOLLAR(USD)")
        print("*"*110)
        print("10.\t\t\t\tBangladeshi taka(BDT)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*83.43)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*83.43)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=(a*83.43)/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*83.43)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*83.43)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*83.43)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*83.43)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*83.43)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*83.43)/74.01
            q=round(d,0)
            print("The amount in UNITED STATES DOLLAR(USD) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*83.43)/0.8702
            q=round(d,0)
            print("The amount in Bangladeshi taka(BDT) is=",q)
            print("*"*110)
    
    elif c=='taka' or c=='TAKA':
        a=int(input("Enter the amount you want to exchange:-"))
        print("Select the currency in which you want to exchange :-")
        print("*"*110)
        print("1.\t\t\t\tINDIAN RUPEES(INR)")
        print("*"*110)
        print("2.\t\t\t\tEuropean euro(EUR)")
        print("*"*110)
        print("3.\t\t\t\tRussian Ruble(RUB)")
        print("*"*110)
        print("4.\t\t\t\tMaldivian Rufiyaa(MVR)")
        print("*"*110)
        print("5.\t\t\t\tSaudi Arabian riyal(SAR)")
        print("*"*110)
        print("6.\t\t\t\tQuwaiti dinar(KWD)")
        print("*"*110)
        print("7.\t\t\t\tBritish Pound(GBP)")
        print("*"*110)
        print("8.\t\t\t\tUgandan shilling(UGX)")
        print("*"*110)
        print("9.\t\t\t\tSwiss franc(CHF)")
        print("*"*110)
        print("10.\t\t\t\tUNITED STATES DOLLAR(USD)")
        print("*"*110)
        ch=int(input("enter your choice:-"))
        print("*"*110)
        if ch==1:
            d=(a*0.8702)
            q=round(d,0)
            print("The amount in INDIAN RUPEES(INR) is=",q)
            print("*"*110)
        elif ch==2:
            d=(a*0.8702)/90.41
            q=round(d,0)
            print("The amount in Europian Euro(EUR) is=",q)
            print("*"*110)
        elif ch==3:
            d=a/0.98
            q=round(d,0)
            print("The amount in Russian Ruble(RUB) is=",q)
            print("*"*110)
        elif ch==4:
            d=(a*0.8702)/4.79
            q=round(d,0)
            print("The amount in Maldivian Rufiyaa(MVR)  is=",q)
            print("*"*110)
        elif ch==5:
            d=(a*0.8702)/19.70
            q=round(d,0)
            print("The amount in Saudi Arabian Riyal(SAR) is=",q)
            print("*"*110)
        elif ch==6:
            d=(a*0.8702)/241.45
            q=round(d,0)
            print("The amount in Kuwaiti Dinar(KWD) is=",q)
            print("*"*110)
        elif ch==7:
            d=(a*0.8702)/98.59
            q=round(d,0)
            print("The amount in British Pound(GBP) is=",q)
            print("*"*110)
        elif ch==8:
            d=(a*0.8702)/0.020
            q=round(d,0)
            print("The amount in Ugandan Shilling(UGX) is=",q)
            print("*"*110)
        elif ch==9:
            d=(a*0.8702)/83.43
            q=round(d,0)
            print("The amount in Swiss franc(CHF) is=",q)
            print("*"*110)
        elif ch==10:
            d=(a*0.8702)/74.01
            q=round(d,0)
            print("The amount in UNITED STATES DOLLAR(USD) is=",q)
            print("*"*110)
    else:
        print("WRONG CHOICE ENTERED FROM THE USER")
        print("WE DON'T HAVE THE CURRENCY WHUCH U WANT TO EXCHANGE")
        print("*"*110)
    
while True:
    Menu()
    ch=int(input("\t\t\t\t\t   So what's your choice?(1-9):"))
    if ch==1:
        while True:
            print("Enter 1 to create Database")
            print("Enter 2 to insert records")
            print("Enter 3 to EXIT from this Option 1")
            q=int(input("What's your choice:"))
            if q==1:
                Create()
            elif q==2:
                Insert()
            elif q==3:
                print("Exiting from Option 1")
                break
    elif ch==2:
        while True:
            MenuSort()
            ch1=input("Enter choice a/b/c/d")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch==3:
        DispSearchAcc()
    elif ch==4:
        Update()
    elif ch==5:
        Delete()
    elif ch==6:
        Debit()
    elif ch==7:
        Credit()
    elif ch==8:
        fe()
    elif ch==9:
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered")
    
