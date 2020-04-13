#Course work_Lakshan
#Student Version

exit=1
if exit==1:
    while exit==1:
        id= input('Enter your Student ID: ')
        p= int(input('Ener your Passed credits: '))
        d= int(input('Enter your defered credits: '))
        f= int(input('Enter your failed credits: '))

            if ((p and d and f)>=0):
                if (p+d+f)==120:
                    if (p==120 and d==0 and f==0):
                        print ('Progress')
                    elif (p==100 and d==20 and f==0):
                        print ('Progress module-trailer')
                    elif (p==100 and d==0 and f==20):
                        print ('Progress module-trailer')
                    elif (p==80 and d==40 and f==0):
                        print ('Do not Progress – module retriever')
                    elif (p==80 and d==20 and f==20):
                        print ('Do not Progress – module retriever')
                    elif (p==80 and d==0 and f==40):
                        print ('Do not Progress – module retriever')
                    elif (p==60 and d==60 and f==0):
                        print ('Do not Progress – module retriever')
                    elif (p==60 and d==40 and f==20):
                        print ('Do not Progress – module retriever')
                    elif (p==60 and d==20 and f==40):
                        print ('Do not Progress – module retriever')
                    elif (p==60 and d==0 and f==60):
                        print ('Do not Progress – module retriever')
                    elif (p==40 and d==80 and f==0):
                        print ('Do not Progress – module retriever')
                    elif (p==40 and d==60 and f==20):
                        print ('Do not Progress – module retriever')
                    elif (p==40 and d==40 and f==40):
                        print ('Do not Progress – module retriever')
                    elif (p==40 and d==20 and f==60):
                        print ('Do not Progress – module retriever')
                    elif (p==40 and d==0 and f==80):
                        print ('Exclude')
                    elif (p==20 and d==100 and f==0):
                        print ('Do not Progress – module retriever')
                    elif (p==20 and d==80 and f==20):
                        print ('Do not Progress – module retriever')
                    elif (p==20 and d==60 and f==40):
                        print ('Do not Progress – module retriever')
                    elif (p==20 and d==40 and f==60):
                        print ('Do not Progress – module retriever')
                    elif (p==20 and d==20 and f==80):
                        print ('Exclude')
                    elif (p==20 and d==0 and f==100):
                        print ('Exclude')
                    elif (p==0 and d==120 and f==0):
                        print ('Do not Progress – module retriever')
                    elif (p==0 and d==100 and f==20):
                        print ('Do not Progress – module retriever')
                    elif (p==0 and d==80 and f==40):
                        print ('Do not Progress – module retriever')
                    elif (p==0 and d==60 and f==60):
                        print ('Do not Progress – module retriever')
                    elif (p==0 and d==40 and f==80):
                        print ('Exclude')
                    elif (p==0 and d==20 and f==100):
                        print ('Exclude')
                    elif (p==0 and d==0 and f==120):
                        print ('Exclude')
                    else:
                        print ('Range error')
                else:
                    print ('Total incorrect')
                
                        
                        
                    
            
