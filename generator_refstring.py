from os.path import exists
from random import randint
# ref string 1-600 ; memory reference 180,000
def generator_refstring_random():
    m_ref = 180000;
    if(exists("test/random.txt")):# if test already exitst
        return;
    f = open("test/random.txt", "a");
    while(m_ref>0):
        ref_s = randint(1,600);
        dirty_bit = randint(0,1);
        ref_bit = randint(0,1);
        f.write(str(ref_s) + " " + str(dirty_bit) + str(ref_bit) +  "\n");
        m_ref-=1;
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
            ref_bit = randint(0,1);
            f.write(str((ref_s+i)%600) + " " + str(dirty_bit) + str(ref_bit) + "\n");
        m_ref-=func_str_length;
    f.close();

def generator_refstring_self():
    m_ref = 180000;
    if(exists("test/self_create.txt")):# if test already exitst
        return;
    f = open("test/self_create.txt", "a");
    while(m_ref>0):
        ref_in_a_row_len = randint(1,10);
        ref_s = randint(1,600);
        for i in range(0,ref_in_a_row_len+1):
            dirty_bit = randint(0,1);
            ref_bit = randint(0,1);
            f.write(str((ref_s+i)%600) + " " + str(dirty_bit) + str(ref_bit) +  "\n");
        m_ref-=ref_in_a_row_len;
    f.close();