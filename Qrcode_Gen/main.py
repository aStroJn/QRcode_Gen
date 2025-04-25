import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from input import img

# Create a object
qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=100,
border=2,
)

# Add data 
qr.add_data(img)
qr.make(fit=True)

# Create an image 
image = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), fill_color="black", back_color="white")

# Save the image
image.save('custom_qrcode.png')