def permutation_init(str):
    permutation(str, "")


def permutation(str, prefix):
    if len(str) == 0:
        print(prefix)
    else:
        for i, s in enumerate(str):
            rem = str[0:i] + str[i + 1:]
            permutation(rem, prefix + str[i])


permutation_init("abcdefg")
