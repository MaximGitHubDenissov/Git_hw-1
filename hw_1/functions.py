
def digits_total(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

def input_is_valid(text):
    while True:
        num = input(text)
        try:
            num = int(num)
            return num
        except:
            print('Нужно вводить целые числа!')