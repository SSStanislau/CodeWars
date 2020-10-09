'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
'''


def parse(num):
    if num < 10:
        return '0{}'.format(num)
    else:
        return num
		
def make_readable(seconds):
    hh = seconds//3600
    mm= (seconds - int(hh) * 3600)//60
    ss = seconds - int(hh)*3600 - int(mm)*60
    return '{}:{}:{}'.format(parse(hh),parse(mm),parse(ss))