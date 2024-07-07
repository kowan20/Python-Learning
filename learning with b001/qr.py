import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border=4,
)
qr.add_data("I'm gonna make you moan")
qr.make(fit=True)
img = qr.make_image(back_color=(0,0,0), fill_color=(255,255,51))