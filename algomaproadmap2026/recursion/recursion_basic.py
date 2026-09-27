class Recursion:

    def walk(self, steps: int):
        if steps == 0:
            return
        
        self.walk(steps - 1)
        print(f"steps: {steps}")

if __name__ == "__main__":
    recursion = Recursion()
    print(recursion.walk(5))
    
    