counter= 0
def permutation_init(str):
    permutation(str, "")


def permutation(str, prefix):
    global counter
    print(f'call number: {counter}')
    counter +=1

    if len(str) == 0:
        print(prefix)
    else:
        for i, s in enumerate(str):
            rem = str[0:i] + str[i + 1:]
            new_prefix = prefix + str[i]
            permutation(rem, new_prefix)


permutation_init("abc")
