password = "admin123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ")
    if pwd == password:
        print("Login successful")
        break
    attempts -= 1
else:
    print("Account locked")
