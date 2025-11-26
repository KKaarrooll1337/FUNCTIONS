def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n*0.393700787

def ft_and_in_to_cm(f, i):
    n = f * 30.48 + i * 2.54
    return n

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'3cm = {cm_to_in(3)}in')
    print(f'12ft 3in = {ft_and_in_to_cm(12, 3)}cm')
