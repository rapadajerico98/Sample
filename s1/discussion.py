street_address = "Blk 4 Lot 5 Kapanalig st"
barangay = "28"
city = "Caloocan City"
postal_code = "1104"
country = "philippines"

#print(f"i live at {street_address} my barangay is {barangay}, {city}, {postal_code}, {country}")

a = 5
b = 5
c = a + b 

#print(c)

d = c * a

#multipy

data1 = 10 * 7
print(data1)

#division

data2 = 100 / 10
print(data2)


num1 = 2
num2 = 5


#print(f"the total sum is {total_sum}")

#d


#multiplication
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
product = num1 * num2

print("the total product is", product )
"""
#division

#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#quotient = num1 / num2

#print("the total quotient is", quotient)

legal_age = 18

my_age = int(input("Enter your age: "))

if my_age >= 60:
    print("You are now on a senior citizen. ")
elif my_age >= legal_age:
    print("You are a now in a legal age")
else: 
    print("You are not 18 year's old. ")

edad = int(input("Ano ang iyong edad nigga?"))

#Pag 18 pwede na uminom ng alak 
#Pag 21 naman pede na mag drive at uminom ng alak
#kapag below 18 bawal uminom ng alak at mag drive

if edad >= 21:
    print("Pwede na mag drive at uminom ng alak")
elif edad >= 18:
    print("pwede ka ng uminom ng alak")
elif edad <= 17:
    print("kapag below 18 bawal uminom ng alak at mag drive")


grade = int(input("Enter your grade:"))

#pag yung grade is above 90 to 100 is excellent
#pag yung grade is 80 to 89 is very good
#pag 75 to 79 is ok 
#pag below 75 bagsak kang kupal ka1

if grade >= 90 and grade <= 100:
    print("Excellent")
elif grade >= 80 and grade <= 89:
    print("VeryGood")
elif grade >= 75 and grade <= 79:
    print("ok na pwede na")
elif grade > 50 and grade <= 74:
    print("Bagsak kang kupal ka!")
else:
    print("Invalid grade")

#kapag ang pera mo ay  50_000 pataas mayaman 
#kapag ang pera mo ay 30_000 to 49_000 sakto lang
#kapag ang pera mo ay 20_000 to 29_000 mahirap kang kupal ka
#else hampas lupa ka


savings_account = int(input("Enter your savings money: "))
if savings_account >= 50_000:
    print("Mayaman ka!")
elif savings_account >= 30_000 and savings_account <= 49_000:
    print("sakto lang")
elif savings_account >= 20_000 and savings_account <= 29_000:
    print("mahirap kang kupal ka!")
elif savings_account > 0 and savings_account <= 19_000:
    print("wala na finish na ")


