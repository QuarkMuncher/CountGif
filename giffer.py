from PIL import Image, ImageDraw, ImageFont


class Giffer:
    def __init__(self):
        self.font = ImageFont.truetype("./res/DankMono-Regular.ttf", 40)

    # Uses PIL library to create single image.
    def __create_image(self, width, height, text):
        img = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), text, font=self.font, fill=(255, 255, 255, 255))
        return img

    # loops 10 times and moves ball position, for each turn, and returns list of image objects.
    def create_frames(self, width, height, content):
        frames = []
        for i in range(60):
            new_frame = self.__create_image(width, height, content[i])
            frames.append(new_frame)
        return frames

    # Creates a gif from the array of images.
    def save_gif(self, name, frames):
        # Params for save()
        #   string: Name of the output file.
        #   format: file encoding.
        #   append_images: is for animating gifs, defing the images to
        #       append to the gif, frames[1:] defines the range 1 to
        #       the end of list.
        #   save_all: True, will save all the images as a single gif.
        #   duration: How long a single image lasts
        #   loop: how many times to loop gif => 0 means infinite.
        frames[0].save(
            name,
            format="GIF",
            append_images=frames[1:],
            save_all=True,
            duration=1000,
            loop=0,
        )


def main():
    make = Giffer()
    gif = make.create_frames(400, 400, 0, 0, 40)
    make.save_gif(gif)


if __name__ == "__main__":
    main()
