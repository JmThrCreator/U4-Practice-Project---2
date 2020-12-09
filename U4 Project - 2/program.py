def get_gender():
    repeat = True
    while repeat == True:
        #asks the user to enter the gender
        race_gender = input("Are the athletes competing Male or Female (M/F): ").upper()
        #if male, it sets men's record times and exists the loop
        if race_gender == 'M':
            record_times = {"World Record Time": 9.58, "European Record Time": 9.86, "British Record Time": 9.87}
            repeat = False
        #if female, it sets women's record times and exits the loop
        elif race_gender == 'F':
            record_times = {"World Record Time": 10.49, "European Record Time": 10.73, "British Record Time": 10.99}
            repeat = False
        #if there is an invalid input, it prints an error message and loops back
        else:
            print("Invalid input, please enter M or F")
    return record_times

#sets the record times
record_times = get_gender()

#declares variables
adding_race_times = True
lane_number = 1
race_times = []

#user enters times
while adding_race_times == True:
    temp_race_time = input(f"Time of the athlete on lane {str(lane_number)} (X to stop): ")
    #exits out of the loop is input is x or X
    if temp_race_time.upper() == "X":
        if len(race_times) == 0:
            print("No times where added at all")
        adding_race_times = False
    else:
        #if the input is a number
        if temp_race_time.replace('.','',1).isdigit():
            #loops back if the input is 0
            if float(temp_race_time) <= 0:
                print("Cannot accept values 0 or under")
            #adds number to list and loops back to the next lane
            else:
                race_times.append([lane_number, round(float(temp_race_time), 2)])
                lane_number += 1]
        #if the input is not a number
        else:
            print("Invalid input")

def process_times(race_times, record_times):
    #declares variables
    min_athletes = 4
    max_athletes = 8
    
    #sorts the race_times list according to time from largest to smallest
    race_times.sort(key=lambda x:x[1], reverse=False)
    
    #displays lanes and times
    for lane_list in race_times:
        print(f"Lane {str(lane_list[0])} : {str(lane_list[1])}")
    
    #if not within the minimum and maximum bounds
    if len(race_times) < min_athletes:
        print("The amount of athletes is too small to qualify")
    elif len(race_times) > max_athletes:
        print("The amount of athletes is too large to qualify")
    
    #if within the bounds
    else:
        print("------------------------------")
        #for all 3 records, the program checks if the highest time matches them
        for record_name, record_time in record_times.items():
            if race_times[0][1] < record_time:
                #outputs what records have been beaten, where and what time
                print(f"{record_name} beaten at {str(race_times[0][1])} in lane {str(race_times[0][0])}")     
        print("------------------------------")

#if times have been added to the race_times list, it calls the function process_times
if len(race_times) >= 1:
    process_times(race_times, record_times)
