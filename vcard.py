import qrcode

class qr_vcard:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def generate_vcard(self):
        data = f"BEGIN:VCARD\nVERSION:4.0\nN:{self.name}\nEMAIL:{self.email}\nTEL:{self.phone}\nGENDER:M\nEND:VCARD"

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        # make the QR code to an image
        img = qr.make_image(fill_color="black", back_color="white")

        # Create the file
        img.convert("RGB").save("vcard.png")