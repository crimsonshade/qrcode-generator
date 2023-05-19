import os
from vcard import qr_vcard
from link import qr_link

def clear_console():
    os.system('clear')

def fin():
    print("=========================")
    print("Your qr code got generated.")

if __name__ == "__main__":
    clear_console()
    print("""What do you want me to create:
=========================

    1. A vcard with your Name, your Email, and your Phone number
    2. A scanable link

=========================
    """)
    choice = input("Your choice: ")
    clear_console()

    if(choice == "1"):
        name = input('Enter your Name\n>')
        email = input("\nYour Email\n>")
        phone = input("\nYour phone number\n>")

        vcard = qr_vcard(name, email, phone)
        vcard.generate_vcard()
        fin()
    elif(choice == "2"):
        url = input("\nEnter the link\n>")

        link = qr_link(url)
        link.generate_link()
        fin()
    else:
        print("Wrong number. Try again")