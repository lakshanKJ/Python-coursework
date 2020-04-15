#Course work_Lakshan
#Student Version

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
                elif (p==100 and d==20 and f==0):
                    print ('Student ID:',id,'\n','Progress module-trailer')
                elif (p==100 and d==0 and f==20):
                    print ('Student ID:',id,'\n','Progress module-trailer')
                elif (p==80 and d==40 and f==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==80 and d==20 and f==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==80 and d==0 and f==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==60 and d==60 and f==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==60 and d==40 and f==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==60 and d==20 and f==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==60 and d==0 and f==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==40 and d==80 and f==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==40 and d==60 and f==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==40 and d==40 and f==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==40 and d==20 and f==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==40 and d==0 and f==80):
                    print ('Student ID:',id,'\n','Exclude')
                elif (p==20 and d==100 and f==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==20 and d==80 and f==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==20 and d==60 and f==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==20 and d==40 and f==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==20 and d==20 and f==80):
                    print ('Student ID:',id,'\n','Exclude')
                elif (p==20 and d==0 and f==100):
                    print ('Student ID:',id,'\n','Exclude')
                elif (p==0 and d==120 and f==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==0 and d==100 and f==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==0 and d==80 and f==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==0 and d==60 and f==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (p==0 and d==40 and f==80):
                    print ('Student ID:',id,'\n','Exclude')
                elif (p==0 and d==20 and f==100):
                    print ('Student ID:',id,'\n','Exclude')
                elif (p==0 and d==0 and f==120):
                    print ('Student ID:',id,'\n','Exclude')
            else:
                print ('Total Incorrect')
        else:
            print ('Range error')
    except:
        print ('Integeer Required')
    
    
            
                    
                    
                
        
