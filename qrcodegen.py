import qrcode

def qrcodegen(text, file_name):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


def main():
    text = input("Give a link to be qrcoded: ")
    pick_name = input("Where does this qrcode lead to?: ")
    file_name = pick_name + "_qrcode.png"
    qrcodegen(text, file_name)
    print(f"qr code saved as {file_name}")


if __name__ == "__main__":
    main()