def get_gender():
    repeat = True
    while repeat == True:
        race_gender = input("Are the athletes competing Male or Female (M/F): ").upper()
        if race_gender == 'M':
            record_times = {"World Record Time": 9.58, "European Record Time": 9.86, "British Record Time": 9.87}
            repeat = False
        elif race_gender == 'F':
            record_times = {"World Record Time": 10.49, "European Record Time": 10.73, "British Record Time": 10.99}
            repeat = False
        else:
            print("Invalid input, please enter M or F")
    return record_times

record_times = get_gender()
adding_race_times = True
lane_number = 1
race_times = []

while adding_race_times == True:
    temp_race_time = input(f"Time of the athlete on lane {str(lane_number)} (X to stop): ")
    if temp_race_time.upper() == "X":
        if len(race_times) == 0:
            print("No times where added at all")
        adding_race_times = False
    else:
        if temp_race_time.replace('.','',1).isdigit():
            if float(temp_race_time) <= 0:
                print("Cannot accept values 0 or under")
            else:
                race_times.append([lane_number, round(float(temp_race_time), 2)])
                lane_number += 1
        else:
            print("Invalid input")

def process_times(race_times, record_times):
    min_athletes = 4
    max_athletes = 8

    race_times.sort(key=lambda x:x[1], reverse=False)

    for lane_list in race_times:
        print(f"Lane {str(lane_list[0])} : {str(lane_list[1])}")

    if len(race_times) < min_athletes:
        print("The amount of athletes is too small to qualify")
    elif len(race_times) > max_athletes:
        print("The amount of athletes is too large to qualify")
    else:
        print("------------------------------")
        for record_name, record_time in record_times.items():
            if race_times[0][1] < record_time:
                print(f"{record_name} beaten at {str(race_times[0][1])} in lane {str(race_times[0][0])}")     
        print("------------------------------")

if len(race_times) >= 1:
    process_times(race_times, record_times)
