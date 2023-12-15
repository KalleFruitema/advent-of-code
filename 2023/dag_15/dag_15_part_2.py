from re import split
from pprint import pprint


def translate_label(label):
    key = 0
    for char in label:
        key += ord(char)
        key *= 17
        key %= 256
    return key


with open("2023/dag_15/input.txt", 'r') as file:
    str_lst = file.read().split(",")
    

all_vals = {}
for s in str_lst:
    label = split(r"[=-]", s)[0]
    key = translate_label(label)
    if "=" in s:
        if key not in all_vals:
            all_vals[key] = [(label, int(s.split("=")[1]))]
        else:
            for i, y in enumerate(all_vals[key]):
                if y[0] == label:
                    all_vals[key][i] = (label, int(s.split("=")[1]))
                    break
            else:
                all_vals[key].append((label, int(s.split("=")[1])))
            
    elif "-" in s and key in all_vals:
        for i, y in enumerate(all_vals[key]):
            if y[0] == label:
                all_vals[key].pop(i)
                break


total = 0
for box, lst in all_vals.items():
    box_total = 0
    for i, y in enumerate(lst, start=1):
        box_total += (box + 1) * i * y[1]
    total += box_total
    
print(total)
