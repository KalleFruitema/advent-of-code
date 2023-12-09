from Maprange import Maprange


class Seedrange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.length = end - start + 1
        
    def map(self, maprange: Maprange):
        ...
        
    def index(self, value: int) -> int:
        if self.start <= value <= self.end:
            return value - self.start
        raise IndexError(f"Value '{value}' not in {self.__repr__()}")
    
    def __len__(self) -> int:
        return self.length
    
    def __getitem__(self, index: int) -> int:
        if index > self.end:
            raise IndexError(f"Index '{index}' out of {self.__repr__()}")
        if index >= 0:
            return self.start + index
        else:
            return self.end + index + 1
    
    def __repr__(self) -> str:
        return f"Seedrange({self.start}, {self.end})"
    
if __name__ == "__main__": 
    sr = Seedrange(5, 15)

    print(sr)
    print(sr[5])
    print(sr[-1])
    print(sr.index(10))
    print(len(sr))

    sr2 = Seedrange(50, 100)
    print(sr2)
    print(sr2[5])
    print(len(sr2))

    print((10 - 1) // 3)
    