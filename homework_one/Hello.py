from datetime import date


def get_date():
    return date.today().strftime('%d %B, %Y')


def say_hello(name, weekday=get_date()):
    print(f"Today, {weekday}, I`m glad to welcome you {name}")


say_hello(name='Alexander')
