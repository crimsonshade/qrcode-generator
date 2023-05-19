import qrcode
import os

class qr_vcard:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def generate_vcard(self):
        data = f"BEGIN:VCARD\nVERSION:4.0\nN:{name}\nEMAIL:{email}\nTEL:{phone}\nGENDER:M\nEND:VCARD"

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        # make the QR code to an image
        img = qr.make_image(fill_color="black", back_color="white")

        # Create the file
        img.convert("RGB").save("vcard.png")

class qr_link:
    def __init__(self, url):
        self.url = url

    def generate_link(self):
        data = self.url
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        # make the QR code to an image
        img = qr.make_image(fill_color="black", back_color="white")

        # Create the file
        img.convert("RGB").save("link.png")

def clear_console():
    os.system('clear')

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
        name = input("Your name: ")
        email = input("Your Email: ")
        phone = input("Your phone number: ")

        vcard = qr_vcard(name, email, phone)
        vcard.generate_vcard()
