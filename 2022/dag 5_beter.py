from pprint import pprint


def give_inp() -> str:
    return '''move 8 from 3 to 2
move 1 from 9 to 5
move 5 from 4 to 7
move 6 from 1 to 4
move 8 from 6 to 8
move 8 from 4 to 5
move 4 from 9 to 5
move 4 from 7 to 9
move 7 from 7 to 2
move 4 from 5 to 2
move 11 from 8 to 3
move 3 from 9 to 7
move 11 from 2 to 8
move 13 from 8 to 4
move 11 from 5 to 6
move 8 from 2 to 4
move 1 from 5 to 4
move 1 from 3 to 2
move 2 from 2 to 1
move 2 from 8 to 5
move 3 from 7 to 5
move 1 from 4 to 7
move 9 from 6 to 7
move 1 from 6 to 5
move 1 from 1 to 4
move 3 from 1 to 9
move 15 from 4 to 3
move 2 from 4 to 1
move 1 from 1 to 9
move 3 from 4 to 5
move 1 from 4 to 1
move 1 from 7 to 2
move 1 from 6 to 3
move 5 from 7 to 1
move 19 from 3 to 9
move 7 from 1 to 2
move 24 from 9 to 7
move 23 from 7 to 1
move 1 from 4 to 6
move 3 from 7 to 3
move 1 from 6 to 1
move 6 from 2 to 1
move 21 from 1 to 9
move 5 from 3 to 8
move 2 from 2 to 5
move 10 from 9 to 5
move 1 from 2 to 1
move 5 from 1 to 3
move 6 from 3 to 4
move 1 from 2 to 8
move 3 from 5 to 2
move 4 from 9 to 3
move 13 from 5 to 9
move 2 from 7 to 2
move 3 from 4 to 7
move 1 from 7 to 8
move 5 from 1 to 3
move 1 from 7 to 5
move 1 from 8 to 1
move 2 from 2 to 7
move 19 from 9 to 2
move 5 from 2 to 3
move 7 from 5 to 9
move 1 from 1 to 9
move 5 from 9 to 2
move 4 from 9 to 3
move 20 from 3 to 9
move 1 from 3 to 9
move 3 from 7 to 3
move 16 from 2 to 3
move 12 from 3 to 4
move 2 from 2 to 5
move 1 from 2 to 4
move 2 from 4 to 1
move 4 from 8 to 1
move 15 from 9 to 3
move 2 from 5 to 3
move 3 from 2 to 8
move 5 from 8 to 5
move 7 from 3 to 4
move 2 from 9 to 6
move 15 from 3 to 1
move 3 from 1 to 8
move 3 from 9 to 5
move 9 from 4 to 1
move 3 from 3 to 5
move 2 from 6 to 5
move 9 from 1 to 3
move 1 from 9 to 4
move 1 from 5 to 2
move 3 from 8 to 5
move 10 from 1 to 6
move 12 from 4 to 8
move 1 from 2 to 7
move 2 from 5 to 6
move 1 from 1 to 4
move 7 from 3 to 6
move 1 from 7 to 2
move 2 from 4 to 9
move 3 from 1 to 7
move 1 from 9 to 8
move 1 from 2 to 3
move 3 from 1 to 7
move 5 from 8 to 2
move 5 from 7 to 1
move 9 from 6 to 8
move 6 from 6 to 9
move 8 from 8 to 6
move 1 from 7 to 4
move 5 from 2 to 4
move 7 from 5 to 1
move 5 from 8 to 9
move 11 from 6 to 7
move 9 from 9 to 1
move 2 from 7 to 5
move 1 from 9 to 5
move 1 from 3 to 6
move 3 from 4 to 6
move 1 from 8 to 2
move 2 from 3 to 6
move 6 from 5 to 2
move 3 from 5 to 9
move 3 from 2 to 1
move 1 from 4 to 3
move 3 from 2 to 7
move 1 from 8 to 9
move 1 from 2 to 8
move 8 from 7 to 5
move 1 from 7 to 8
move 3 from 5 to 6
move 5 from 5 to 2
move 1 from 4 to 1
move 1 from 3 to 2
move 4 from 1 to 5
move 4 from 2 to 6
move 6 from 1 to 2
move 5 from 9 to 3
move 2 from 5 to 3
move 3 from 3 to 6
move 10 from 6 to 4
move 4 from 8 to 5
move 5 from 5 to 1
move 21 from 1 to 7
move 3 from 2 to 9
move 1 from 5 to 2
move 4 from 2 to 9
move 8 from 4 to 8
move 1 from 2 to 1
move 7 from 8 to 2
move 2 from 6 to 1
move 2 from 1 to 5
move 1 from 1 to 5
move 4 from 3 to 7
move 1 from 9 to 3
move 4 from 6 to 3
move 1 from 3 to 8
move 1 from 3 to 4
move 2 from 2 to 6
move 2 from 9 to 7
move 14 from 7 to 8
move 10 from 8 to 7
move 3 from 4 to 6
move 5 from 2 to 3
move 3 from 9 to 8
move 3 from 3 to 4
move 1 from 2 to 4
move 1 from 9 to 4
move 1 from 9 to 5
move 1 from 5 to 2
move 3 from 5 to 7
move 1 from 4 to 6
move 5 from 3 to 8
move 1 from 6 to 8
move 5 from 7 to 6
move 14 from 8 to 5
move 2 from 6 to 7
move 18 from 7 to 2
move 3 from 6 to 1
move 5 from 5 to 4
move 5 from 6 to 2
move 7 from 2 to 1
move 1 from 8 to 4
move 1 from 5 to 1
move 8 from 1 to 9
move 10 from 4 to 3
move 8 from 5 to 3
move 1 from 4 to 3
move 2 from 1 to 5
move 1 from 5 to 3
move 5 from 3 to 1
move 1 from 1 to 3
move 5 from 1 to 6
move 13 from 3 to 1
move 3 from 9 to 4
move 2 from 9 to 6
move 5 from 6 to 5
move 6 from 5 to 1
move 7 from 7 to 9
move 7 from 9 to 6
move 1 from 9 to 3
move 1 from 7 to 9
move 3 from 9 to 1
move 12 from 2 to 7
move 7 from 6 to 2
move 22 from 1 to 7
move 1 from 6 to 5
move 4 from 7 to 6
move 1 from 5 to 6
move 2 from 4 to 1
move 1 from 4 to 1
move 23 from 7 to 9
move 4 from 6 to 2
move 4 from 7 to 3
move 1 from 1 to 9
move 6 from 2 to 1
move 1 from 7 to 2
move 7 from 2 to 8
move 2 from 3 to 8
move 3 from 1 to 9
move 1 from 2 to 8
move 5 from 8 to 3
move 3 from 2 to 1
move 2 from 7 to 8
move 10 from 9 to 8
move 4 from 1 to 3
move 14 from 3 to 4
move 7 from 4 to 5
move 1 from 6 to 9
move 5 from 5 to 8
move 1 from 6 to 4
move 6 from 9 to 4
move 3 from 8 to 4
move 1 from 5 to 1
move 3 from 4 to 3
move 9 from 4 to 3
move 5 from 3 to 6
move 5 from 1 to 5
move 4 from 6 to 2
move 8 from 9 to 2
move 2 from 6 to 5
move 3 from 4 to 7
move 2 from 2 to 7
move 2 from 5 to 4
move 3 from 5 to 9
move 3 from 4 to 2
move 10 from 2 to 5
move 1 from 9 to 8
move 2 from 2 to 9
move 3 from 7 to 2
move 1 from 2 to 9
move 13 from 5 to 1
move 2 from 2 to 7
move 8 from 9 to 2
move 1 from 4 to 6
move 1 from 9 to 5
move 14 from 8 to 4
move 7 from 4 to 5
move 4 from 7 to 5
move 2 from 3 to 8
move 4 from 1 to 5
move 2 from 5 to 4
move 6 from 5 to 6
move 7 from 2 to 5
move 1 from 2 to 6
move 1 from 5 to 2
move 2 from 2 to 8
move 2 from 1 to 3
move 8 from 4 to 7
move 1 from 4 to 3
move 6 from 1 to 6
move 7 from 3 to 9
move 3 from 7 to 1
move 2 from 8 to 7
move 7 from 6 to 9
move 2 from 3 to 6
move 6 from 8 to 3
move 9 from 5 to 3
move 2 from 7 to 8
move 2 from 6 to 4
move 7 from 6 to 9
move 5 from 3 to 8
move 10 from 9 to 1
move 11 from 1 to 8
move 1 from 3 to 2
move 4 from 5 to 6
move 2 from 6 to 2
move 2 from 7 to 9
move 3 from 1 to 7
move 6 from 3 to 9
move 2 from 7 to 2
move 2 from 6 to 9
move 1 from 5 to 9
move 11 from 9 to 8
move 1 from 4 to 5
move 6 from 9 to 8
move 31 from 8 to 9
move 1 from 3 to 6
move 1 from 7 to 1
move 1 from 4 to 3
move 1 from 5 to 2
move 1 from 1 to 8
move 1 from 8 to 9
move 1 from 7 to 3
move 11 from 9 to 6
move 2 from 3 to 1
move 2 from 3 to 5
move 1 from 5 to 4
move 1 from 4 to 1
move 6 from 8 to 3
move 1 from 1 to 4
move 1 from 4 to 6
move 2 from 3 to 6
move 17 from 9 to 2
move 23 from 2 to 9
move 14 from 9 to 4
move 1 from 1 to 7
move 1 from 5 to 6
move 8 from 6 to 2
move 1 from 3 to 2
move 4 from 9 to 8
move 5 from 4 to 7
move 3 from 7 to 2
move 1 from 1 to 2
move 2 from 9 to 4
move 3 from 6 to 9
move 8 from 4 to 9
move 2 from 4 to 2
move 4 from 7 to 2
move 1 from 7 to 9
move 4 from 6 to 2
move 16 from 2 to 1
move 2 from 3 to 2
move 18 from 9 to 8
move 1 from 4 to 2
move 1 from 6 to 8
move 1 from 3 to 9
move 3 from 9 to 5
move 4 from 9 to 8
move 6 from 2 to 8
move 1 from 5 to 1
move 4 from 2 to 8
move 1 from 5 to 1
move 17 from 1 to 4
move 1 from 5 to 8
move 10 from 4 to 3
move 10 from 3 to 1
move 4 from 4 to 9
move 1 from 4 to 6
move 1 from 4 to 8
move 38 from 8 to 1
move 27 from 1 to 5
move 1 from 8 to 2
move 1 from 6 to 3
move 1 from 4 to 8
move 1 from 8 to 4
move 14 from 1 to 9
move 1 from 3 to 1
move 1 from 5 to 1
move 1 from 2 to 5
move 2 from 5 to 4
move 17 from 5 to 8
move 3 from 4 to 9
move 2 from 9 to 1
move 3 from 5 to 7
move 3 from 7 to 4
move 2 from 4 to 7
move 12 from 1 to 4
move 1 from 7 to 4
move 1 from 7 to 6
move 1 from 6 to 9
move 11 from 4 to 3
move 1 from 5 to 3
move 11 from 3 to 9
move 1 from 3 to 2
move 3 from 5 to 4
move 1 from 2 to 4
move 1 from 5 to 8
move 13 from 9 to 3
move 16 from 9 to 1
move 4 from 8 to 9
move 2 from 1 to 4
move 1 from 9 to 1
move 1 from 9 to 7
move 1 from 7 to 2
move 6 from 8 to 3
move 8 from 4 to 2
move 4 from 9 to 6
move 3 from 2 to 3
move 3 from 6 to 1
move 3 from 8 to 6
move 1 from 6 to 8
move 3 from 6 to 4
move 11 from 3 to 5
move 4 from 8 to 2
move 6 from 3 to 5
move 3 from 5 to 1
move 2 from 8 to 3
move 14 from 5 to 3
move 4 from 3 to 4
move 6 from 3 to 5
move 3 from 2 to 9
move 4 from 1 to 8
move 3 from 9 to 6
move 2 from 6 to 9
move 6 from 4 to 3
move 15 from 1 to 4
move 1 from 6 to 7
move 5 from 5 to 1
move 11 from 3 to 1
move 2 from 9 to 7
move 1 from 5 to 6
move 2 from 1 to 3
move 7 from 2 to 6
move 4 from 8 to 1
move 8 from 4 to 2
move 3 from 6 to 4
move 5 from 1 to 4
move 17 from 4 to 8
move 3 from 3 to 7
move 4 from 3 to 4
move 4 from 4 to 2
move 9 from 8 to 7
move 1 from 3 to 8
move 10 from 2 to 4
move 1 from 6 to 2
move 2 from 8 to 4
move 2 from 6 to 9
move 2 from 6 to 2
move 1 from 2 to 3
move 3 from 1 to 4
move 1 from 3 to 2
move 1 from 9 to 3
move 1 from 9 to 7
move 4 from 8 to 4
move 10 from 4 to 8
move 5 from 4 to 3
move 1 from 2 to 8
move 5 from 3 to 7
move 3 from 7 to 8
move 3 from 4 to 3
move 8 from 7 to 2
move 8 from 7 to 8
move 1 from 3 to 2
move 3 from 2 to 8
move 9 from 2 to 5
move 12 from 1 to 7
move 21 from 8 to 3
move 5 from 8 to 6
move 8 from 7 to 5
move 6 from 7 to 4
move 12 from 5 to 7
move 1 from 8 to 5
move 2 from 4 to 2
move 1 from 7 to 6
move 14 from 3 to 8
move 5 from 6 to 2
move 7 from 2 to 6
move 6 from 8 to 4
move 11 from 7 to 4
move 8 from 3 to 7
move 4 from 5 to 7
move 9 from 8 to 2
move 6 from 4 to 1
move 2 from 5 to 2
move 1 from 7 to 2
move 11 from 2 to 3
move 1 from 2 to 1
move 7 from 4 to 1
move 5 from 6 to 8
move 1 from 2 to 3
move 2 from 8 to 7
move 14 from 3 to 7
move 15 from 7 to 6
move 4 from 4 to 6
move 2 from 8 to 3
move 12 from 1 to 3
move 1 from 8 to 2
move 1 from 2 to 3
move 1 from 3 to 9
move 1 from 9 to 7
move 1 from 1 to 4
move 18 from 6 to 8
move 3 from 3 to 2
move 17 from 8 to 3
move 3 from 7 to 6
move 3 from 2 to 6
move 25 from 3 to 7
move 2 from 4 to 1
move 9 from 6 to 5
move 2 from 3 to 1
move 1 from 3 to 9
move 5 from 5 to 2
move 1 from 8 to 3
move 2 from 4 to 7
move 1 from 9 to 4
move 1 from 6 to 7
move 2 from 5 to 2
move 2 from 4 to 8
move 2 from 5 to 8
move 5 from 7 to 9
move 27 from 7 to 5
move 2 from 9 to 6'''


def give_matrix() -> str:
    return '''\
[P]     [L]         [T]            
[L]     [M] [G]     [G]     [S]    
[M]     [Q] [W]     [H] [R] [G]    
[N]     [F] [M]     [D] [V] [R] [N]
[W]     [G] [Q] [P] [J] [F] [M] [C]
[V] [H] [B] [F] [H] [M] [B] [H] [B]
[B] [Q] [D] [T] [T] [B] [N] [L] [D]
[H] [M] [N] [Z] [M] [C] [M] [P] [P]
 1   2   3   4   5   6   7   8   9 '''


def parse_matrix(matrix: str) -> list[list]:
    matrix = matrix.split("\n")[:-1]
    for i, line in enumerate(matrix):
        matrix[i] = [line[idx:idx+4].strip(' ')
                     for idx in range(0, len(line) + 1, 4)]

    invert_matrix = [] 
    for tup in list(zip(*matrix[::-1])):
        invert_matrix.append([i for i in tup if i != ""])

    return invert_matrix


def handle_input() -> list[dict]:
    inp = give_inp().split("\n")

    inp_list = []
    for line in inp:
        l = line.split(' ')
        inp_list.append({
            "amount": int(l[1]),
            "old": int(l[3]) - 1,
            "new": int(l[5]) - 1
        })
    return inp_list


def make_moves(moves: list[dict]) -> str:
    matrix = give_matrix()
    matrix = parse_matrix(matrix)

    for move in moves:
        for _ in range(move["amount"]):
            matrix[move["new"]].append(matrix[move["old"]].pop(-1))

    return "".join(line[-1][1] for line in matrix)


def make_moves2(moves: list[dict]) -> str:
    matrix = give_matrix()
    matrix = parse_matrix(matrix)

    for move in moves:
        stack_part = []
        for _ in range(move["amount"]):
            stack_part.append(matrix[move["old"]].pop(-1))
        matrix[move["new"]].extend(stack_part[::-1])
    
    return "".join(line[-1][1] for line in matrix)


def main() -> None:
    moves = handle_input()
    end_result = make_moves(moves)
    print(end_result)

    end_result2 = make_moves2(moves)
    print(end_result2)


if __name__ == "__main__":
    main()
