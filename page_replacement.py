from asyncore import write
import queue;

def FIFO(test_file , frame_size):
    page_fault = 0;
    interrupt = 0;
    write_back = 0; 
    p_memory_ref_s = queue.Queue(frame_size);
    p_memory_dirty_bit = queue.Queue(frame_size);
    f = open(test_file,'r');
    list = f.readlines(); # load test file to list
    for i in list:  
        index = i.find(' ');
        end = i.find('\n');
        ref_s = i[0:index];
        dirty_bit = i[index:end];
        if ref_s in p_memory_ref_s.queue: # if ref string in memory
            continue;
        if(p_memory_ref_s.full()): # (page fault occurs) need to select victim
            tmp = p_memory_dirty_bit.get()
            if tmp==1:
                write_back+=1; 
                interrupt+=1;
            p_memory_ref_s.get();
        else:# frame have space but ref isnt in memory (page fault occurs)
            p_memory_ref_s.put(ref_s);
            p_memory_dirty_bit.put(dirty_bit);
        page_fault+=1;
        interrupt+=1;
    print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

#def OPTIMAL():