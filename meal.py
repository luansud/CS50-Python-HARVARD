def main():
    time = input("What time is it? ")
    value = convert(time)
    if value >= 7 and value <= 8:
        print("breakfast time")
    elif value >= 12 and value <= 13:
        print("lunch time")
    elif value >= 18 and value <= 19:
        print("dinner time")


def convert(value):
    hours, minutes = value.split(":")
    time_float = float(hours) + (float(minutes) / 60)
    return time_float

if __name__ == "__main__":
    main()