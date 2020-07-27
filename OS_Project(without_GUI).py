import matplotlib.pyplot as plt

def FCFS(head, arr, size): 
    seek_count = 0
    distance, cur_track = 0, 0 
    x=[]
    x.append(head)
    for i in range(size): 
        cur_track = arr[i]
        distance = abs(cur_track - head) 
        seek_count += distance 
        head = cur_track
    print("Total number of seek operations of FCFS is : ",  seek_count) 
    print("Seek Sequence is") 
    for i in range(size): 
        print(arr[i])
        x.append(arr[i])   
    y=[]
    for i in range(size+1):
        y.append(i+1)
    print(y)
    print(x)
    plt.plot(x,y,'r-o')
    plt.show()
    return seek_count/size    

def calculateDifference(arra, head, diff): 
    for i in range(len(diff)): 
        diff[i][0] = abs(arra[i] - head)
        
def findMin(diff):  
    index = -1
    minimum = 999999999
    for i in range(len(diff)): 
        if (not diff[i][1] and 
                minimum > diff[i][0]): 
            minimum = diff[i][0] 
            index = i 
    return index  
      
def SSTF(head, request):              
    if (len(request) == 0):
        return
    x=[]
    l = len(request)
    diff = [0] * l
    for i in range(l):
        diff[i] = [0, 0]   
        seek_count = 0
        seek_sequence = [0] * (l + 1)       
    for i in range(l):
        seek_sequence[i] = head
        calculateDifference(request, head, diff)
        index = findMin(diff)  
        diff[index][1] = True  
        seek_count += diff[index][0]
        head = request[index]  
        seek_sequence[len(seek_sequence) - 1] = head       
    print("Total number of seek operations of SSTF is : ",  seek_count)                                                   
    print("Seek Sequence is")   
    for i in range(l + 1): 
        print(seek_sequence[i])
        x.append(seek_sequence[i])
    y=[]
    for i in range(l+1):
        y.append(i+1)
    print(y)
    print(x)
    plt.plot(x,y,'r-o')
    plt.show()        
    return seek_count/len(request)
    
def SCAN(head,reqs):
    requests = reqs.copy()
    pos = head
    start,time,end,end1,count,cl,cr=0,0,199,199,0,0,0
    x=[]
    x.append(head)
    seek_sequence = [0] * len(requests)
    for i in requests:
        if i>=head:
            cr+=1
        else:
            cl+=1
    if cr > cl:
        for i in range(pos,end+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)      
        time+=abs(pos-end)
        pos=end                              
        for i in range(end,start-1,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)        
        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            if seek_sequence[i] <= head and cou==1:
                x.append(end1)
                x.append(seek_sequence[i])
                cou+=1
            else:
                x.append(seek_sequence[i])
        y=[]
        for i in range(len(seek_sequence)+2):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
        avg_seek_time = time/n

    else:
        for i in range(pos,start-1,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        time+=abs(pos-start)
        pos=start                        
        for i in range(start,end+1,+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            if seek_sequence[i] > head and cou==1:
                x.append(0)
                x.append(seek_sequence[i])
                cou+=1
            else:
                x.append(seek_sequence[i])

        y=[]
        for i in range(len(seek_sequence)+2):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
    
        avg_seek_time = time/n
    return avg_seek_time

def C_SCAN(head,reqs):
    requests = reqs.copy()
    pos = head
    start,time,end,end1,count,cl,cr=0,0,199,199,0,0,0
    x=[]
    x.append(head)
    seek_sequence = [0] * len(requests)
    for i in requests:
        if i>=head:
            cr+=1
        else:
            cl+=1
    if cr > cl:            
        for i in range(pos,end+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        time+=abs(pos-end)
        pos=end
        temp,ans=0,0
        for i in range(start,head+1):
            if i in requests:
                temp += 1
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
                if temp == 1:
                    ans = i
        time += (ans*2)

        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            if seek_sequence[i] <= head and cou==1:
                x.append(end1)
                x.append(0)
                x.append(seek_sequence[i])
                cou+=1
            else:
                x.append(seek_sequence[i])

        y=[]
        for i in range(len(seek_sequence)+3):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
        
        avg_seek_time = time/n

    else:
        tmep=0
        for i in range(pos,start-1,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                temp=i
                requests.remove(i)
        time+=abs(pos-end)
        pos=end
        time += (temp*2)
        for i in range(end,head,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)

        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            if seek_sequence[i] > head and cou==1:
                x.append(0)
                x.append(end1)
                x.append(seek_sequence[i])
                cou+=1
                
            else:
                x.append(seek_sequence[i])

        y=[]
        for i in range(len(seek_sequence)+3):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
        
        avg_seek_time = time/n
    return avg_seek_time

def LOOK(head,reqs):
    requests = reqs.copy()
    pos = head
    start,time,end,count,cl,cr=min(requests),0,max(requests),0,0,0
    x=[]
    x.append(head)
    seek_sequence = [0] * len(requests)

    for i in requests:
        if i>=head:
            cr+=1
        else:
            cl+=1
    if cr > cl:
        for i in range(pos,end+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)      
        time+=abs(pos-end)
        pos=end                               
        for i in range(end,start-1,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
                
        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            x.append(seek_sequence[i])

        y=[]
        for i in range(len(seek_sequence)+1):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
    
        avg_seek_time = time/n

    else:
        for i in range(pos,start-1,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        time+=abs(pos-start)
        pos=start
                                
        for i in range(start,end+1,+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            x.append(seek_sequence[i])

        y=[]
        for i in range(len(seek_sequence)+1):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
    
        avg_seek_time = time/n
    return avg_seek_time

def C_LOOK(head,reqs):
    requests = reqs.copy()
    pos = head
    start,time,end,end1,count,cl,cr=0,0,199,199,0,0,0
    x=[]
    x.append(head)
    seek_sequence = [0] * len(requests)
    for i in requests:
        if i>=head:
            cr+=1
        else:
            cl+=1
    if cr > cl:            
        for i in range(pos,end+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        time+=abs(pos-end)
        pos=end
        for i in range(start,head+1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            x.append(seek_sequence[i])
        y=[]
        for i in range(len(seek_sequence)+1):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()       
        avg_seek_time = time/n

    else:
        for i in range(pos,start-1,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)
        time+=abs(pos-end)
        pos=end

        for i in range(end,head,-1):
            if i in requests:
                time+=abs(pos-i)
                pos=i
                seek_sequence[count] = i
                count += 1
                requests.remove(i)

        print("Toatal number of seek operation is :" ,time)
        print("Seek Sequence is :" )
        cou=1
        for i in range(len(seek_sequence)):
            print(seek_sequence[i])
            x.append(seek_sequence[i])

        y=[]
        for i in range(len(seek_sequence)+1):
            y.append(i+1)
        print(y)
        print(x)
        plt.plot(x,y,'r-o')
        plt.show()
        
        avg_seek_time = time/n
    return avg_seek_time

if __name__=='__main__':
    print("DISK SCHEDULING:")
    print("Provide number of I/O requests")
    #n is the number of I/O requests
    n = int(input())
    print("Provide initial position of disc arm (total cylinders=199)")
    head = int(input())
    while head > 199:
        print("!!! INVALID !!! try again")
        head = int(input())	
    print("Provide positions to visit : max is 200")
    requests = []
    for i in range(n):
        req = int(input())
        requests.append(req)
    print(requests)  
    print("Avg seek time for FCFS was ", FCFS(head,requests,len(requests)))
    print("Avg seek time for SSTF was ", SSTF(head,requests))
    print("Avg seek time for  scan was ", SCAN(head,requests))
    print("Avg seek time for  C-scan was ", C_SCAN(head,requests))
    print("Avg seek time for  look was ", LOOK(head,requests))       
    print("Avg seek time for  C-look was ", C_LOOK(head,requests))

