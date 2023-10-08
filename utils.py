def isfloat(num):
    try:
        num = num.replace(',', '.')
        float(num)
        return True
    except ValueError:
        return False
