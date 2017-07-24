n = 123

converted_string = ''


def convert_to_string(n):
    global converted_string
    while n > 0:
        # get the last number in the whole sequence
        next_num = n % 10
        # convert 3 => '3'
        # 0 starts at 48
        converted_string = chr(48 + next_num) + converted_string
        n = n // 10


convert_to_string(n)
print(converted_string)
