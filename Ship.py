class Ship:
    
    def __init__(self) -> None:
        
        self._hp = 3
        self._coords = [380, 760]
        self.acc = 0
        
    @property
    def hp(self): return self._hp
    @hp.setter
    def hp(self, val: int): self._hp = val
    
    @property
    def coords(self): return self._coords
    @coords.setter
    def coords(self, xy: list[int]): self._coords = xy
    
    def left(self):
        if self._coords[0] > 0:
            self.acc -= 1
            self._coords[0] += self.acc
        else:
            self._coords[0] = 0
    def right(self):
        if self._coords[0] < 801:
            self.acc += 1
            self._coords[0] += self.acc
    def slow(self):
        self.acc = 0
        self._coords[0] = self.acc