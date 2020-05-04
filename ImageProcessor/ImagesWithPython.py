from PIL import Image, ImageFilter

img = Image.open(r'..\Pictures\pikachu.jpg')
filtered_img = img.convert('L')
filtering_img = img.filter(ImageFilter.BLUR)
filtered_img.save("..\Pictures\greyPikachu.png", 'png')
filtering_img.save("..\Pictures\\blurPikachu.png", 'png')

filtered_img.show()
