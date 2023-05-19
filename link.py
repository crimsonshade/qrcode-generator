import qrcode

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
        img.convert("RGB").save("img/link.png")