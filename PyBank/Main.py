import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Header
    csv_header = next(csvreader)
    print()
    print()
    print('---------------------------------------------------')
    print('                Financial Analysis')
    print('---------------------------------------------------')
###############

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
            diff.append(incr_temp)
            if(incr_temp > incrVal):
                incrVal = incr_temp
                incrValIndex = count 
                incr.append(incr_temp)
            if(incr_temp < decrVal):
                decrVal = incr_temp
                decrValIndex = count 
                decr.append(incr_temp)   
        count += 1 #count number of rows
            
        
        

    print("    Total Months: " + str(count))
    print("    Net Total: $" + str(p_n))
    print("    Average Change: " + str(sum(diff) / len(diff)))
    print("    Greatest Increase: " +list1[incrValIndex] + ' ($'+ str(incrVal)+')')
    print("    Greatest Decrease: " +list1[decrValIndex] + ' ($'+ str(decrVal)+')')
    print('---------------------------------------------------')
    print()
    print()
    csvreader.to_csv('results.csv')