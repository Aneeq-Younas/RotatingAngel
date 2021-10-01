def nmbrs (all):

    final = nums(all, all)
    return final

def nums (all, length):
    if all == 0:
        return [""]

    if all == 1:
        return ["7", "11", "3"]
    cntr = nums(all - 2, length)
    final = []
    for i in cntr:
        if all != length:

             final.append("15" + i + "15")
        final.append(("11" + i + "11"))
        final.append(("5" + i + "7"))
        final.append(("3" + i + "9"))
        final.append(("2" + i + "5"))

    return final

print("Number  2:\n ", nmbrs(2))
print("Number  4:\n ", nmbrs(4))
print("Number  9:\n ", nmbrs(9))
