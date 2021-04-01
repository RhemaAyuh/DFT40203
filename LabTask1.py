#RHEMA ANAK AYUH
#20DDT19F1107

#QUESTION 1(a)
range(11)
for i in range(11):
    print("The Square of", i ,"is: ",i*i)
print("Process finished with exit code 0")
print("")

#1(b)

limit=11
number=0
total=0
while number<limit:
    if(number % 2 == 0):
        total = total + number
    number=number+1

print("The total of Even Numbers from 0 to 10 is ", total)


#QUESTION 2


username=input('Please enter your username: ')
password=input('Please enter your password: ')
print(len(password))
if not username.isalpha():
    print("Please use only alphabet characters")
else:
    print("")

if len(password)<5:
    print("Your password need to contain at least 5 characters")

if not password.isdigit():
    print("Your password must in numeric")

else:
    print("")


#QUESTION 3

Carprice=103300
downpayment=int(input("Please enter your downpayment : "))
years=int(input("Please enter your leon period in years : "))

loan_amount=Carprice-downpayment
total_interest=(2.7/100)*loan_amount*years
monthly_installement=(loan_amount+total_interest)//(years*12)
monthly= str(round(monthly_installement, 2))

print("you need to pay",monthly,"as your monthly installment")

