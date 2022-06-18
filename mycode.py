
#assignment1(register and login)

#after register valid username and valid password the data store in this file(stage-2 done)
with open('trial.txt', 'r') as f:
    content = f.read()

a = int(input("To login press 0 \nTo Register press 1 \n"))

if a == 0:
    username = input("enter the name: ")
    if username in content:
        password2 = input("Enter the password: ")
        if password2 in content:
            print("Your credential exist")
        else:
            print("wrong password")
    else:
        print("Credential not exist so go for registration")
#stage-3 done
if a == 1:
    import re
    #check whether username valid or not
    pattern="^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_name=input("enter the user name:")
    if re.search(pattern, user_name):
        print("valid user name")
        if user_name in content:
            print("username exists. Choose a unique one.")
        else:
            password = input("Enter the password: ")

            import re
            #check whether password valid or not(stage-1 of assignment done)
            pattern = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&+=]).*$"
            password = input("Enter Password:")
            result = re.findall(pattern, password)
            if (result):
                print("Password is valid")
            else:
                print("Password is not valid")
            with open('trial.txt', 'a') as g:
                g.write("\n")
                g.write("username: ")
                g.write(user_name)
                g.write("\n")
                g.write("password: ")
                g.write(password)
                print("you are registered")
    else:
        print("user id not valid")























