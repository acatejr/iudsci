# assignment2.py
# author: Averill Cate, Jr
import datetime

# Data for problem 3
my_med_dict = {
    "Abelcet":"Aug 1 2016",
    "Azithromycin":"Dec 24 2016",
    "Arava":"Jan 1 2019",
    "Arixtra":"May 31 2022",
    "Aplenzin":"Jan 3 2020",
    "Antizol":"Aug 31 2023",
    "Anadrol-50":"Nov 14 2010"
}

def dec_to_bin_iter(d):
    """ Problem 1. Converts decimal int to binary using iteration.
    """
    bin_list = []
    n = d
    while (n > 0):
        q = n // 2        
        r = n % 2
        bin_list.append(r)
        n = q

    bin_str = "".join(str(i) for i in bin_list[::-1])
    return bin_str

def arr_to_dec(arr):
    """ Problem 2. Given an array representing a binary number convert ot decimal
    """
    total = 0
    for i in arr[:]:
        total = (2 * total) + i        

    return total

def expired_meds(meds):
    """ Problem 3.  Using the medicine dictionary print those items that are expired.
    """

    print("\nExpired Meds:")
    print("=" * 20)
    for m in meds:
        med_name = m
        med_exp_date = datetime.datetime.strptime(meds[m], '%b %d %Y')
        if med_exp_date < datetime.datetime.now():
            print("{} expired on {}".format(med_name, meds[m]))

if __name__ == '__main__':
    print("The integer 12 in binary is {}.".format(dec_to_bin_iter(12)))
    print("The integer 5 in binary is {}.".format(dec_to_bin_iter(5)))
    print("The integer 293 in binary is {}.".format(dec_to_bin_iter(293)))

    print("Binary 1100 in binary is {}.".format(arr_to_dec([1,1,0,0])))
    print("Binary 101 in binary is {}.".format(arr_to_dec([1,0,1])))
    print("Binary 100100101 in binary is {}.".format(arr_to_dec([1,0,0,1,0,0,1,0,1])))

    expired_meds(my_med_dict)