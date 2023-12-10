from Seedrange import Seedrange
from Maprange import Maprange
from pprint import pprint


def parse_input() -> tuple[list[Seedrange], dict[str, list[Maprange]]]:
    with open(r'2023/dag_5/input_test.txt') as file:
        content = [line.strip() for line in file]

    seeds, content = content[0].split(":")[1].strip().split(" "), content[1:]

    seeds = [Seedrange(int(seeds[i]), int(seeds[i+1])) 
            for i in range(0, len(seeds), 2)]

    map_book = {}
    book_page = {}
    for line in content[1:]:
        if line == "":
            map_book.update(book_page)
            book_page = {}
        elif "-" in line:
            curr_page = line.split("-")[2].split(" ")[0]
            book_page[curr_page] = []
        else:
            book_page[curr_page].append(Maprange(*[int(i) for i in line.split(" ")]))
    map_book.update(book_page)
    
    return seeds, map_book


def ffffffffffffffff(seed_lst: Seedrange | list[Seedrange], maps: list[Maprange]):
    if not isinstance(seed_lst, list):
        seed_lst = [seed_lst]
    
    mapped = []
    for map_range in maps:
        n_seed_lst = []
        for seed in seed_lst:
            print(seed, map_range)
            seed.intersect(map_range)
        


def main():
    seeds, map_book = parse_input()
    for title, page in map_book.items():
        print(f"\n{title}")
        for seed in seeds:
            ffffffffffffffff(seed, page)
    
    
if __name__ == "__main__":
    main()
    