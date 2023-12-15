with open("2023/dag_15/input.txt", 'r') as file:
    str_lst = file.read().split(",")
    

all_vals = []
for s in str_lst:
    val = 0
    for char in s:
        val += ord(char)
        val *= 17
        val %= 256
    all_vals.append(val)
    
print(sum(all_vals))