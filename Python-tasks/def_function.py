# format is [marks, 10th marksheets, 12th marksheet, adhaar card]
entrance_exam_results = {
    "Max" : [90, True, True, True],
    "Alie" : [85, True, False, True],
    "Ankit" : [70, False, True, True],
    "Dhanasekar" : [100, True, True, True],
    "Vishnu" : [97, True, True, True],
    "Sourabh" : [35, True, False, False],
    "Aravinth" : [30, True, False, False],
    "Karthik" : [60, True, True, True]
}

cut_off=60

def admission_status(selected, cut_off):#defining the function
    results=[]#stores result
    for candidate , data in selected.items():#loop to check
        mark =data[0]
        document =data[1:]

        if mark >= cut_off:
            if False not in document:
                status = "YOU ARE SELECTED"
            else:
                status = "needs to submit documents to be selected"
        else:
            status = "didn't meet the requirements"
        
        print(f"{candidate}, {status}")
        results.append((candidate, status))

    return results
         
results= admission_status(entrance_exam_results, cut_off)#fun call

"""output
Max, YOU ARE SELECTED
Alie, needs to submit documents to be selected
Ankit, needs to submit documents to be selected
Dhanasekar, YOU ARE SELECTED
Vishnu, YOU ARE SELECTED
Sourabh, didn't meet the requirements
Aravinth, didn't meet the requirements
Karthik, YOU ARE SELECTED"""

#2.Shopping
print("")

def afford_purchase(current_funds, cost):
    if current_funds > cost:
        return "Affordable, you can buy it. "#if true exits
    return "OUT OF BUDGET"
    
current_funds =30000
cost=40000
decide=afford_purchase(current_funds , cost)
print(decide)

"""output
OUT OF BUDGET"""

