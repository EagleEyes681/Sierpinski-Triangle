from PIL import Image, ImageColor
import random
import moviepy.video.io.ImageSequenceClip

print("Do you want to make this into a video? (Only answer with YES or NO.)")
answer = str(input())
print()

print("What do you want the output filename to be? (Do not include the file extension on the end)")
fp_out_name = str(input())
print()

images_folder = "C:\\Users\\eagle\\Documents\\Side Projects\\Triangle_imgs\\"
fp_in = "C:\\Users\\eagle\\Documents\\Side Projects\\Triangle_imgs\\image_*.png"
fp_out = "C:\\Users\\eagle\\Documents\\Side Projects\\" + fp_out_name

print("How many dots do you want to draw?")
num_of_dots = int(input())

img = Image.new(mode="RGB", size=(1000, 1000), color=(250, 250, 250))
imgs = [(500, 100), (500-462, 900), (500+462, 900)]
filenames = []


for i in range(num_of_dots+1):
    j = i

    if i == 0:
        first_point = random.randint(0, 2)
        second_point = random.randint(0, 2)
        while first_point == second_point:
            second_point = random.randint(0, 2)

        x1 = imgs[first_point][0]
        y1 = imgs[first_point][1]
        x2 = imgs[second_point][0]
        y2 = imgs[second_point][1]

        new_point = (round((x1+x2)/2), round((y1+y2)/2))
        imgs.append(new_point)
    
    if i != 0:
        first_point = random.randint(0, 2)

        x1 = imgs[first_point][0]
        y1 = imgs[first_point][1]
        x2 = new_point[0]
        y2 = new_point[1]

        new_point = (round((x1+x2)/2), round((y1+y2)/2))
        imgs.append(new_point)

    if answer == "YES":
        if j <= 10000:
            if j % 100 == 0:
                for i in range(len(imgs)):
                    img.putpixel((imgs[i][0], imgs[i][1]), ImageColor.getcolor("black", "1"))
                
                filenames.append("Triangle_imgs\\image_" + str(j) + ".png")
                img.save("C:\\Users\\eagle\\Documents\\Side Projects\\Triangle_imgs\\image_" + str(j) + ".png")

        if j <= 50000:
            if j % 500 == 0:
                for i in range(len(imgs)):
                    img.putpixel((imgs[i][0], imgs[i][1]), ImageColor.getcolor("black", "1"))
                
                filenames.append("Triangle_imgs\\image_" + str(j) + ".png")
                img.save("C:\\Users\\eagle\\Documents\\Side Projects\\Triangle_imgs\\image_" + str(j) + ".png")

        if j <= 100000:
            if j % 5000 == 0:
                for i in range(len(imgs)):
                    img.putpixel((imgs[i][0], imgs[i][1]), ImageColor.getcolor("black", "1"))
                
                filenames.append("Triangle_imgs\\image_" + str(j) + ".png")
                img.save("C:\\Users\\eagle\\Documents\\Side Projects\\Triangle_imgs\\image_" + str(j) + ".png")

        if j >= 500000:
            if j % 10000 == 0:
                for i in range(len(imgs)):
                    img.putpixel((imgs[i][0], imgs[i][1]), ImageColor.getcolor("black", "1"))
                
                filenames.append("Triangle_imgs\\image_" + str(j) + ".png")
                img.save("C:\\Users\\eagle\\Documents\\Side Projects\\Triangle_imgs\\image_" + str(j) + ".png")

if answer == "YES":
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(filenames, fps=10)
    clip.write_videofile((fp_out_name + ".mp4"))

if answer == "NO":
    for i in range(len(imgs)):
        img.putpixel((imgs[i][0], imgs[i][1]), ImageColor.getcolor("black", "1"))
    
    img.save(fp=fp_out+'.png', format='PNG')
    img.show()
