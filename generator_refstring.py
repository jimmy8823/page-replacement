from os.path import exists
from random import randint
# ref string 1-600 ; memory reference 180,000
def generator_refstring_random():
    m_ref = 180000;
    if(exists("test/random.txt")):# if test already exitst
        return;
    f = open("test/random.txt", "a");
    while(m_ref>0):
        continue_ref_length = randint(1,10);# to reduce random time
        ref_s = randint(1,600);
        dirty_bit = randint(0,1);
        for i in range(0,continue_ref_length+1):
            f.write(str(ref_s+i) + " " + str(dirty_bit) + "\n");
        m_ref-=continue_ref_length;
    f.close();

def generator_refstring_locality():# subset 1/40 
    m_ref = 180000;
    if(exists("test/locality.txt")):# if test already exitst
        return;
    f = open("test/locality.txt", "a");
    while(m_ref>0):
        subset = randint(1,600);
        subset_min = subset-7;
        subset_max = subset+7;
        func_str_length = randint(30,50);
        for i in range(0,func_str_length):
            ref_s = randint(subset_min,subset_max);
            dirty_bit = ref_s%2;
            f.write(str(ref_s+i) + " " + str(dirty_bit) + "\n");
        m_ref-=func_str_length;
    f.close();

#def generator_refstring_self():
