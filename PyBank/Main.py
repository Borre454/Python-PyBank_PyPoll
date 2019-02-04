import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #d_reader = csv.DictReader(csvfile)
   # print(csvreader)
    
    #Header
    csv_header = next(csvreader)
    print('Financial Analysis')
    print('------------------------------')


    #Net Total Profit/Losses
    list1 = []
    list2 = []
    count = 0
    p_n = 0
    change = 0
    diff = []
    incr = []
    incrVal = 0
    decrVal = 0
    decr = []
    incrValIndex = 0
    decrValIndex = 0


    for row in csvreader:
        
        p_n += int(row[1]) #added net totals
        list1.append(row[0])
        list2.append(int(row[1]))
        if(count > 0):
            incr_temp = list2[count] - list2[count-1]
           
            #incr.append(incr_temp)
            if(incr_temp > incrVal):
                incrVal = incr_temp
                incrValIndex = count 
            if(incr_temp < decrVal):
                decrVal = incr_temp
                decrValIndex = count    

            
           # if(list2[count] > incr):
           # incr = [count]

            #change += (list2[count] - list2[count-1]) / count
            #change /= count

        #if(list2[count] > incr):
         #   incr = list2[count]


        count += 1 #count number of rows
            
        
        

    print("Total Months: " + str(count))
    print("Net Total: $" + str(p_n))
    #print(p_n/count)
    print("Greatest Increse: " +list1[incrValIndex] + ' $'+ str(incrVal))
    print("Greatest Increse: " +list1[incrValIndex] + ' $'+ str(Val))
    
    #Average change in profit/losses

    #Greatest increase in profits

    #Greatest decrease in losses