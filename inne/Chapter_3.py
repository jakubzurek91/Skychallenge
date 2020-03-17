b = 0
for element in range(372**2, 809**2+1):

    # unpack string elements to list integers
    tmp = [int(d) for d in str(element)]

    # checking criteria the digits never decrease
    if tmp == sorted(tmp):
        set_tmp = set(tmp)
        count_repeat = 0

        # counting number of repeat
        for value in set_tmp:
            if tmp.count(value) >= 2:
                count_repeat += 1

        # checking criteria at least two groups of identical adjacent digits
        if count_repeat >= 2:
            print(tmp)
            b += 1

