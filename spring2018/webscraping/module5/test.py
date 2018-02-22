import re
addr = "2706 10th Street, Bloomington, IN - 47408"
zip_expr = r'\d\d\d\d\d'
street_expr = r'^\d+ \d+\w* (Street|St|st), [A-Z]\w*'
state_expr = r'[A-Z][A-Z]'

zip_regex = re.compile(zip_expr)
zip_match = zip_regex.search(addr)
if zip_match:
    print("Found the address {}".format(zip_match.group()))
else:
    print("No match!")

state_regex = re.compile(state_expr)
state_match = state_regex.search(addr)
if state_match:
    print("Found the state {}".format(state_match.group()))
else:
    print("No match!")

street_regex = re.compile(street_expr)
street_match = street_regex.search(addr)
if street_match:
    print("Found the street {}".format(street_match.group()))
else:
    print("No match!")
