# assignment2.py
# author: Averill Cate, Jr
import datetime, os
import numpy as np
import pandas as pd

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CRIME_DATA_COLUMNS = [
    'ADDRESS', 'ARSON', 'ASSAULT', 'BAD_CHECKS', 
    'BRIBERY', 'BURGLARY', 'DISORDERLY_CONDUCT', 
    'DRIVING_UNDER_THE_INFLUENCE', 'DRUG/NARCOTIC', 
    'DRUNKENNESS', 'EMBEZZLEMENT', 'EXTORTION', 
    'FAMILY_OFFENSES', 'FORGERY/COUNTERFEITING', 
    'FRAUD', 'GAMBLING', 'KIDNAPPING', 
    'LARCENY/THEFT', 'LIQUOR_LAWS', 'LOITERING', 
    'MISSING_PERSON', 'NON_CRIMINAL', 'OTHER_OFFENSES', 
    'PORNOGRAPHY/OBSCENE_MAT', 'PROSTITUTION', 'RECOVERED_VEHICLE', 
    'ROBBERY', 'RUNAWAY', 'SECONDARY_CODES', 'SEX_OFFENSES_FORCIBLE', 
    'SEX_OFFENSES_NON_FORCIBLE', 'STOLEN_PROPERTY', 'SUICIDE', 
    'SUSPICIOUS_OCC', 'TREA', 'TRESPASS', 'VANDALISM', 'VEHICLE_THEFT', 'WARRANTS', 
    'WEAPON LAWS'
]

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

def dec_to_bin_rec(n):
    """ Recursive function for converting decimal to binary.
    """    
    # Base case
    if n < 1:
        return n % 2
    else:
        q = n // 2        
        r = n % 2
        return str(dec_to_bin_rec(q)) + str(r)

def crimes_by_type(crime):
    """ Problem 5.  Calculates the mean of that crime, i.e., average number 
    of times that crime has happened at addresses.  The function should return 
    all the address (may be in a list) where this crime has occurred more than 
    the mean number of times.
    """
    file_name = BASE_DIR + '/crime.csv'
    data = pd.read_csv(file_name, sep=',')
    data.columns = CRIME_DATA_COLUMNS
    avg = data[crime].mean()
    results = data[data[crime] > avg]
    return results.ADDRESS.values

if __name__ == '__main__':
    # Dec to bin iterative
    print("The integer 12 in binary is {}.".format(dec_to_bin_iter(12)))
    print("The integer 5 in binary is {}.".format(dec_to_bin_iter(5)))
    print("The integer 293 in binary is {}.".format(dec_to_bin_iter(293)))

    # Bin to dec iterative
    print("Binary 1100 in binary is {}.".format(arr_to_dec([1,1,0,0])))
    print("Binary 101 in binary is {}.".format(arr_to_dec([1,0,1])))
    print("Binary 100100101 in binary is {}.".format(arr_to_dec([1,0,0,1,0,0,1,0,1])))

    # Expired meds
    expired_meds(my_med_dict)

    print("\n")
    # Dec to bin recursive
    print("The integer 12 in binary is {}.".format(dec_to_bin_rec(12)[1:]))
    print("The integer 5 in binary is {}.".format(dec_to_bin_rec(5))[1:])
    print("The integer 293 in binary is {}.".format(dec_to_bin_rec(293)[1:]))
    print("The integer 9 in binary is {}.".format(dec_to_bin_rec(9)[1:]))

    # Crimes
    crime_name = 'EXTORTION'
    print("\nThe following addresses exceed the average rate for {}".format(crime_name))
    print("="*70)
    addresses = crimes_by_type(crime_name)
    for a in addresses:
        print(a)

    crime_name = 'DRUNKENNESS'
    print("\nThe following addresses exceed the average rate for {}".format(crime_name))
    print("="*70)
    addresses = crimes_by_type(crime_name)
    for a in addresses:
        print(a)