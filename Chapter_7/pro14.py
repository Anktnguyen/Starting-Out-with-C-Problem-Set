"""
14. Expense Pie Chart
Create a text file that contains your expenses for last month in the following categories:
• Rent
• Gas
• Food
• Clothing
• Car payment
• Misc
Write a Python program that reads the data from the file and uses matplotlib to plot a pie
chart showing how you spend your money.
"""
import matplotlib.pyplot as plt

def main():
    #using w+ to overwrite previous data, using a (append) will add to file and make x-label out of range
    write_file = open("pie_chart_expenses.txt", "w+")
    #I created this list to guide the user through the categories
    item_labels = ["Rent", "Gas", "Food", "Clothing", "Car payment", "Misc"]

    #this was the list that I tried to create
    #expense_list = []
    for line in range(len(item_labels)):
        line = int(input(f"Enter amount of expenses for {item_labels[line]}: "))
        #originally I am using this because I was not understanding the process of writing it to the list
        #expense_list.append(write_file.write(f"{line} \n"))
        write_file.write(f"{line} \n")
    write_file.close()

    #Here is where the file get read
    open_file = open("pie_chart_expenses.txt", "r")
    item_labels = ["Rent", "Gas", "Food", "Clothing", "Car payment", "Misc"]
    expenses = open_file.readlines()
    open_file.close()

    #reading the file into list
    for line in range(len(expenses)):
        expenses[line] = expenses[line].strip("\n")

    #pie chart labels
    plt.pie(expenses, labels=item_labels)

    #title of chart
    plt.title("Monthly Expenses")

    #Display chart
    plt.show()
        



if __name__ == "__main__":
    main()
