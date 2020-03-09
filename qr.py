import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

print('Text to QR-tify:')
input_data = input();
qr.add_data(input_data)
qr.make(fit=True)
print('select colors:\n(1)QR Code Color\n(2)Background color')



colors = ['orange','red','blue','green','grey','black','white','mediumvioletred','tomato','brown','mediumseagreen','darkslategray','indigo','darksalmon','cyan','palevioletred','darkcyan','firebrick','darkolivegreen','forestgreen','darkslateblue','olive','greenyellow','lime','wheat','gold']
available = ', '.join(sorted(colors)).upper()

print(f'Colors {available} can be selected.')

print('\nSelect code color:')
qr_color = input()
while qr_color not in colors:
    qr_color = input()

print('\nSelect background color:')
qr_back = input()
while qr_back not in colors:
    qr_back = input()

img = qr.make_image(fill_color=qr_color, back_color=qr_back)


from string import punctuation
punc = list(punctuation)

title = ''
for el in input_data[:50]:
    if el not in punctuation:
        if not el.isspace():
            title+=el
        else:
            title+='_'

img.save(f'{title[:5]}.png')
