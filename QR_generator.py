# pip install qrcode[pil]
import qrcode
from qrcode.constants import ERROR_CORRECT_M

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_M,
    box_size=10,   # pixel size per box
    border=4       # quiet zone
)
qr.add_data(input("Enter text/URL: "))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
print("✅ QR saved as qr_code.png")
