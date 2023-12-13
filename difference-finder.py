from PIL import Image
#original image and image with difference
input_image=Image.open(#path to the original image)
difference=Image.open(#path to the image with differences)



widthA, heightB= input_image.size
widthC, heightD= difference.size
min_width= min(widthA, widthC)
min_height= min(heightB, heightD)
input_image= input_image.resize((min_width, min_height))
difference= difference.resize((min_width, min_height))
width1, height1= input_image.size
width2, height2= difference.size

Original_map= input_image.load()
difference_map= difference.load()
for i in range(width2):
    for j in range(height2):
        r1, g1, b1, p1 = input_image.getpixel((i, j))
        r2, g2, b2, p1 = difference.getpixel((i, j))
        sum_of_colors1= sum([r1, g1, b1])
        sum_of_colors2 = sum([r2, g2, b2])
        grayscale = (0.299 * r2 + 0.587 * g2 + 0.114 * b2)
        if sum_of_colors2 not in range(sum_of_colors1-110, sum_of_colors1+110):
            difference_map[i, j]=(int(grayscale), int(grayscale), int(grayscale))
difference.save(#where do you want to save the image +"diferences.PNG", format="png")
