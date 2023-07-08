import mysql.connector
mydb=mysql.connector.connect(user='root', passwd='12345', host='localhost', auth_plugin='mysql_native_password',database="BankDB") 
mycursor=mydb.cursor(buffered=True)
print('*' *117)
print("*"*117)
print("\t\t\t\t\t\t          HELLO!! USER")
print()
print("\t\t\t\t               WELCOME! I M Mr. PYTHON SOFTWARE")
print()
print("\t\t\t\t               I WAS CREATED BY KARTIKEY & EKAGRA ")
print()
print("\t\t\t\t                 OF CLASS-12th  BATCH 2020-2021")
print()
print("\t\t\t\t          OF ST.JOSEPH'S SENIOR SECONDARY SCHOOL")
print()
print("\t\t\t\t\t\t        HERE WE GO  ⬇️")
print()
print("\t\t\t\t\t\t     *\t                     *")
print("\t\t\t\t\t\t     * *\t                   * *")
print("\t\t\t\t\t\t     * * *\t                 * * *")
print("\t\t\t\t\t\t     * * * *\t    * * * *")
print("\t\t\t\t\t\t     * * * * *\t  * * * * *")
print("\t\t\t\t\t\t     * * * * * * *   * * * * * *")
print("\t\t\t\t\t\t     * * * * * * * * * * * * * *")
size = 10
m = (2 * size)-2
for i in range(0, size):
    for j in range(0, m):
        pass
    m=m-1 # decrementing m after each loop
    for j in range(0, i + 1):
        print("*", end=" ")
input()
print("*"*117)
print("*"*117)
print("\t\t\t\t\t\tTHE BANK THAT BEGINS WITH 'U'")
print("\t\t\t\t\t\t...........................................")
print()
print("")
print("\t\t\t\t\t\tWELCOME TO UNITED BANK 2021")
print("\t\t\t\t\t\t.........................................")
print("")
print()
print("\t\t\t\t\t\tयूनाइटेड बैंक 2021 मैं आप का स्वागत है!")
print("\t\t\t\t\t\t...................................... ...")
print(" ")
print()
print("\t\t\t\t\t\t      متحدہ بینک 2021 میں خوش آمدید")
print("\t\t\t\t\t\t      ..............................")
print(" ")
print()
print("\t\t\t\t\tUNITED BANK'S AIM IS TO PROVIDE THEIR CUSTOMERS")
print("\t\t\t\t\t......................................................................")
print()
print("")
print("\t\t\t\t\t      THE BEST SERVICE WITH EVERY WAY POSSIBLE")
print("\t\t\t\t\t      ............................................................")
print()
print("")
print("\t\t\t\t         WE WILL VALUE CUSTOMER'S CONTRIBUTION TO OUR BANK ")
print("\t\t\t\t\t      ............................................................................")
print()
print("")
print("\t\t\t\t\t  FOR LIFTING HIS STANDARD IN THE UPCOMING YEARS")
print("\t\t\t\t\t  .....................................................................")
print()
input()
print("")
print("*"*117)
print("*"*117)
print("")
print("\t\t\t\t\t    Co-Founded By  ➡  KARTIKEY AND EKAGRA")
print("\t\t\t\t\t    .....................................................")
print()
input()
print("*"*117)
print("*"*117)
print()
print("\t\t\t\t\t\tCONTACT US (24/7) ON :-")
print("\t\t\t\t\t\t................................")
print()
print("\t\t\t\t\t       TOLL FREE NO 📞     : -1800987654")
print("\t\t\t\t\t       ............................................")
print()
print("\t\t\t\t\t    EMAIL ID     ✉     :-UB2021@gmail.com")
print("\t\t\t\t\t    .................................................")
print("")
print("\t\t\t\t\tWHATSAPP NO  :-9856321470     OR        9978456321")
print("\t\t\t\t\t..................................................................")
print("")
print("\t\t\t\t    MOBILE NO   📱     :-9658741230        OR        9874545421")
print("\t\t\t\t    ..........................................................................")
print("")
print("*"*117)
print("*"*117)
print("")
print("\t\t\t\t\t\t\t\t\t\t\tTIMINGS:-")
print("\t\t\t\t\t\t\t\t\t\t\t..............")
print("")
print(" \t\t\t\t\t\t\t\tMONDAY-SATURDAY:-9:00 AM-4:00 PM")
print(" \t\t\t\t\t\t\t\t.................................................")
print("")
print("\t\t\t\t\t\t NOTE:- 2ND & 4TH SATURDAY WILL REMAIN CLOSED")
print("\t\t\t\t\t\t ..................................................................")
print("")
print("*"*117)
print("*"*117)
print()
input()
def Menu():                                                                      
    print("\t\t\t\t\t\tMAIN MENU")
    print()
    print("*"*117)
    print("*"*117)
    print("\t\t\t\t\t 1.INTRODUCE RECORD/S DETAILS")
    print("\t\t\t\t\t ..........................................")
    print("\t\t\t\t\t 2.DISPLAYING RECORD/S DETAILS")
    print("\t\t\t\t\t ..........................................")
    print("\t\t\t\t\t 3.EXPLORE RECORD/S DETAILS")
    print("\t\t\t\t\t ......................................")
    print("\t\t\t\t\t 4.UPGRADE RECORD/S DETAILS")
    print("\t\t\t\t\t ......................................")
    print("\t\t\t\t\t 5.DELETE RECORD/S DETAILS")
    print("\t\t\t\t\t .....................................")
    print("\t\t\t\t\t 6.TRANSACTION DEBIT")
    print("\t\t\t\t\t .............................")
    print("\t\t\t\t\t 7.TRANSACTION CREDIT")
    print("\t\t\t\t\t ..............................")
    print("\t\t\t\t\t 8.FOREIGN EXCHANGE PROCESS")
    print("\t\t\t\t\t .......................................")
    print("\t\t\t\t\t 9.EXIT")
    print("\t\t\t\t\t ........")
    print("*"*117)
    print("*"*117)


    
def Create(): 
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(20),DESIGNATION varchar(30),MOBILE_NO varchar(10),EMAIL varchar(30),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(20),SALARY integer(15))') 
        print("\t\t\tTABLE CREATED")
        print("\t\t\t....................")
    except: 
        print("\t\t\tTABLE ALREADY EXISTS")
        print("\t\t\t..............................")

def Insert():
    while True:
        x=int(input("ENTER NUMBER OF RECORDS:"))
        for i in range(1,x+1):
            print("\t\t\t\tEnter record of person",i,"")

            while True:                
                Acc=input("Enter Employee's Number:-")
                x= len(Acc)                         
                if x!=5:
                    print("Employee's Number should be of 5 digit only....")
                    pass
                elif x==5:
                    print("Employee Number Saved....")
                    break
            Name=input("Enter Employee's Name:-")
            Desig=input("Enter Employee's Designation:-")
            while True:                
                Mob=input("Enter Employee's Mobile Number:-")
                z= len(Mob)
                if z!=10:
                    print("Employee's Mobile Number should be of 10 digit only....")
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
            Rec=[Acc,Name.upper(),Desig.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Sal] 
            Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(Cmd,Rec) 
            mydb.commit()
            
        ch=input("\t\t\t\tPress N/n to Exit this Option....") 
        if ch=='N' or ch=='n': 
            break 

def MenuSort():
    print("\t\t\t\t\t1.SORT AS PER CUSTOMER'S ACCOUNT NUMBER")
    print("\t\t\t\t\t2.SORT AS PER CUSTOMER'S ACCOUNT NAME")
    print("\t\t\t\t\t3.SORT AS PER CUSTOMER'S ACCOUNT BALANCE")
    print("\t\t\t\t\t4.BACK FROM THIS OPTION") 

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
        print("TABLE DOESN'T EXISTS") 
        

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
        print("TABLE DOESN'T EXISTS") 
def DispSortBal(): #Function to Display records as per ascending order of Balance
    try:
        cmd="select * from BANK order by SALARY"
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
        print("TABLE DOESN'T EXISTS") 

def DispSearchAcc():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("ENTER THE ACCOUNT NO TO BE SEARCHED:-")
        x= len(ch)
        if x!=5:
            print("EMPLOYEE'S NO SHOULD BE OF 5 DIGIT ONLY....")
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
            print("RECORD NOT FOUND...")

    except:
        print("TABLE DOESN'T EXISTS") 


def Update():
    #try:
        cmd="select * from BANK";
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("ENTER THE ACCOUNT NO WHOSE DETAILS HAS TO BE UPDATED:-")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("CHANGE NAME(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("ENTER NAME:-")
                    i[1]=i[1].upper()
                ch=input("CHANGE DESIGNATION(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("ENTER DESIGNATION:- ")
                    i[2]=i[2].upper()                    
                ch=input("CHANGE MOBILE NO(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("ENTER MOBILE NO:-")
                ch=input("CHANGE EMAIL(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("ENTER EMAIL:-")
                    i[4]=i[4].upper()
                ch=input("CHANGE ADDRESS(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("ENTER ADDRESS:-")
                    i[5]=i[5].upper()
                ch=input("CHANGE CITY(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("ENTER CITY:-")
                    i[6]=i[6].upper()
                ch=input("CHANGE COUNTRY(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=input("ENTER COUNTRY:-")
                    i[7]=i[7].upper()
                ch=input("CHANGE SALARY(Y/N)")
                if ch=='y' or ch=='Y':
                    i[8]=float(input("ENTER SALARY:-"))
                cmd="UPDATE BANK SET NAME=%s,DESIGNATION=%s,MOBILE_NO=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,SALARY=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("ACCOUNT UPDATED....")
                break
            else:
                print("RECORD NOT FOUND....")
    #except:
        #print("No such table") 


def Delete():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("ENTER THE ACCOUNT NO WHOSE DETAILS HAS TO BE DELETED")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("ACCOUNT DELETED....")
                break
        else:
            print("RECORD NOT FOUND...")
    except:
        print("TABLE DOESN'T EXISTS") 


def Debit(): #Function to Withdraw the amount by assuming the min balance of Rs 5000
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc=input("ENTER THE ACCOUNT NO FROM WHICH MONEY HAS TO BE DEBITED:-")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("ENTER THE AMOUNT TO BE WITHDRAWN:-"))
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE BANK SET SALARY=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("AMOUNT DEBITED...........")
                    break
                else:
                    print("FOR DEBIT PROCESS THERE MUST BE A BALANCE OF ATLEAST Rs 5000 IN YOUR ACCOUNT..")
                    break
        else:
            print("RECORD NOT FOUND")
    except:
        print("TABLE DOESN'T EXISTS") 


def Credit():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        acc=input("ENTER THE ACCOUNT NO FROM WHICH IT IS TO BE CREDITED:-")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("ENTER THE AMOUNT TO BE CREDITED:-"))
                i[7]+=Amt
                cmd="UPDATE BANK SET SALARY=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("AMOUNT CREDITED..... ")
                break
        else:
            print("RECORD NOT FOUND")
    except:
        print("TABLE DOESN'T EXISTS") 

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
            print("PROCESSING.................")
            break
    while True:
        email=input("Enter Employee's Email:-")
        if len(email)<=30 and email[-10:]=='@gmail.com' or email[-10:]=='@yahoo.com':
            break

        elif len(email)>30 or len(email)<=30 and email[-10:]!='@gmail.com' or email[-10:]!='@yahoo.com':
            print("Employee's Email should of 30 characters and should contain '@gmail.com' or '@yahoo.com' only....")
            print("PROCESSING...................")
            pass
    while True:
        Mob=input("Enter your Mobile Number:-")
        z= len(Mob)
        if z!=10:
            print("Mobile Number should be of 10 digit only....")
            pass                        
        elif z==10:
            print("PROCESSING...........")
            break
    print(" OUR BANK")
    print(" \tSUPPORT")
    print(" \t\tONLY ")
    print(" \t\t\tGIVEN ")
    print(" \t\t\t\t COUNTRIES")
    print(" \t\t\t\t\tCURRENCY")
    print(" \t\t\t\t\t\tFOR")
    print(" \t\t\t\t\t\t\tEXCHANGE ")
    print(" \t\t\t\t\t\t\t\tPROCESS")
    c=input("\t\t\tENTER THE CURRENCY WHICH YOU HAVE:-")
    print("*"*110)
    if c=='indian' or c=='INDIAN':
        a=int(input("ENTER AMOUNT TO BE EXCHANGED:-"))
        print("SELECT THE CURRENCY IN WHICH YOU WANT TO CHANGE :-")
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
    ch=int(input("\t\t\t\t\t   WHAT'S YOUR CHOICE DEAR(1-9)"))
    if ch==1:
        while True:
            print("\t\t\t\tEnter 1 TO CREATE DATABASE")
            print("\t\t\t\tEnter 2 TO INSERT RECORD/S")
            print("\t\t\t\tEnter 3 TO EXIT FROM OPTION 1 ")
            q=int(input("\t\t\tWHAT'S YOUR CHOICE BETWEEN (1-3):"))
            if q==1:
                Create()
            elif q==2:
                Insert()
            elif q==3:
                print("EXITING FROM OPTION 1")
                break
    elif ch==2:
        while True:
            MenuSort()
            ch1=input("ENTER CHOICE BETWEEN (A/B/C/D)")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("BACK TO THE MAIN MENU")
                break
            else:
                print("INVALID CHOICE ENTERED")
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
        print("EXITING FROM OPTION 9")
        break
    else:
        print("WRONG CHOICE ENTERED DEAR")
        print()
        print("TRY AGAIN")
        print()
        print("THANKS FOR VISITING IN OUR CAMPUS")
    
