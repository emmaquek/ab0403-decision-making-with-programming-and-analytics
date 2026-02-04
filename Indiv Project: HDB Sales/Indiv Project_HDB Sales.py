"""
Recording link: https://youtu.be/RSY8uVmL3uA
Password (if any): NIL

Scenario 5: 5.	Which storey remains most popular among Singapore residences by flat type across the years.

You are given HDB_Sales.csv file by the interviewer during an
interview for an intern position in Nanyang Analytics Pte Ltd . 
The dataset contains HDB sales data collected between the year 2020 and 2025(Partial). 

You are to conduct analysis 
based on the dataset given and provide some insights to the marketing director of 
the company from the output of the analysis.

The following are the deliverables of your analysis:
1.	Allow user to enter a certain filter criterion, in this case flat model. 

2.  Tabulate a table that address the scenarios according to the filter criteria. 
(note: You are NOT allowed to use the tabulate module available in python import) 
    one of the possible tabulation suggested may be :

 _______________________________________________________________________
|             Popularity for ???  (flat model)              |
| _____________________________________________________________________|                                
|Storey	      |     2020    |    2021   |    2022  |     2023 |	  2024 |
| _____________________________________________________________________|     
|01 TO 03     |      999   |   	 999   |     999  |    999   |   999   |
|04 TO 06     |      999   |   	 999   |     999  |    999   |   999   |
|07 TO 09     |      999   |   	 999   |     999  |    999   |   999   |
|10 TO 12     |      999   |   	 999   |     999  |    999   |   999   |
|______________________________________________________________________|    
   
3.	You program should include capability to provide a summary of the insights based on 
the results of your table in point (2).

4.	You are required to allow your analysis on (2) to be continuous until a blank input
for (1) is detected

5.  To value add to the analysis, you are required to think of one additional analysis that the 
marketing director may be interested to find out after (4). Present the solution and explain how such analysis 
adds value to the analysis.

IMPORTANT: You must use the original dataset given, you are not allowed to use excel or any other 
application software to modify the data before importing it to your python program.
"""

#DEFINE CATEGORIES
def storey_cat():
    storey_temp = []
    for i in range(1,10,3):
        storey_temp.append(f"0{i} TO 0{i+2}")
    for i in range(10,51,3):
        storey_temp.append(f"{i} TO {i+2}")
    
    return storey_temp

#FILTER OUT RELEVANT DATA FROM CSV
def sort_data(flat_model):
    data = {}
    year = [2020, 2021, 2022, 2023, 2024]
    storey = storey_cat()
    
    for y in year:
        data[y] = {}
        for s in storey:
            data[y][s] = 0
    
    import csv
    filename = "HDB_Sales.csv" 
    with open(filename, "r") as file_pointer:
        csv_pointer = csv.reader(file_pointer)
        next(csv_pointer)
      
        for line in csv_pointer:
            s = line[3]
            y = int(line[-3])
            if line[5] == flat_model and y in data and s in storey:
                data[y][s] += 1          
    return data

#TABLE FORMATTING
def print_table(flat_model, data):
    print(f"""
{"_"*72}
|{"Popularity for " + flat_model:^70}|
|{"_"*70}|
|{'Storey':<15}|{'2020':>10}|{'2021':>10}|{'2022':>10}|{'2023':>10}|{'2024':>10}|
|{"_"*70}| """)
    
    for key in data[2020].keys():
        print_row = f"|{key:<15}|"
        for value in data.keys():
            print_row += f"{str(data[value][key]):>10}|"
        print(print_row)
    
    print(f"|{"_"*70}|\n")

#INSIGHTS: WHICH STOREY HAS THE MOST FLATS PURCHASED FOR EACH YEAR & OVERALL
def insights(data):
    year = [2020, 2021, 2022, 2023, 2024]
    storey = storey_cat()
    storey_max = {}
    for st in storey:
        storey_max[st] = 0
        
    for yr in year:
        highest_yearly = max(data[yr].values())
        if highest_yearly == 0:
            print(f"There were no such flats purchased in {yr}.")
            continue
        storey_check = []
        for st in storey:
            if highest_yearly == data[yr][st]:
                storey_check.append(st)
        storey_print = f"{storey_check[0]}"
        if len(storey_check) > 1:
            for i in range(1,len(storey_check)):
                storey_print += f", {storey_check[i]}"
        print(f"The most popular storey in {yr} is {storey_print} with total of {highest_yearly} flats purchased.")     
        for st in storey_check:
            storey_max[st] += 1
    
    highest = max(storey_max.values())
    highest_check = []
    for st in storey:
        if highest == storey_max[st]:
            highest_check.append(st)
    highest_print = f"{highest_check[0]}"
    if len(highest_check) > 1:
        for j in range(1,len(highest_check)):
            highest_print += f", {highest_check[j]}"
    print(f"The most popular storey throughout the years is {highest_print}.")
    
    return highest_print

def add_insights(data, first_insight):
    year = [2020, 2021, 2022, 2023, 2024]
    trend = []
    for y in year:
        count = data[y][first_insight]
        trend.append(count)
        
    for n in range(len(trend)-1):
        change = ((trend[n+1]-trend[n]) / trend[n]) * 100
        print(f"{year[n]} -> {year[n+1]}: {round(change,2)}% change")
        
#MAIN PROGRAM
print("""Welcome to my program!
In this program, you are able to check which storey remains most popular among Singapore residences by flat type across the years.
The flat models available to check are:""")
models = ["2-room","Adjoined flat","Apartment","DBSS","Improved","Maisonette","Model A","Model A-Maisonette","Model A2",
          "Multi Generation","New Generation","Premium Apartment","Simplified","Standard","Terrace","Type S1","Type S2"]
for model in models:
    print(model)
while True:
    filter_criterion = input(str("\nEnter flat model you would like to check (or press 'Enter' to exit the program):"))
    if filter_criterion == "":
        print("Thank you for using my program!")
        break
    elif filter_criterion not in models:
        print("There is no such model. Try again.")
    else:
        result = sort_data(filter_criterion)
        print_table(filter_criterion, result)
        insight = insights(result)
        answer = input(str(f"\nWould you like to know trends in {insight} storey {filter_criterion} flats purchased over the years? (Yes/No):"))
        if answer == "No":
            continue
        elif answer == "Yes":
            add_insights(result, insight)
          
            
