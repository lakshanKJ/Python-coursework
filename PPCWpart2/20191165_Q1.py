# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. # Any code taken from other sources is referenced within my code solution.
# Student ID: 20191165
# Date: 17/04/2020
#Course work_Lakshan
#Student Version

# Part 1

end=1
listrange = 0
list = [0, 20, 40, 60, 80, 100, 120]

while end==1:
    id= input('Please enter the Student ID: ')

    # Check whether the inputs are integers
    try:
        passed = int(input('PASSED CREDITS: ') or "0")
        defered = int(input('DEFERED CREDITS: ') or "0")
        failed = int(input('FAILED CREDITS: ') or "0")
        
        #Check whether the inputs are within the range
        if passed in list:
            if defered in list:
                if failed in list:
                    listrange = 1
        if (1 == listrange):

            #Check whether the total is correct
            if (passed+defered+failed)==120:
                end=0
                if (passed==120 and defered==0 and failed==0):
                    print ('Student ID:',id,'\n','Progress')
                elif (passed==100 and defered==20 and failed==0):
                    print ('Student ID:',id,'\n','Progress module-trailer')
                elif (passed==100 and defered==0 and failed==20):
                    print ('Student ID:',id,'\n','Progress module-trailer')
                elif (passed==80 and defered==40 and failed==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==80 and defered==20 and failed==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==80 and defered==0 and failed==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==60 and defered==60 and failed==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==60 and defered==40 and failed==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==60 and defered==20 and failed==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==60 and defered==0 and failed==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==40 and defered==80 and failed==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==40 and defered==60 and failed==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==40 and defered==40 and failed==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==40 and defered==20 and failed==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==40 and defered==0 and failed==80):
                    print ('Student ID:',id,'\n','Exclude')
                elif (passed==20 and defered==100 and failed==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==20 and defered==80 and failed==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==20 and defered==60 and failed==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==20 and defered==40 and failed==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==20 and defered==20 and failed==80):
                    print ('Student ID:',id,'\n','Exclude')
                elif (passed==20 and defered==0 and failed==100):
                    print ('Student ID:',id,'\n','Exclude')
                elif (passed==0 and defered==120 and failed==0):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==0 and defered==100 and failed==20):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==0 and defered==80 and failed==40):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==0 and defered==60 and failed==60):
                    print ('Student ID:',id,'\n','Do not Progress – module retriever')
                elif (passed==0 and defered==40 and failed==80):
                    print ('Student ID:',id,'\n','Exclude')
                elif (passed==0 and defered==20 and failed==100):
                    print ('Student ID:',id,'\n','Exclude')
                elif (passed==0 and defered==0 and failed==120):
                    print ('Student ID:',id,'\n','Exclude')
            else:
                print ('Total Incorrect')
        else:
            print ('Range error')
    except:
        print ('Integeer Required')
    
    
            
                    
                    
                
        
