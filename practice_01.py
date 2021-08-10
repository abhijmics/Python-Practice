# WAP to find whether the given String is a Palindrome

str1 = input("Enter the String..")

print(str1)

str2 = str1[::-1]

if str1.upper() == str2.upper():
    print("palindrome")
else:
    print("not palindrome")