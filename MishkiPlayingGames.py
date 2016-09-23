nsets, ndays = input().split()

sets = input().split()

'''
    4 2 3
    day1 => m => 4/2 = 2, h=>2/2=1, m=>0, h=>?
         => h=>2/1 =1,m=>0, h=>?
         m wins
    day 2 => m => 2/2 =1, h=>0, m=>?
          => m=>3/2=1,h=>0, m=>?
          h wins
'''

for day in range(0,len(ndays)):
    #day[0]
    m = h =0    
    
    m = int(sets[day])
    while 1:
        it = 0             
        m = m/2
        
        if(m == 0):            
            h = int(int(sets[day+1])/2)            
            m = h/2
            it+=1
        else:
            h = m/2

        if(h == 0):           
            m = int(int(sets[day+1])/2)
            h = m/2
            it+=1
        else:
            m = h/2

        print(it)
        if(it == 1):
            if(m==0):
                print("Mishki")
            else:
                if (h == 0):
                    print("Hacker")
            break
    
