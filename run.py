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
def main():
    print("Hello there welcome to password locker .....")
    while True:
        print("Use the following short codes :cc- create an a new account")
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
            print ('\n')
            save_credentials(save_credentials(face_bookp,e_mailp))
            print('\n')
            print(f"New Account  {f_name}{m_name}{face_bookp} has been created")
            print('\n')
        else:
            print("please enter options listed above")

if __name__ == '__main__':
    
    main()
