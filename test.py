import queue;

def FIFO(test_file , frame_size):
    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_memory_ref_s = queue.Queue(frame_size);
    p_memory_dirty_bit = queue.Queue(frame_size);# init variable
    f = open(test_file,'r');
    list = f.readlines(); # load test file to list
    for i in list: 
        ref_s = i[0:i.find(' ')];
        dirty_bit = i[i.find(' ')+1];
        print(ref_s + " " + dirty_bit);
        if ref_s in p_memory_ref_s.queue: # if ref string in memory
            print("hit !");
            continue;
        if(p_memory_ref_s.full()): # (page fault occurs) need to select victim
            tmp = p_memory_dirty_bit.get()
            print("page fault select a victim")
            if tmp == '1': # if dirty bit is set
                write_back+=1;
                interrupt+=1;
            p_memory_ref_s.get(); # remove element from head
            p_memory_ref_s.put(ref_s); # add element to tail
            p_memory_dirty_bit.put(dirty_bit); # add element to tail
        else:# frame have space but ref isnt in memory (page fault occurs)
            p_memory_ref_s.put(ref_s);
            p_memory_dirty_bit.put(dirty_bit);
            print("page fault load into frame")
        page_fault+=1;
        interrupt+=1;
    print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

def OPTIMAL(test_file , frame_size):
    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_memory_ref_s = [];
    p_memory_dirty_bit = []; #init variable
    f = open(test_file,'r');
    list = f.readlines(); # load test file to list
    for i in range(0,len(list)):
        item = list[i];
        ref_s = item[0:item.find(' ')];
        dirty_bit = item[item.find(' ')+1];
        if ref_s in p_memory_ref_s: # check frame to see exist ref page or not if the page exist in frame doesnt need to replace 
            continue;
        else: # page fault occurs
            if(len(p_memory_ref_s)<frame_size):# frame isnt full and ref isnt exist in frame
                p_memory_ref_s.append(ref_s);
                p_memory_dirty_bit.append(dirty_bit);
            else:# frame is full need to select victim to replace
                current_index = i;
                longest_not_used_page_index = 0;
                longest_period = 0;
                for k in range(0,len(p_memory_ref_s)):
                    period = 0;
                    flag = 0;
                    print(p_memory_ref_s[k])
                    for l in range(current_index+1,len(list)):
                        period+=1;
                        tmp=list[l];
                        if(str(p_memory_ref_s[k])==tmp[0:tmp.find(" ")]):
                            flag=1;
                            break;
                    if(period==len(list)-(current_index+1) and flag==0):# isn`t exist (must be the longest not used)
                        longest_not_used_page_index = k;
                        break;
                    if(period>longest_period):
                        longest_period = period;
                        longest_not_used_page_index = k;
                if(p_memory_dirty_bit[longest_not_used_page_index]=='1'):# victim dirty bit is set
                    write_back+=1;
                    interrupt+=1;
                p_memory_dirty_bit[longest_not_used_page_index] = dirty_bit;
            page_fault+=1;
            interrupt+=1;
    print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

OPTIMAL("test.txt",5);
#FIFO("test.txt",5);
