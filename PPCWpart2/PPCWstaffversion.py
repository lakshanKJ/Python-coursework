#Programming Principles
#Course Work
#Staff Version

quitStatus = 1
count = 0
progressCount = 0
progModTrailCount = 0
progNotRetrievCount = 0
excludeCount = 0

while "q" != quitStatus:
    end=1
    listrange = 0
    list = [0, 20, 40, 60, 80, 100, 120]

    while end==1:
        id= input('Please enter the Student ID: ')

        try:   # Check whether the inputs are integers
            p = int(input('PASSED CREDITS: ') or "0")
            d = int(input('DEFERED CREDITS: ') or "0")
            f = int(input('FAILED CREDITS: ') or "0")
            #Check whether the inputs are in range
            if p in list:
                if d in list:
                    if f in list:
                        listrange = 1
            if (1 == listrange):

                if (p+d+f)==120:  #Check whether the total is correct
                    end=0
                    if (p==120 and d==0 and f==0):
                        print ('Student ID:',id,'\n','Progress')
                        progressCount=progressCount+1
                    elif (p==100 and d==20 and f==0):
                        print ('Student ID:',id,'\n','Progress module-trailer')
                        progModTrailCount=progModTrailCount+1
                    elif (p==100 and d==0 and f==20):
                        print ('Student ID:',id,'\n','Progress module-trailer')
                        progModTrailCount=progModTrailCount+1
                    elif (p==80 and d==40 and f==0):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==80 and d==20 and f==20):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==80 and d==0 and f==40):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==60 and d==60 and f==0):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==60 and d==40 and f==20):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==60 and d==20 and f==40):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==60 and d==0 and f==60):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        progNotRetrievCount=progNotRetrievCount+1
                    elif (p==40 and d==80 and f==0):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==40 and d==60 and f==20):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==40 and d==40 and f==40):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==40 and d==20 and f==60):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==40 and d==0 and f==80):
                        print ('Student ID:',id,'\n','Exclude')
                        excludeCount=excludeCount+1
                    elif (p==20 and d==100 and f==0):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==20 and d==80 and f==20):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==20 and d==60 and f==40):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==20 and d==40 and f==60):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==20 and d==20 and f==80):
                        print ('Student ID:',id,'\n','Exclude')
                        excludeCount=excludeCount+1
                    elif (p==20 and d==0 and f==100):
                        print ('Student ID:',id,'\n','Exclude')
                        excludeCount=excludeCount+1
                    elif (p==0 and d==120 and f==0):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==0 and d==100 and f==20):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==0 and d==80 and f==40):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==0 and d==60 and f==60):
                        print ('Student ID:',id,'\n','Do not Progress – module retriever')
                        y=y+1
                    elif (p==0 and d==40 and f==80):
                        print ('Student ID:',id,'\n','Exclude')
                        excludeCount=excludeCount+1
                    elif (p==0 and d==20 and f==100):
                        print ('Student ID:',id,'\n','Exclude')
                        excludeCount=excludeCount+1
                    elif (p==0 and d==0 and f==120):
                        print ('Student ID:',id,'\n','Exclude')
                        excludeCount=excludeCount+1
                    count = count + 1
                    #print("count",count)
                else:
                    print ('Total Incorrect')
            else:
                print ('Range error')
        except:
            print ('Integeer Required')
    quitStatus = input("Press Enter to Continue / 'q' to Quit ")

print ("\n Progress \t",progressCount,end =": ")
for i in range(progressCount):
    print("*", end ="")
print ("\n Trailing \t",progModTrailCount,end =": ")
for i in range(progModTrailCount):
    print("*", end ="")
print ("\n Retriever \t",progNotRetrievCount,end =": ")
for i in range(progNotRetrievCount):
    print("*", end ="")
print ("\n Exclude \t",excludeCount,end =": ")
for i in range(excludeCount):
    print("*", end ="")

        
            


    
    
    
            
                    
                    
                
        

    
