from random import sample
import io
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*"
password = lower_case + upper_case + numbers + symbols
gen_password = "".join(sample(password, 16))
print(gen_password)
password_for = input("passwd for : ")
file = open("passwords.txt", "a")
text = gen_password + " : " + password_for
file.write(text)
file.write("\n")
file.close()
