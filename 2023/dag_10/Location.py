class Location:
    def __init__(self, location: tuple[int, int], symbol: str) -> None:
        self.location = location
        self.symbol = symbol
        self.pipe_on_loc = False
        
    def get(self) -> tuple[tuple[int, int], str]:
        return (self.location, self.symbol)
    
    def __eq__(self, __value: object) -> bool:
        return self.get() == __value.get()
    
    def __repr__(self) -> str:
        return str(self.symbol)
    