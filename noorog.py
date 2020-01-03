# Improting Image class from PIL module
from PIL import Image
from PIL import ImageOps
import os

# Opens a image in RGB mode

os.chdir(r"C:\Users\ADMIN\Desktop\Sanjaa\카탈로그\3.Audi\A5")
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        size_3600 = (3600, 3600)
        i.thumbnail(size_3600)
        i.save("3600/{}{}".format(fn, fext))

        width, height = i.size

        if width < height:

            size_450 = (200, 100000)
            i.thumbnail(size_450)

            left = 0
            top = 0
            right = 200
            bottom = 150

            im = i.crop((left, top, right, bottom))
            im.save("450/{}{}".format(fn, fext))

        elif width > height:

            size_450 = (1000000, 150)
            i.thumbnail(size_450)
            w, h = i.size
            print(w, h)
            start_pixel = (w - 200) / 2
            end_pixel = start_pixel + 200
            im = i.crop((start_pixel, 0, end_pixel, 150))
            im.save("450/{}{}".format(fn, fext))