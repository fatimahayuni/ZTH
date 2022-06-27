dict_1 = {'A':1, 'B':2, 'C':3}
dict_2 = {'B':4, 'C':5, 'D':6}

a_counter = Counter(dict_1)
b_counter = Counter(dict_2)

add_dict = a_counter + b_counter
dict_3 = dict(add_dict)
