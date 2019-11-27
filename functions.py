import datetime


def tdeltaformat(timedelta):
    return (
        str(timedelta.days)
        + ":"
        + str(timedelta.seconds // 3600)
        + ":"
        + str((timedelta.seconds // 60) % 60)
    )


def pretty_time_delta(seconds):
    sign_string = "-" if seconds < 0 else ""
    seconds = abs(int(seconds))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    return "%s%02d:%02d:%02d:%02d" % (sign_string, days, hours, minutes, seconds)
