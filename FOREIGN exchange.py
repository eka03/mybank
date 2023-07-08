import mysql.connector
mydb=mysql.connector.connect(user='root', passwd='12345', host='localhost', auth_plugin='mysql_native_password',database="BankDB") 
mycursor=mydb.cursor(buffered=True)

print("*"*110)
print("\n")
acc=input("Enter your account number:- ")
print("*"*110)
email=input("ENTER YOUR MAIL_ID:-")
print("*"*110)
c=input("ENTER THE CURRENCY WHICH U WANT TO CHANGE TO:-")
print("*"*110)
try:
    if c=='indian':
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
            d=a/70
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
except:
    print("invalid optiion")
    print("*"*110)
    print("visit again")
