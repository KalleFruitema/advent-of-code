from Seedrange import Seedrange


class Maprange:
    def __init__(self, destination_start: int, source_start: int,
                 length: int) -> None:
        self.dest_start = destination_start
        self.src_start = source_start
        self.length = length
        self.dest_end = destination_start + length - 1
        self.src_end = source_start + length - 1
        
    def intersect(self, seedrange: Seedrange):
        intersect = Seedrange(max(self.src_start, seedrange.start), 
                              min(self.src_end, seedrange.end))
        if intersect:
            unused = []
            dest_intersect = Seedrange(self.dest_start + (intersect[0] - self.src_start),
                                       self.dest_end + (intersect[-1] + self.src_end))
            if seedrange.check_if_in(self):
                return unused, dest_intersect
            if self.src_get(0) >= intersect[0]:
                unused.append(Seedrange(intersect[-1] + 1))
            return unused, dest_intersect
        else:
            return [seedrange], None
        
    def dest_index(self, value: int) -> int:
        if self.dest_start <= value <= self.dest_end:
            return value - self.dest_start
        raise IndexError(f"Value '{value}' not in {self.__repr__()}")
    
    def src_index(self, value: int) -> int:
        if self.src_start <= value <= self.src_end:
            return value - self.src_start
        raise IndexError(f"Value '{value}' not in {self.__repr__()}")
    
    def __len__(self) -> int:
        return self.length
    
    def dest_get(self, index: int) -> int:
        if index > self.dest_end:
            raise IndexError(f"Index '{index}' out of {self.__repr__()}")
        if index >= 0:
            return self.dest_start + index
        else:
            return self.dest_end + index + 1
        
    def src_get(self, index: int) -> int:
        if index > self.src_end:
            raise IndexError(f"Index '{index}' out of {self.__repr__()}")
        if index >= 0:
            return self.src_start + index
        else:
            return self.src_end + index + 1
    
    def __repr__(self) -> str:
        return f"Maprange(dest:({self.dest_start}, {self.dest_end}) "\
               f"src:({self.src_start}, {self.src_end}))"
               
               
if __name__ == "__main__":
    print(len(range(50, 100)))
    mr = Maprange(25, 50, 50)
    print(mr)
    print(mr.src_get(-1))