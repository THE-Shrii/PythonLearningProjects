# ✅ 1. Even-Odd Checker
# 🎯 What it does:
# User enters a number → program tells Even or Odd

# num = int(input("Enter a number: "))
#
# if (num % 2 == 0):
#     print("even")
# else:
#     print("odd")






# ✅ 2. Simple Calculator
# 🎯 What it does:
# Performs +, -, *, /

# num1 = int(input("Enter first one: "))
# num2 = int(input("Enter second two: "))
# operation = input("Enter operation(+, -, *, /): ")
#
# if operation == "+":
#     print(num1+num2)
# elif operation == "-":
#     print(num1-num2)
# elif operation == "*":
#     print(num1*num2)
# elif operation == "/":
#     print(num1/num2)
# else:
#     print("Operation not supported")




# ✅ 3. Largest of 3 Numbers
# 🎯 What it does:
# Find biggest number
#
#
# input1 = int(input("Enter 1st no.:"))
# input2 = int(input("Enter 2nd no.:"))
# input3 = int(input("Enter 3rd no.:"))
#
# if input1 > input2 and input1 > input3:
#     print("1st Number is biggest")
# elif input2 > input1 and input2 > input3:
#     print("2nd Number is biggest")
# elif input3 > input1 and input3 > input2:
#     print("3rd Number is biggest")
# else:
#     print("All numbers are equal or two numbers are same")
#


# sor/t
# print("Biggest number is:", max(input1, input2, input3))


#  FOR EQUAL NUMBERS


# input1 = int(input("Enter 1st no.:"))
# input2 = int(input("Enter 2nd no.:"))
# input3 = int(input("Enter 3rd no.:"))
#
# if input1 == input2 == input3:
#     print("All numbers are equal")
#
# elif input1 == input2:
#     print("1st and 2nd numbers are equal")
#
# elif input2 == input3:
#     print("2nd and 3rd numbers are equal")
#
# elif input1 == input3:
#     print("1st and 3rd numbers are equal")
#
# elif input1 > input2 and input1 > input3:
#     print("1st Number is biggest")
#
# elif input2 > input1 and input2 > input3:
#     print("2nd Number is biggest")
#
# else:
#     print("3rd Number is biggest")





# ✅ 4. String Reverser
# 🎯 What it does:
#
# Reverse a word

# word = input("Enter a word: ")
# print(word[::-1])






# ✅ 5. Count Vowels
# 🎯 What it does:
#
# Counts vowels in a word

# s = input("Enter a string:")
# count = 0
#
# for ch in s:
#     if ch.lower() in "aeiou":
#         count += 1
#
# # check AFTER loop
# if count == 0:
#     print("No Vowels found")
# else:
#     print("Vowels:", count)






# ✅ 6. Remove Duplicates (List)
# 🎯 What it does:
#
# Remove duplicate numbers

# l1 = [1,2,2,2,2,4]
# uniquel1 = list(set(l1))
# print(uniquel1)





# ✅ 7. Simple Password Checker
# 🎯 What it does:
#
# Checks if password is strong

# password = input("Enter Your Password:")
#
# if len(password) < 8:
#     print("Too short")
# elif not any(ch.isdigit() for ch in password):
#     print("Add a number")
# elif not any(ch.isupper() for ch in password):
#     print("Add uppercase letter")
# elif not any(ch in "#$&@!*" for ch in password):
#     print("Add special character")
# else:
#     print("Strong password ")





# ✅ 8. Sum of List
# 🎯 What it does:
#
# Find total of numbers

# l1 = [1,2,3]
# l2 = [1,2,3]
#
# print (sum(l1 +l2))



# ✅ 9. Check Palindrome
# 🎯 What it does:
#
# Check same forward/backward
#
# s = input("Enter word: ")
#
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#
# # Explanation:
# # Compare string with reverse




# 🎯 What it does:
#
# Grade system
#
# marks = int(input("Enter marks: "))
#
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")
#
# # Explanation:
# # Multiple conditions using elif