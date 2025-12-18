import qrcode

data = "https://github.com/Rahmatul-Rovi" 

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# ইমেজ তৈরি ও সেভ
img = qr.make_image(fill_color="black", back_color="white")
img.save("Github.png")

print("Congratulations! Your QR code has been ready and save.")