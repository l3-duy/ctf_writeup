from PIL import Image
img1=Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
img2=Image.open('flag_7ae18c704272532658c10b5faad06d74.png')
width, height = img1.size
for x in range(width):
    for y in range(height):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))
        r = pixel1[0] ^ pixel2[0]
        g = pixel1[1] ^ pixel2[1]
        b = pixel1[2] ^ pixel2[2]
        img1.putpixel((x, y), (r, g, b))
img1.save('flag.png')