#user will be able to view the passwords
#user will be able to add the  passwords
#user will be able to quit the program
from cryptography.fernet import Fernet



#function will be called

#creating a key 
'''
key = Fernet.generate_key()
def cryptographic():
      
    with open("key.key" , "wb") as keyfile:
        keyfile.write(key)
        
        '''
#this function loads the key file and returning the key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    return key

#key variable hold the load_key() inside load_key() its returning the key
key = load_key()

#creating a object that will hold class Fernet and as a parameter we are giving  out key
cipher = Fernet(key)       

#need a way to use the key and the master password


def add_password():
    user_name = input("Enter username: ")
    psw = input("enter password: ")
    
    with open("password_manager.txt", "a") as f:
       f.write(user_name + " | " + cipher.encrypt(psw.encode()).decode() + "\n")
            
def view_password():
    with open("password_manager.txt", "r") as f:
        for line in f.readlines():

            #strip will remove whitespace
            data = line.rstrip() 

            #split will remove the pipeline and store user name in user variable and password in password variable
            user , password = data.split(" | ")

            print("User: "+  user + " | Password: " +  cipher.decrypt(password.encode()).decode())

#take input from the user
while(True):

    master_psw = input("What is the Master password or press q to quite: ").lower()

    if master_psw == "q":
        print("Thank you for using the password manager.")
        break

    if master_psw == 'key':

        user_input = input("Do You want to add/view the password: ").lower()

        if user_input == "add":
            add_password()

        elif user_input == "view":
            view_password()

        else:
            print("Invalid input")

    else:
        print("Enter the correct Master Password")

        







