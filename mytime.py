from datetime import datetime 


def time_to_second(hour = 0, minute = 0, second = 0):
    try: 
        return hour * 3600 + minute * 60 + second
    
    except:
        return "Dude enter a number"

def time_difference_hour(hour):
    time = datetime.now()

    now_hour = time.hour
    
    if hour - now_hour < 0:
        now_hour = 24 + (hour - now_hour)

    else:
        now_hour = hour - now_hour

    return now_hour


def time_difference_min(minute):
    time = datetime.now()

    now_min = time.minute
    
    if minute - now_min < 0:
        now_min = 60 + minute - now_min

    else:
        now_min = minute - now_min

    return now_min

def time_difference_sec(second):
    time = datetime.now()

    now_sec = time.second
    
    if second - now_sec < 0:
        now_sec = 60 + second - now_sec

    else:
        now_sec = second - now_sec

    return now_sec