import queue
from random import randint

def FIFO(test_file , frame_size , output):
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
    output = "result/" + output;
    result =str(frame_size)+ " " + str(page_fault) + " " +str(interrupt) + " " + str(write_back)+"\n";
    writr_file(output,result);
    #print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
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
    result =str(frame_size)+ " " + str(page_fault) + " " +str(interrupt) + " " + str(write_back)+"\n";
    f.close();

def ESC(test_file,frame_size,output):
    class frame:
        def __init__(self, ref_s, ref_bit, dirty_bit):
            self.ref_string = ref_s;
            self.ref_bit = ref_bit;
            self.dirty_bit = dirty_bit;

    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_frame=[]; #init variable
    f = open(test_file,'r');
    list = f.readlines(); # load test file to list
    for i in list:
        offset = i.find(' ');
        ref_s = i[0:offset];
        ref_bit = i[offset+1];
        dirty_bit = i[offset+2];
        hit = 0;
        for k in range(0,len(p_frame)):
            if (ref_s == p_frame[k].ref_string): # check frame to see exist ref page or not if the page exist in frame doesnt need to replace 
                hit = 1;
                break;
        if(hit==0): # page fault
            if(len(p_frame)<frame_size):
                p_frame.append(frame(ref_s,ref_bit,dirty_bit));
            else: # need to page replacement
                tmp_best_page_to_replace = -1;
                tmp_best_page_priority = 0;
                for j in range(0,len(p_frame)):# check all page in memory their priority
                    priority = 0;
                    if(p_frame[j].ref_bit=='0'):
                        if(p_frame[j].dirty_bit=='0'): # pair 0,0
                            priority = 4;
                        else: # pair 0,1
                            priority = 3;
                    else:
                        if(p_frame[j].dirty_bit=='0'): # pair 1,0
                            priority = 2;
                        else: # pair 1,1
                            priority = 1;
                    if(priority>tmp_best_page_priority):
                        tmp_best_page_to_replace = j;
                        tmp_best_page_priority = priority;
                    if(tmp_best_page_priority==4): #found the best page to replace
                        break;
                if(p_frame[tmp_best_page_to_replace].dirty_bit=='1'):
                    interrupt += 1;
                    write_back += 1;
                p_frame[tmp_best_page_to_replace] = frame(ref_s,ref_bit,dirty_bit); # replace page
            page_fault+=1;
            interrupt+=1;
    output = "result/" + output;
    result =str(frame_size)+ " " + str(page_fault) + " " +str(interrupt) + " " + str(write_back)+"\n";
    writr_file(output,result);
    #print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

def OPTIMAL_table(test_file , frame_size , output):
    class frame:
        def __init__(self, ref_s, ref_bit, dirty_bit,period:int):
            self.ref_string = ref_s;
            self.ref_bit = ref_bit;
            self.dirty_bit = dirty_bit;
            self.period = period;

    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_frame = [];
    f = open(test_file,'r');
    list = f.readlines();
    for i in range(0,len(list)):
        element = list[i];
        ref_s = element[0:element.find(" ")];
        dirty_bit = element[element.find(" ")+2];
        period = count_next_appear_period(i,list,ref_s);
        in_frame = 0;
        hit_index = -1;
        for j in range(0,len(p_frame)):
            item = p_frame[j]
            if(item.ref_string==ref_s):
                in_frame = 1;
                hit_index = j;
                break;
        if(in_frame==0): #if page not in frame
            page_fault+=1;
            interrupt+=1;
            if(len(p_frame)<frame_size): # if p_frame not full
                p_frame.append(frame(ref_s , 0 , dirty_bit, period)); # add to p_frame
            else: #page replacement
                victim_index = -1;
                longest_period = 0;
                for k in range(0,len(p_frame)):
                    if( p_frame[k].period > longest_period):
                        longest_period = p_frame[k].period;
                        victim_index = k;
                if(p_frame[victim_index].dirty_bit=='1'): #check whether victim dirty bit is set
                    interrupt+=1;
                    write_back+=1;
                p_frame[victim_index] = frame(ref_s,0,dirty_bit,period); # replace
        else: # hit
            p_frame[hit_index].period = period # hit still need to update period
    output = "result/" + output;
    result =str(frame_size)+ " " + str(page_fault) + " " +str(interrupt) + " " + str(write_back)+"\n";
    writr_file(output,result);
    #print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

def OPTIMAL_improve(test_file , frame_size , output):
    class frame:
        def __init__(self, ref_s, ref_bit, dirty_bit,period:int):
            self.ref_string = ref_s;
            self.ref_bit = ref_bit;
            self.dirty_bit = dirty_bit;
            self.period = period;

    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_frame = [];
    f = open(test_file,'r');
    list = f.readlines();
    for i in range(0,len(list)):
        element = list[i];
        ref_s = element[0:element.find(" ")];
        dirty_bit = element[element.find(" ")+2];
        period = count_next_appear_period_for_opt_improve(i,list,ref_s);
        in_frame = 0;
        hit_index = -1;
        for j in range(0,len(p_frame)):
            item = p_frame[j]
            if(item.ref_string==ref_s):
                in_frame = 1;
                hit_index = j;
                break;
        if(in_frame==0): #if page not in frame
            page_fault+=1;
            interrupt+=1;
            if(len(p_frame)<frame_size): # if p_frame not full
                p_frame.append(frame(ref_s , 0 , dirty_bit, period)); # add to p_frame
            else: #page replacement
                victim_index = -1;
                longest_period = 0;
                for k in range(0,len(p_frame)):
                    if( p_frame[k].period > longest_period):
                        longest_period = p_frame[k].period;
                        victim_index = k;
                if(p_frame[victim_index].dirty_bit=='1'): #check whether victim dirty bit is set
                    interrupt+=1;
                    write_back+=1;
                p_frame[victim_index] = frame(ref_s,0,dirty_bit,period); # replace
        else: # hit
            p_frame[hit_index].period = period # hit still need to update period
    output = "result/" + output;
    result =str(frame_size)+ " " + str(page_fault) + " " +str(interrupt) + " " + str(write_back)+"\n";
    writr_file(output,result);
    #print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();

def count_next_appear_period(index , list , ref_s):
    period = 0;
    for i in range(index+1,len(list)):
        item = list[i];
        period+=1;
        if (item[0:item.find(" ")] == ref_s):
            return period;
    return 200000; # return 200 000 if didnt find in list

def count_next_appear_period_for_opt_improve(index , list , ref_s):
    period = 0;
    for i in range(index+1,len(list)):
        item = list[i];
        period+=1;
        if (item[0:item.find(" ")] == ref_s):
            return period;
        if(period > 500):
            break;
    return 200000; # return 200 000 if didnt find in list

def RANDOM(test_file , frame_size , output):
    class frame:
        def __init__(self, ref_s, ref_bit, dirty_bit):
            self.ref_string = ref_s;
            self.ref_bit = ref_bit;
            self.dirty_bit = dirty_bit;
    page_fault = 0;
    interrupt = 0;
    write_back = 0;
    p_frame = [];
    f = open(test_file,'r');
    list = f.readlines();
    for i in list:
        ref_s = i[0:i.find(" ")];
        dirty_bit = i[i.find(" ")+2];
        hit = 0;
        for j in range(0,len(p_frame)):
            if(p_frame[j].ref_string == ref_s):# hit 
                hit = 1;
                break;
        if(hit == 0): # page fault
            if(len(p_frame)<frame_size):
                p_frame.append(frame(ref_s,0,dirty_bit));
            else:
                vitcim_pg_index = randint(0,len(p_frame)-1);
                if(p_frame[vitcim_pg_index].dirty_bit=='1'):
                    write_back+=1;
                    interrupt+=1;
                p_frame[vitcim_pg_index] = frame(ref_s,0,dirty_bit);
            page_fault+=1;
            interrupt+=1;
    output = "result/" + output;
    result =str(frame_size)+ " " + str(page_fault) + " " +str(interrupt) + " " + str(write_back)+"\n";
    writr_file(output,result);
    #print(str(page_fault) + " " +str(interrupt) + " " + str(write_back));
    f.close();
        
def writr_file(output , string):
    o = open(output, "a");
    o.write(string);
    o.close();