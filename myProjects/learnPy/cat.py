#for _ in range(10):
#    print("meow")


#print("meow\n" * 3, end="")

def main():
    meow(2)

def meow(n):
    for _ in range(n):
        print("meow")
    
def get_number():
        while True:
            n = int(input("What's n? "))
            if n > 0:
                break
            return n

main()