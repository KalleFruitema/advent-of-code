print(sum(int(2**(len(set.intersection(*[set([x for x in i.split(" ") if x != ""]) for i in card.split("|")])) - 1)) for card in [line.strip().split(":")[1] for line in open("2023/dag_4/input.txt", 'r')]))