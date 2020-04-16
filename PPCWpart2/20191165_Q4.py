# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. # Any code taken from other sources is referenced within my code solution.
# Student ID: 20191165
# Date: 17/04/2020
#Programming Principles
#Course Work
#Staff Version

#part 4

# Test data
testdata = [["stu1",120, 0, 0],["stu2",100,20,0],["stu3",100,0,20],["stu4",80,20,20],["stu5",60,40,20],["stu6",40,40,40],["stu7",20,40,60],["stu8",20,20,80],["stu9",20,0,100],["stu10",0,0,120]]

# User defined function
def evaluateStudents(data):
    
    progressCount = 0
    progModTrailCount = 0
    progNotRetrievCount = 0
    excludeCount = 0
    count = 0

    for item in data:
        end=1
        listrange = 0
        list = [0, 20, 40, 60, 80, 100, 120]

        while end==1:
            id= item[0]

            # Check whether the inputs are integers
            try:
                passed = item[1]
                defered = item[2]
                failed = item[3]
                print(passed,defered,failed)

                #Check whether the inputs are in range
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
                            progressCount=progressCount+1
                        elif (passed==100 and defered==20 and failed==0):
                            print ('Student ID:',id,'\n','Progress module-trailer')
                            progModTrailCount=progModTrailCount+1
                        elif (passed==100 and defered==0 and failed==20):
                            print ('Student ID:',id,'\n','Progress module-trailer')
                            progModTrailCount=progModTrailCount+1
                        elif (passed==80 and defered==40 and failed==0):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==80 and defered==20 and failed==20):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==80 and defered==0 and failed==40):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==60 and defered==60 and failed==0):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==60 and defered==40 and failed==20):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==60 and defered==20 and failed==40):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==60 and defered==0 and failed==60):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==40 and defered==80 and failed==0):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==40 and defered==60 and failed==20):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==40 and defered==40 and failed==40):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==40 and defered==20 and failed==60):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==40 and defered==0 and failed==80):
                            print ('Student ID:',id,'\n','Exclude')
                            excludeCount=excludeCount+1
                        elif (passed==20 and defered==100 and failed==0):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==20 and defered==80 and failed==20):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==20 and defered==60 and failed==40):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==20 and defered==40 and failed==60):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==20 and defered==20 and failed==80):
                            print ('Student ID:',id,'\n','Exclude')
                            excludeCount=excludeCount+1
                        elif (passed==20 and defered==0 and failed==100):
                            print ('Student ID:',id,'\n','Exclude')
                            excludeCount=excludeCount+1
                        elif (passed==0 and defered==120 and failed==0):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==0 and defered==100 and failed==20):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==0 and defered==80 and failed==40):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==0 and defered==60 and failed==60):
                            print ('Student ID:',id,'\n','Do not Progress – module retriever')
                            progNotRetrievCount=progNotRetrievCount+1
                        elif (passed==0 and defered==40 and failed==80):
                            print ('Student ID:',id,'\n','Exclude')
                            excludeCount=excludeCount+1
                        elif (passed==0 and defered==20 and failed==100):
                            print ('Student ID:',id,'\n','Exclude')
                            excludeCount=excludeCount+1
                        elif (passed==0 and defered==0 and failed==120):
                            print ('Student ID:',id,'\n','Exclude')
                            excludeCount=excludeCount+1
                        count = count + 1
                    else:
                        print ('Total Incorrect')
                else:
                    print ('Range error')
            except:
                print ('Integeer Required')

    # Horizontal Histogram
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
    print("\n\n Total: ", count)

# Pass values to the function evaluateStudents()
evaluateStudents(testdata)
    
            
                    
                    
                
        

    
