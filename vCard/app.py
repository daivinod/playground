import qrcode

# vCard data
vcard_data = """BEGIN:VCARD
VERSION:3.0
N:Lingeswaran;Suyamburaj Pandian;;;
FN:Suyamburaj Pandian L
TITLE:Senior Developer
ORG:ABOSS Technologies India (OPC) Pvt Ltd
TEL;WORK;VOICE:+91 7339650900
EMAIL:suyamburajpandian.lingeswaran@aboss.in
ADR;WORK:;;7/3-2, Kannirajapuram Road, Sayalgudi;Ramanathapuram District;Tamil Nadu;623120;India
URL:https://www.aboss.in
END:VCARD
"""

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("vcard_qr.png")