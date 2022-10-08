from generator_refstring import generator_refstring_locality,generator_refstring_random;
from page_replacement import FIFO;

def main():
    generator_refstring_random();
    generator_refstring_locality();
    for i in range(1,10):
        print("frame size: " + str(i));
        FIFO("test/random.txt",i*10);

main()