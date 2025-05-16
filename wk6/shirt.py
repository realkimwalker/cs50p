from sys import argv
from PIL import Image, ImageOps
import os

def main():
    try:
        if len(argv) < 3:
            exit("Too few command-line arguments")
        elif len(argv) > 3:
            exit("Too many command-line argument")
        elif argv[1].endswith(".png" or ".jpg" or "jpeg"):
            exit("Invalid file")
        elif argv[2].endswith(".png" or ".jpg" or "jpeg"):
            exit("Invalid file")
        else:
                shirt = Image.open("shirt.png")
                size = shirt.size
                image = Image.open(argv[1])
                image_fitted = ImageOps.fit(image, size)
                image_fitted.paste(shirt, shirt)
                image_fitted.save(argv[2])


    except FileNotFoundError:
        exit(f"Could not read {argv[1]}")


if __name__=="__main__":
    main()
