#gif.py 
import sys
import datetime
import imageio

VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'sph.gif'
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":
    filenames = []
    for i in range(1,1500, 20):
        filenames.append(str(i)+ ".png")

    create_gif(filenames, 0.1)