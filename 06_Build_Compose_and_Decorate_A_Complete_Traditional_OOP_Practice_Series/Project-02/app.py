class Counter:
    # --- class variable ---
    _count = 0    

    def __init__(self) -> None:
       
        Counter._count += 1

    # --- class method ---
    @classmethod
    def how_many(cls) -> int:
        """
        Return (and optionally print) how many Counter objects exist so far.
        Uses `cls` so it works even if the class is subclassed.
        """
       
        print(f"Counter objects created: {cls._count}")
        return cls._count


# ---- quick demo ----
if __name__ == "__main__":
    a = Counter()    
    b = Counter()     
    c = Counter()     

    Counter.how_many() 
    # → Counter objects created: 3
    # or:
    print("Total objects:", Counter.how_many())
