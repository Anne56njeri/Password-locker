#!/usr/bin/env python3.6
from user import User
from credentials import Info

def create_account(f_name,m_name,e_mail):
    new_user = User(f_name,m_name,e_mail)
    return new_user
def create_credentials(face_bookp,e_mailp):
    new_cred = Info(face_bookp,e_mailp)
    return new_cred
def save_account(user):
    user.save_user()
def save_credentials(credentials):
    credentials.save_info()
def display_users():
    return User.display_user()
def display_creds():
    return Info.display_info()    
def main():
    print("Hello there welcome to password locker .....")
    while True:
        print("Use the following short codes :cc- create an a new account ,ex- exit the password locker")
        short_code = input() .lower()
        if short_code =='cc':
            print("Create a new account")
            print ("-"* 10)

            print("what is your first name...")
            f_name =input()
            print("What is your middle name...")
            m_name= input()
            print("what is your email address..")
            e_mail= input()
            print ("what is your facebook password...")
            face_bookp =input()
            print("what is your email password...")
            e_mailp= input()
            save_account(create_account(f_name,m_name,e_mail))
            print('\n')
            save_credentials(create_credentials (face_bookp,e_mailp))
            print('\n')
            print(f"New Account  {f_name}{m_name}{face_bookp} has been created")
            print('\n')
        elif short_code == "ex":
            print("Bye... Bye...")
            break
        else:
            print("please select one ofthe options provided")

if __name__ == '__main__':

    main()
