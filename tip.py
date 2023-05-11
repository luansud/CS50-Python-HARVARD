def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    money_float = d.replace("$","")
    return float(money_float)


def percent_to_float(p):
    percent_value = p.replace("%","")
    percent_float = float(percent_value) / 100
    return percent_float

main()