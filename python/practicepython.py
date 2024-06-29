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

# START
s = "Stroll happen ahome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# FINISH