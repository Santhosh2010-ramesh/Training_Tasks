import qrcode

# Get user input for the QR code data
data = input("Enter text or URL: ")

# Create the QR code
qr = qrcode.make(data)

# Save the QR code as a PNG file
qr.save("qrcode.png")

# Confirm that the QR code has been generated and saved
print("QR Code generated and saved as 'qrcode.png'!")
