import random
import string
import pyautogui


pwd = pyautogui.password("Enter a password: ")
chars = string.ascii_letters + string.digits
sample_pwd = 100
attempts = 0
while sample_pwd != pwd:
    sample_pwd = random.choices(chars, k=len(pwd))
    print("<====" + str(sample_pwd) + "===>")
    attempts += 1
    if sample_pwd == list(pwd):
        print("The Password is : " + "".join(sample_pwd))
        break

print(f"The password was cracked in {attempts} attempts.")
