total = (lambda lines: sum((__import__("functools").reduce((int.__mul__, int.__add__)[("".join(lines[-1]).split())[i] != "*"], line)) for i, line in enumerate([map(int, x.split()) for x in " ".join("".join(c).strip() for c in zip(*lines[:-1])).split("  ") if x]))) ( [list(l) for l in open("input.txt") if l.strip() != ""] )
print(total)

# or the formatted, readable version:
total = (
    lambda lines: sum(
        (
            __import__("functools").reduce(
                (int.__mul__, int.__add__)[("".join(lines[-1]).split())[i] != "*"], line
            )
        )
        for i, line in enumerate(
            [
                map(int, x.split())
                for x in " ".join("".join(c).strip() for c in zip(*lines[:-1])).split(
                    "  "
                )
                if x
            ]
        )
    )
)([list(l) for l in open("input.txt") if l.strip() != ""])
print(total)
