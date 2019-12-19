import os
import csv

bank_data_csv = ("budget_data.csv")

months = {}
total_profit_loss = 0
change = 0
prev = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
sum_change = 0
other_change = 0
other_prev = 0
other_total = 9999999
other_sum_change = 0

with open(bank_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    csv_header = next(csvreader)

    for row in csvreader:
        
        total_profit_loss = total_profit_loss + int(row[1])

        date = row[0]

        if date in months:
            months[date] = months[date] + 1

        else:
            months[date] = 1

        total = total + 1

        if total > 1:
            change = int(row[1]) - prev
            sum_change = sum_change + change

            if change > greatest_increase:
                greatest_increase = change
                greatest_date = date

        prev = int(row[1])

        other_total = other_total + 1

        if other_total > 1:
            other_change = int(row[1]) - other_prev
            other_sum_change = other_sum_change + other_change

            if change < greatest_decrease:
                greatest_decrease = other_change
                lowest_date = date

        other_prev = int(row[1])

average_change = round(sum_change/(len(months)-1), 2)


print("Financial Analysis")
print("------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_date) + " $" + (str(greatest_increase)))
print("Greatest Decrease in Profits: " + str(lowest_date) + " $" + (str(greatest_decrease)))


with open('PyBankAnalysis.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("------------------\n")
    text.write("Total Months: " + str(len(months))+"\n")
    text.write("Total: $" + str(total_profit_loss) + "\n")
    text.write("Average Change: $" + str(average_change) + "\n")
    text.write("Greatest Increase in Profits: " + str(greatest_date) + " $" + (str(greatest_increase)) + "\n")
    text.write("Greatest Decrease in Profits: " + str(lowest_date) + " $" + (str(greatest_decrease)) + "\n")