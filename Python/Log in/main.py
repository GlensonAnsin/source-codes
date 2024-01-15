username = []
password = []

sign_in = input("Sign in(Y) or Log in(N): ")

if sign_in == "Y":
    print("SIGN IN")
    sign_in_username = input("Username: ")
    sign_in_password = input("Password: ")
    username.append(sign_in_username)
    password.append(sign_in_password)
    print("\nLOG IN")
    currUsername = input("Username: ")
    currPassword = input("Password: ")
    for i in range(len(username)):
        if currUsername == username[i] and currPassword == password[i]:
            print(f"Welcome, {currUsername}")
            break
    else:
        print("Account not found.")

elif sign_in == "N":
    print("LOG IN")
    currUsername = input("Username: ")
    currPassword = input("Password: ")
    for i in range(len(username)):
        if currUsername == username[i] and currPassword == password[i]:
            print(f"Welcome, {currUsername}")
            break
    else:
        print("Account not found.")

else:
    print("Invalid input!")