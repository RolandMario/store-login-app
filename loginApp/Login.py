users = {"Roland": "mario", "Akpe": "1234"}
def login(username,password):
    for usern, passw in users.items():
        if usern == username and passw == password:
            print("Login Successful")
        else:
            print("Wrong Credentials")

login("xxx", "1234")
