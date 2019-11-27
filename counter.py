import datetime
import pytz
import functions


class Counter:
    def __init__(self, id, name, clock):
        self.id = id
        self.name = name
        self.minutes = self.__set_minutes(clock)

    def __set_minutes(self, clock):
        time_now = datetime.datetime.now()
        clock_parsed = datetime.datetime.strptime(clock, "%Y-%m-%d-%H-%M")
        time_remaining = clock_parsed - time_now

        minutes = []

        for i in range(1, 61, 1):
            time_frame = functions.pretty_time_delta(
                (time_remaining.seconds + (time_remaining.days * 86400)) - i
            )
            minutes.append(time_frame)

        return minutes


# print("Current datetime: {}".format(datetime.datetime.now().strftime("%u:%H:%M:%S")))

if __name__ == "__main__":
    counting = Counter(1, "sss", "2019-11-26-10-55")
    print(counting.minutes)
