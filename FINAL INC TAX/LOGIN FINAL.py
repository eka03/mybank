import mysql.connector
mydb=mysql.connector.connect(user='root', passwd='12345', host='localhost', auth_plugin='mysql_native_password',database="data") 
mycursor=mydb.cursor(buffered=True)

def Create1():
     try:
          mycursor.execute('create table info(PASSWRD integer(4),USERNAME varchar(20))') 
          print("\t\t\t\t\t\t\tSO YOU ARE READY TO GO")       
     except:
          print("")

        
def start():
     while True:
          print("="*120)  
          print('1. New Account')
          print()
          print('2. Login To Your Account')
          print()
          print('3. Exit from here...')
          print()          
          print("="*120)  
          n=int(input("\t\t\t\t\t\tSo what's your choice?(1-3):"))
          print()
          if n== 1:
               name=input('Enter a Username=')
               print()
               passwd=int(input('Enter a 4 DIGIT Password/Pin='))
               print()
               a="insert into info(PASSWRD,USERNAME) values (" +  str (passwd) + ",'" + name + "') "
               mycursor.execute(a)
               mydb.commit()
               print()
               print('Your Account is Created Succesfully')
          elif  n==2 :
              name=input('Enter Your Username=')
              print()
              passwd=int(input('Enter Your 4 DIGIT Password/Pin='))
              print()
              mycursor.execute('use data')
              a="select * from info where passwrd='%s' and username='%s'" % (passwd,name) 
              mycursor.execute(a)
              S=mycursor.fetchall()
              for i in S:
                   i=list(i)
                   if i[0]==passwd:
                        print("\t\t\t\t\t\tYou Are Logged In To Your Account.")
                        import CODING4
             
          elif  n==3 :
            print()
            print("\t\t\t\t\t\tTHANK YOU! HAVE A NICE DAY....")
            print()
            print("\t\t\t\t\t\t      Press Enter to EXIT....")
            input()
            break
                        

print("="*120)                   
print("\t\t\t\t\t\t    Hi, Welcome! I'm Mr. Software")
print("")
print("\t\t\t\t\t\tI was created by KARTIKEY & EKAGRA")
print("")
print("\t\t\t\t\t\t\t  of Class-12th  batch (2020-2021)")
print("")
print("\t\t\t\t\t\t   From St. Joseph's Sr. Sec School")
print("="*120)  
g=input("\t\t\t\t\tTo run the software 'PRESS ANY KEY' and 'HIT ENTER'")
try:   
    Create1()
    start()
except:
    print("Try Another Key...")
