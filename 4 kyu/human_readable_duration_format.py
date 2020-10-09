'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
'''


def format_duration(seconds):
    if seconds == 0:
        return "now"
    lst = [seconds // (365*24*60*60), (seconds // (24*60*60))%(365), (seconds//(60*60))%(24), (seconds//60)%60, seconds%60]
    times = {0:"year", 1:"day", 2:"hour", 3:"minute", 4:"second"}
    total = []
    for i in range(len(lst)):
        if lst[i] != 0:
            if lst[i] > 1:
                total.append(str(lst[i]) + " " + times[i] + "s")
            else:
                total.append(str(lst[i]) + " " + times[i])
    if len(total) == 1:
        return total[0]
    elif len(total) == 2:
        return total[0] + " and " + total[1]
    else:
        return ', '.join(total[:-1]) + " and " + total[-1]