def sortByAlphabet(inputSet):
    return int(inputSet.split()[-1])


def get_files_sizes():
    a = os.listdir()
    b = []
    c = []
    for i in range(len(a)):
        b.append(f"{a[i]} {os.path.getsize(a[i])}")

    b.sort(key=sortByAlphabet, reverse=True)
    for i in range(len(b)):
        if int((b[i].split())[-1]) >= 1024:
            n = int((b[i].split())[-1]) / 1024
            n1 = round(n)
            k = (f"{b[i].split()[0]} {n1}КБ")
            if n >= 1024:
                n /= 1024
                n1 = round(n)
                k = (f"{b[i].split()[0]} {n1}МБ")
                if n >= 1024:
                    n /= 1024
                    n1 = round(n)
                    k = (f"{b[i].split()[0]} {n1}ГБ")
        else:
            k = (f"{b[i].split()[0]} {b[i].split()[-1]}Б")
        c.append(k)
    return ("\n".join(c[:10]))


print(get_files_sizes())
