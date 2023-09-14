  Fuctions
def maria(x):
  n=x/3
  return n

y= maria(10)

print(int(y))

Fisrt Project
"""TITLE OF THE PROJECT: My first program"""
print("Hello, world :)") #Here I can wrie whatever

EXAM CODES REVIEW

Discount calculator
Kilometer= float(input("How many kilometers you drive?: "))
Gasoline= float(input("How many litters you used?: "))
Millas= Kilometer/1.6
Galones= Gasoline/3.7
KiolmeterperLiter=Kilometer/Gasoline
MillasperGalon=Millas/Galones
print("Kilometer per liter ",KiolmeterperLiter)
print("Millas per Galon ",MillasperGalon)

Average class
def grades_average():
  print("Hello, what was your grade?")
  grade_1 = input()
  print("what was your grade")
  grade_2 = input()
  print("what was your grade")
  grade_3 = input()
  print("what was your grade")
  y= int(grade_1)+ int(grade_2) +int(grade_3)
  x= y/3
  round (y/3),2

  print("Your average grade is", x)
#STEP 2
grades_average()

Tip Calculator
Foodcheck=float(input("Your bill is total of : "))
Tip= float(input("How mmuch of porcentage of tip in number?"))
TIP=(Tip/100)*Foodcheck
Total=TIP+Foodcheck
print("You total with tip is",Total)
print("Your tip amount is",TIP)
print("You orginial cost od the food is",Foodcheck)


FUNCTIONS
y=f(7)
print(y)
def f(x):
 f_x=x/3-10
return f_x

y=f(9)
print(y)
def f(x)
f_x=-abs(3*x)
return f_x

y=f(6)
print(y)
def f(x):
f_x= (x-2)*2
return f_x
y=f(8)
print(y)

Coding Rush
"""
InstructJUST BECAUSE :D
Instructions: make a code that says you hi and your name, and then
asks you a if you want to say something to your ex and give you the
wordcount.
DRAFT CODE
1. MAKE THE FUNCTION
ask the use his/her/their name
say hi and the name
asks if they want to say something to their ex
give you the wordcount
2. EXECUTE THE FUNCTION
“““
#STEP 1
 def Just_get_over_it():
print( "What is your name?" )
variable = input()
print( "Hello my friend", variable)
print ( "Something you want to say to your ex?")
letter = input()
letter = letter.split()
word count = len(letter)
print( "Your letter wordcount is" ,word_count)
#STEP 2
Just_get_over_it()

EXAM CODES

Easy level
VB=float (input ( "How much its the Vibration Machine?:
"))
Discount=float(input("Whatis the discount in number of the Vibration
Machine?:
"))
Operation=(Discount/100)*VB
TotalVB=VB-Operation
print ( "Your total with the discount is", TotalVB)

Normal level
TM= float(input( "How much is the Temperature Machine?: ") )
TSM= float(input( "How much is the Thermal Shock Manchine?:"))
Operation1= TM+TSM
Operation2=(10/100)*Operation1
TotalD=Operation1-Operation2
print( "Your total of the two machine without a discount is", Operation1)
print( "Your total with a 10 porcent of discount is", TotalD)

Hard Level
T=float (input ( "How much is the Total of both machines? :
"))
TD=float (input( "How much is the Total of the two machines with
discount?:
"))
yen=TD*8.37
ad=TD*.057
yent=T*8.37
adt=T*.057
print ( "Your total of the two machines without a discount in japanese
yen is",yent)
print ( "Your total of the two machines without a discount in american
dollar is",adt)
print( "Your total of the two machines with a discount in japanese yer
is",yen)
print ( "Your total of the two machines with a discount in american
dollar is",ad)
