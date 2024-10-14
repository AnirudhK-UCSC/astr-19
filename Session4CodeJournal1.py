class FavoriteAnimal:
    arm_length: float
    leg_length: float
    num_eyes: int
    tail: bool
    furry: bool
    
    def __init__(self, arm_length, leg_length, num_eyes, tail, furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.tail = tail
        self. furry = furry
    
    def __str__(self):
        out = f"Your favorite animal has arms {self.arm_length} inches long, legs {self.leg_length} inches long, {self.num_eyes} eyes"
        if(self.tail):
            out = out + " has a tail"
        else:
            out = out + " doesn't have a tail"
        if(self.furry):
            out = out + " and is furry!"
        else:
            out = out + " and isn't furry!"
        
        return out
def main():
    cat = FavoriteAnimal(9.0,9.0, 2, True, True)
    
    print(cat)
    
if __name__ == "__main__":
    main()