#w3c
print("1. Write a Python program to display the current date and time.")

import datetime

x = datetime.datetime.now()
print(x)

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("2. Write a Python program which accepts the radius of a circle from the user and compute the area.")

pi = 3.14
r = float(input("Podaj promień koła:"))
pole = pi * r * r

print("Pole koła jest równe: %.2f" %pole)

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print("3. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.")

name = input("Podaj imię: ")
surname = input("Podaj nazwisko: ")

name_rev_s = name [::-1]
surname_rev_s = surname [::-1]

result = ''
for ch in name_rev_s, surname_rev_s:
   result = result + ch + ' '
print(result[:-1])

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print("4. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.")

seq = input("Podaj ciąg liczb odzielonych przecinkami: ")
list = seq.split(",")
tuple = tuple(list)

print("Tuple: " ,tuple)
print("List: " ,list)

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("5. Write a Python program to accept a filename from the user and print the extension of that.")
fil = input("Podaj pełną nazwę pliku: ")

f_ext = fil.split(".")
print ("Format pliku to: " + repr(f_ext[-1]))

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("6. Write a Python program to display the first and last colors from the following list.")

color_list = ["Red","Green","White" ,"Black"]
print("Pierwszy kolor to:", color_list[0], ", a ostatni kolor to:" , color_list[-1])

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("7. Write a Python program to display the examination schedule. exam_st_date = (11, 12, 2014)")

exam_st_date = (11, 12, 2014)
print( "Egzamin odbędzie się : %i / %i / %i"%exam_st_date)

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("8. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.")

a = int(input("Podaj liczbę: "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("9. Write a Python program to get the volume of a sphere with radius 6")
r = int(input("Podaj promień kuli: "))
pi = 3.14
res = 4/3*(pi*r*r*r)
print("Objętość kuli wyosi: " ,res )

quest = input("Przejść do kolejnego zadania? y / n")
if quest != "y":
    print ('nie to nie ;)')
    import sys
    sys.exit()
else:
    print("ok, lecimy dalej!")    

print ("10. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference")
num = int(input("Podaj liczbę: "))
if num <= 17:
    print("Różnica między podaną liczbą a liczbą 17 to:",17 - num)
elif num > 17:
    for num in num:
        b = a + 17
        if b > num:
         break
        print(num - b)
        
 print("11. Merge two sorted arrays into one - remember to delete duplicates)     
 def merge_arrays(arr1, arr2):
    new = arr1 + arr2
    new.sort()
    output = []
    for x in new:
        if x not in output:
            output.append(x)
    output.sort()
    return output
