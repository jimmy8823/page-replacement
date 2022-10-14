from generator_refstring import generator_refstring_locality,generator_refstring_random, generator_refstring_self;
from page_replacement import ESC, FIFO, OPTIMAL, OPTIMAL_improve, OPTIMAL_table, RANDOM;

def main():
    generator_refstring_random();
    generator_refstring_locality();
    generator_refstring_self();
    """for i in range(1,11): # simulate with random test in memory size 10 20 30 40....100
        FIFO("test/random.txt",i*10,"FIFO_random.txt");
        ESC("test/random.txt",i*10,"ESC_random.txt");
        OPTIMAL_table("test/random.txt",i*10,"OPT_random.txt");
        RANDOM("test/random.txt",i*10,"RND_random.txt");
        OPTIMAL_improve("test/random.txt",i*10,"OPTimprove_random.txt")
    for i in range(1,11): # simulate with locality test in memory size 10 20 30 40....100
        FIFO("test/locality.txt",i*10,"FIFO_locality.txt");
        ESC("test/locality.txt",i*10,"ESC_locality.txt");
        OPTIMAL_table("test/locality.txt",i*10,"OPT_locality.txt");
        RANDOM("test/locality.txt",i*10,"RND_locality.txt");
        OPTIMAL_improve("test/locality.txt",i*10,"OPTimprove_locality.txt")"""
    for i in range(1,11): # simulate with mix test in memory size 10 20 30 40....100
        FIFO("test/mix.txt",i*10,"FIFO_mix.txt");
        ESC("test/mix.txt",i*10,"ESC_mix.txt");
        OPTIMAL_table("test/mix.txt",i*10,"OPT_mix.txt");
        RANDOM("test/mix.txt",i*10,"RND_mix.txt");
        OPTIMAL_improve("test/mix.txt",i*10,"OPTimprove_mix.txt")
main()