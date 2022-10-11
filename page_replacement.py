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
        dirty_bit = i[i.find(' ')+2];
        if ref_s in p_memory_ref_s.queue: # if ref string in memory
            continue;
        if(p_memory_ref_s.full()): # (page fault occurs) need to select victim
            tmp = p_memory_dirty_bit.get()
            if int(tmp)==1: # if dirty bit is set
                write_back+=1;
                interrupt+=1;
            p_memory_ref_s.get(); # remove element from head
            p_memory_ref_s.put(ref_s); # add element to tail
            p_memory_dirty_bit.put(dirty_bit); # add element to tail
        else:# frame have space but ref isnt in memory (page fault occurs)
            p_memory_ref_s.put(ref_s);
            p_memory_dirty_bit.put(dirty_bit);
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
        dirty_bit = item[item.find(' ')+2];
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
                p_memory_ref_s[longest_not_used_page_index] = ref_s;
            page_fault+=1;
            interrupt+=1;
    print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

def ESC(test_file,frame_size):
    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_memory_ref_s = [];
    p_memory_dirty_bit = []; 
    p_memory_ref_bit = []; #init variable
    f = open(test_file,'r');
    list = f.readlines(); # load test file to list
    for i in list:
        offset = i.find(' ');
        ref_s = i[0:offset];
        ref_bit = i[offset+1];
        dirty_bit = i[offset+2];
        if ref_s in p_memory_ref_s: # check frame to see exist ref page or not if the page exist in frame doesnt need to replace 
            continue;
        else: # page fault
            if(len(p_memory_ref_s)<frame_size):
                p_memory_ref_s.append(ref_s);
                p_memory_dirty_bit.append(dirty_bit);
                p_memory_ref_bit.append(ref_bit);
            else: # need to page replacement
                tmp_best_page_to_replace = -1;
                tmp_best_page_priority = 0;
                for j in range(0,len(p_memory_ref_s)):# check all page in memory their priority
                    priority = 0;
                    if(p_memory_ref_bit=='0'):
                        if(p_memory_dirty_bit=='0'): # pair 0,0
                            priority = 4;
                        else: # pair 0,1
                            priority = 3;
                    else:
                        if(p_memory_dirty_bit=='0'): # pair 1,0
                            priority = 2;
                        else: # pair 1,1
                            priority = 1;
                    if(priority>tmp_best_page_priority):
                        tmp_best_page_to_replace = j;
                        tmp_best_page_priority = priority;
                    if(tmp_best_page_priority==4): #found the best page to replace
                        break;
                if(p_memory_dirty_bit[tmp_best_page_to_replace]=='1'):
                    interrupt += 1;
                    write_back += 1;
                p_memory_ref_bit[tmp_best_page_to_replace] = ref_bit; # replace page
                p_memory_dirty_bit[tmp_best_page_to_replace] = dirty_bit;
                p_memory_ref_s[tmp_best_page_to_replace] = ref_s;
                page_fault+=1;
                interrupt+=1;
    print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

#def self():