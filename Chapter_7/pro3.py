"""
3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a
list. The program should calculate and display the total rainfall for the year, the average
monthly rainfall, the months with the highest and lowest amounts.
"""

def main():
    #empty list for rainfall
    rainfall_tmonth = []
    total = 0
    count = 0
    #for loop to record all 12 months 
    for count in range(12):
        monthly_rain = int(input(f"Enter amount of rainfall for month {count + 1}: "))
        #appending the amount for each month
        rainfall_tmonth.append(monthly_rain)
        total += monthly_rain
        count += 1
    average = total / count

    #printing out all of the information
    print(f'{rainfall_tmonth}')
    print(f"The highest rainfall amount is {max(rainfall_tmonth)}")
    print(f"The lowest rainfall amount is {min(rainfall_tmonth)}")
    print(f"The average rainfall for 12 months is {average:.2f}")

    

if __name__ == "__main__":
    main()