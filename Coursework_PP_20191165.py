#Course work_Lakshan
#Student Version

exit=1
if exit==1:
    while exit==1:
        id= input('Enter your Student ID: ')
        try:
            p = int(input('PASSED CREDITS: ') or "0")
            d = int(input('DEFERED CREDITS: ') or "0")
            f = int(input('FAILED CREDITS: ') or "0")
            
            if (p+d+f)==120:
                exit=0
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
                    print ('Range error')
            else:
                print ('Total incorrect')
        except:
            print ('Integeer Required')
        
                
                        
                        
                    
            
