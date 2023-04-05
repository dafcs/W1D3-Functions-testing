
def return_10():
    return 10

def add(val1,val2):
    res = val1 + val2
    return res

def subtract(val1,val2):
    res = val1 - val2
    return res

def multiply(val1,val2):
    res = val1 * val2
    return res

def divide(val1,val2):
    res = val1 / val2
    return res

def length_of_string(string):
    lst = len(string)
    return lst

def join_string(st1,st2):
    resco = st1 + st2
    return resco

def add_string_as_number(val1,val2):
    string_num1 = int(val1)
    string_num2 = int(val2)
    res = string_num1 + string_num2
    return res

def number_to_full_month_name(month_number):
    months = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    return months[month_number]

def number_to_short_month_name(mon_num):
       months = {
        1:"Jan",
        2:"Feb",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"Jun",
        7:"Jul",
        8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nov",
        12:"Dec"
    } 
       return months[mon_num]

def calc_cube_volume(height, width, length):
    cub_vol = height * width * length
    return cub_vol

def reverse_string(str):
    revs = str[::-1]
    return revs

def conv_far_celc(farn):
    Celcius = (farn - 32) * 5/9
    return Celcius
