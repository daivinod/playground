import qrcode
from PIL import Image
import requests

# vCard data
vcard_data = """BEGIN:VCARD
VERSION:3.0
N:Rajagopal;Vinoth Kumar;;;
FN:Vinoth Kumar Rajagopal
TITLE:Founder & CEO
ORG:ABOSS Technologies India (OPC) Pvt Ltd
TEL;WORK;VOICE:+91 9003399595
TEL;WORK;VOICE:0456244333
EMAIL:vinoth@aboss.in
EMAIL:hello@aboss.in
ADR;WORK:;;7/3-2, Kannirajapuram Road, Sayalgudi;Ramanathapuram District;Tamil Nadu;623120;India
URL:https://www.aboss.in
END:VCARD
"""

# Generate QR code
qr = qrcode.QRCode(
    version=5,  # Adjusted size for better fit with the logo
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for adding a logo
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo
logo_url = "https://media.licdn.com/dms/image/v2/C560BAQHnOnsEm88S9w/company-logo_100_100/company-logo_100_100/0/1671424139490?e=1740614400&v=beta&t=9nGQIudFz5I3Z1gTilKN5SJHTwjzRoTEg03bV_8ZCaA"
response = requests.get(logo_url, stream=True)
logo = Image.open(response.raw)

# Ensure the logo has an alpha channel
logo = logo.convert("RGBA")

# Resize the logo
logo_size = int(qr_img.size[0] * 0.2)  # Logo size as 20% of the QR code size
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Create a mask for the logo's transparency
logo_mask = logo.split()[3]  # Extract the alpha channel

# Calculate position to paste the logo
pos = (
    (qr_img.size[0] - logo.size[0]) // 2,
    (qr_img.size[1] - logo.size[1]) // 2
)

# Paste the logo onto the QR code with the transparency mask
qr_img.paste(logo, pos, mask=logo_mask)

# Save the final QR code with logo
qr_img.save("vcard_qr_with_logo.png")