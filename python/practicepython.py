# HELLO

# mystring = "hello"
# myfloat = 10.0
# myint = 20

# if mystring == "hello":
#     print("String %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print ("Float %f" % myfloat)
# if isinstance(myint, int) and myint == 20:
#     print ("integer: %d" % myint)

# mylist = []
# mylist.append(1)
# mylist.append("Hello World")
# mylist.append(12.0)
# mylist.append({1,2,3})
# for x in mylist:
#     print(x)

# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# strings = []
# strings.append("hello")
# strings.append("world")
# names = ["Eric","John","Jessica"]

# second_name = names[1]

# print(numbers); print(strings); print("Second name: %s" % second_name)

# num1 = [2,4,6,8]
# num2 = [1,3,5,7]
# print(num1 + num2)
# print([1,2,3]*3)

# x = 1
# y = 2

# x_list = [x]*10
# y_list = [y]*10
# big_list = (x_list + y_list) *10
# print(big_list)

# print("%.4f" % 3.1415926) 
# print("%X %x" % (78, 78))

# # START
# s = "Stroll happen ahome!"
# # Length should be 20
# print("Length of s = %d" % len(s))

# # First occurrence of "a" should be at index 8
# print("The first occurrence of the letter a = %d" % s.index("a"))

# # Number of a's should be 2
# print("a occurs %d times" % s.count("a"))

# # Slicing the string into bits
# print("The first five characters are '%s'" % s[:5]) # Start to 5
# print("The next five characters are '%s'" % s[5:10]) # 5 to 10
# print("The thirteenth character is '%s'" % s[12]) # Just number 12
# print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
# print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# # Convert everything to uppercase
# print("String in uppercase: %s" % s.upper())

# # Convert everything to lowercase
# print("String in lowercase: %s" % s.lower())

# # Check how a string starts
# if s.startswith("Str"):
#     print("String starts with 'Str'. Good!")

# # Check how a string ends
# if s.endswith("ome!"):
#     print("String ends with 'ome!'. Good!")

# # Split the string into three separate strings,
# # each containing only a word
# print("Split the words of the string: %s" % s.split(" "))

# # FINISH

# if 'bob' in ['joe','bob','jimmy']:
#     print("ok")

# number = 20
# second_number = 0
# first_array = [1,2,3]
# second_array = [1,2]

# if number > 15:
#     print("1")
# if first_array:
#     print("2")
# if len(second_array) == 2:
#     print("3")
# if len(first_array) +len(second_array) ==5:
#     print("4")
# if first_array and first_array[0] == 1:
#     print("5")
# if not second_number:
#     print("6")

# for x in range(10):
#     print(x)
# else:
#     print('bob')

# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]

# # your code goes here
# for number in numbers:
#     if number == 237: 
#         break
#     if number%2 == 0:
#         print(number)

# else:
#     print('')

# # Modify this function to return a list of strings as defined above
# def list_benefits():
#     return ["more organised code", "more readable code", "easier code reuse", "allowed programmers to share and connect code together"]

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return "%s is a benefit of functions!" %(benefit)

# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()

# class Vehicle:
#     name = ""
#     kind = ""
#     color = ""
#     value = 0.0
#     def descriptio(self):
#         return "%s is a %s %s worth %s" %(self.name, self.color, self.kind, self.value)

# car1 = Vehicle()
# car1.name = "Fer"
# car1.kind = "convertible"
# car1.color = "red"
# car1.value = "$60,000"

# car2 = Vehicle()
# car2.name = "Jump"
# car2.kind = "van"
# car2.color="blue"
# car2.value="$10,000"

# print(car1.descriptio())
# print(car2.descriptio())

# phonebook = {  
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }  
# # your code goes here
# phonebook["Jake"] = 87384749
# del phonebook["Jill"]
# # testing code
# if "Jake" in phonebook:  
#     print("Jake is listed in the phonebook.")
    
# if "Jill" not in phonebook:      
#     print("Jill is not listed in the phonebook.")

# for person in phonebook:
#     print("%s 's phone number is %d" %(person, phonebook[person]))

# import module1

# module1.texts()

# from module1 import texts

# texts()

# from module1 import *

# texts()

# import re
# find_members = []
# for functo in dir(re):
#     if "find" in functo:
#         find_members.append(functo)
# find_members.sort()
# print(find_members)

def fib():
    a = 1
    b = 1
    while True:
        f = a + b
        a = b
        b = f
        yield f

counter = 0
for n in fib():
    print(n)
    counter += 1
    if counter == 10:
        break