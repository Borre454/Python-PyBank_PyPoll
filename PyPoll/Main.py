import csv
import os 

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Header
    csv_header = next(csvreader)
    #print(csv_header)
    print()
    print()
    print('---------------------------------------------------')
    print('                Election Results')
    print('---------------------------------------------------')
###############
    votes = 0
    candidates = []
    cand1 = []
    cand2 = []
    cand3 = []
    cand4 = []
   
    
    for row in csvreader: 
        if row[2] not in candidates:
            candidates.append(row[2])
        if candidates[0] in row[2]:
            cand1.append(candidates[0])
        elif candidates[1] in row[2]:
            cand2.append(candidates[1])
        elif candidates[2] in row[2]:
            cand3.append(candidates[2])
        elif candidates[3] in row[2]:
            cand4.append(candidates[3])
        
        votes += 1
        votes_cand1 = len(cand1)
        votes_cand2 = len(cand2)
        votes_cand3 = len(cand3)
        votes_cand4 = len(cand4) 
        v_count = [votes_cand1, votes_cand2, votes_cand3, votes_cand4] 
        cand1_perc = (len(cand1) / votes) * 100
        cand2_perc = (len(cand2) / votes) * 100
        cand3_perc = (len(cand3) / votes) * 100
        cand4_perc = (len(cand4) / votes) * 100
        def winner():
            if v_count[0] > v_count[1] and v_count[0] > v_count[2] and v_count[0] > v_count[3]:
                print("Winner: " + candidates[0])
            elif v_count[1] > v_count[0] and v_count[1] > v_count[2] and v_count[1] > v_count[3]:
                print("Winner: " + candidates[1])
            elif v_count[2] > v_count[0] and v_count[2] > v_count[1] and v_count[2] > v_count[3]:
                print("Winner: " + candidates[2])
            elif v_count[3] > v_count[0] and v_count[3] > v_count[1] and v_count[3] > v_count[2]:
                print("Winner: " + candidates[3])

    print("Total Votes: " + str(votes))
    print('---------------------------------------------------')
    #print(candidates)
    print(candidates[0] + ": " + str(round(cand1_perc, 4)) + "% (" + str(votes_cand1)+ ")")
    print(candidates[1] + ": " + str(round(cand2_perc, 4)) + "% (" + str(votes_cand2)+ ")")
    print(candidates[2] + ": " + str(round(cand3_perc, 4)) + "% (" + str(votes_cand3)+ ")")
    print(candidates[3] + ": " + str(round(cand4_perc, 4)) + "% (" + str(votes_cand4)+ ")")
    print('---------------------------------------------------')
    winner()
    print('---------------------------------------------------')
    print()
