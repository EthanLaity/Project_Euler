def main():
    try:
        for c in range(3,998):
            for b in range(2,c):
                for a in range(1,b):
                    while (a**2 + b**2 == c**2) and (a + b + c == 1000):
                        raise StopIteration
    except StopIteration:
        print("The set of three natural numbers, representing a Pythagorean triplet, is {{{}, {}, {}}}, where a = {}, b = {}, c = {}. The product is abc = {}.".format(a, b, c, a, b, c, a*b*c))
        
if __name__ == "__main__":
    main()
