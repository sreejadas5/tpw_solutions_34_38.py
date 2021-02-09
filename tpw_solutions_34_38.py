
num = int(input("Enter a number: "))
interger = num % 2
if interger > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    
letter = input("Input a letter of the alphabet: ")

if letter in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif letter  == 'y':
	print ("Could be a consonant or vowel")
else:
	print("%s is a consonant." % letter)
  
  numSides=int(input("How many sides in the shape: "))
geometry = {
    3: "The shape is a Triangle.",
    4: "The shape is a Quadrilateral.",
    5: "The shape is a pentagon.",
    6: "The shape is a hexagon.",
    7: "The shape is a heptagon.",
    8: "The shape is a octagon.",
    9: "The shape is a nonagon.",
    10: "The shape is a decagon.",
    
}
if numSides == 3:
  print(geometry[3])
elif numSides == 4:
  print(geometry[4])
elif numSides == 5:
  print(geometry[5])
elif numSides == 6:
  print(geometry[6])
elif numSides == 7:
  print(geometry[7])
elif numSides == 8:
  print(geometry[8])
elif numSides == 9:
  print(geometry[9])
elif numSides == 10:
  print(geometry[10])
elif numSides == 11:
  print("Error, number of sides have to be between 3 and 10. Try again.")
  
  month = input ("Enter a month: ")
days = 31
if month == "April" or month == "June" or month == "Spetemeber" or month == "Novemeber" : days = 30
elif month =="Febuary":
  days = "28 or 29"
print ( month,"has", days, "days in it")
