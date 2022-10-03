class Random():
    def __init__(self, seed):
        self.seed = seed
    def seed_multiplier(self, multiplier):
        product = str(self.seed * multiplier).zfill(8)
        randn = product[-6:-2]
        
        yield randn
        # print(self.format(multiplier, product, randn))
        
        self.seed_multiplier(int(product[-4:]))
    def format(self, multiplier, product, randn):
        return f'{self.seed}\t{multiplier}\t{product}\t{randn}'
    
    
class SeedMultiplierRandom():
    def __init__(self, seed, multiplier, t=10) -> None:
        self.seed = seed
        self.multiplier = multiplier
        self.t = t
    def __iter__(self):
        return self
    
    def next(self):
        if self.t == 0:
            raise StopIteration
        
        product = str(self.seed * self.multiplier).zfill(8)
        self.multiplier = int(product[-4:])
        
        self.t -= 1
        return product[-6:-2]
    
    
if __name__ == '__main__':
    rand = Random(5673)
    u = 0
    for i in rand.seed_multiplier(1234):
        print(i)
        u += 1
        if (u > 10):
            break