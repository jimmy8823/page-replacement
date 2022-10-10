from generator_refstring import generator_refstring_locality,generator_refstring_random;
from page_replacement import FIFO, OPTIMAL;

def main():
    generator_refstring_random();
    generator_refstring_locality();
    """for i in range(1,11): # simulate FIFO with random test in memory size 10 20 30 40....100
        print("(random test)frame size: " + str(i*10));
        OPTIMAL("test/random.txt",i*10);"""
    print("(locality test)frame size: " + str(100));
    FIFO("test/locality.txt",100);
main()