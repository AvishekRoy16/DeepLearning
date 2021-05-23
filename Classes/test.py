def check(value):
    if value in original:
        return True
    else:
        return False

def test(sample):
    global original
    original = set(sample)
    for i in filter(check, original):
        print(i + i)

