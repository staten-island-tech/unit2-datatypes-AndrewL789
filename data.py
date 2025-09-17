# floats r for numbers with decimal values 

""" x = 3 
y = float(3)
print(x,y)


values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)


print(values[0])
print(values[6])

 """

# strings r a list of letters  to make text

""" x = "this is a thing"
y = x.split()
z= y[0]
print(y)
print(z)

 """

""" #challenge 
blah = input("say something")
z = blah.split()
y =(len(z))
#len is for the length of the list "a"
print(y)

 """


#booleans

""" dow = input("what day is it")
if dow == "Friday":
    print ("correct")
else:
    print("incorrect")
 """
# f strings used b4 a string 

""" x = "test"
print (f"hello {x}") """

""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """


 #challenge 2 off or even
""" number = input("give me a number")


if float(number) % 2 == 0:
    print('even')
else:
    print('odd')
  """
#challenge 3  tip calc
""" bill = input("bill?")

service = input("rate out service?")

if service == ('bad'):
    print("bill")
    final = bill
    print(final)
elif service == ('okay'):
    final = float(bill) * 1.15 
    print(final)
elif service == ('good'):
    final = float(bill) * 1.20
    print(final)
elif service == ('great'):
    final = float(bill) * 1.25
    print(final)
else:
    print("no") """


""" # factor 5 
def factor(x,y):
    if x % y == 0 :
        print(f"{y} is a factor of {x}")
    else:
        print(f"{y} is not a factor of {x}")
 """

#challenge 3 
def factor(x,y):
    for i in range(y-x):
    print(int(x % y) 
    