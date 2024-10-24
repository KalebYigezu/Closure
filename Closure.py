def enter_number_outer():
    numbers = []

    def enter_number(x):
        numbers.append(x)
        print(numbers)

    return enter_number


enter_number = enter_number_outer()
enter_number(5)
enter_number(7)
enter_number(9)

https://www.youtube.com/watch?v=yiSdpYmZA2w
