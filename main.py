import giffer
import counter


class Main:
    def __init__(self):
        self.giffer = giffer.Giffer()

    def main(self, name, countdown):
        numbers = counter.Counter(1, name, countdown)
        frames = self.giffer.create_frames(400, 200, numbers.minutes)
        self.giffer.save_gif(name, frames)


if __name__ == "__main__":
    main = Main()
    main.main()
