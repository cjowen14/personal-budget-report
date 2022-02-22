import Expense
import matplotlib.pyplot as plt

#create budget list class
class BudgetList():
    #establish variables
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    #append expenses to either expenses or overages list and calculate respective total
    def append (self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item
    
    #get length of both expenses and overages lists combined and return
    def __len__(self):
        return (len(self.expenses) + len(self.overages))

    #make class iterable with expenses and overages
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self
    
    #get next value for expense or overage
    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()
            
            

def main():
    #store return value from BudgetList class to myBudgetList variable
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    #run each expense through the append method in the BudgetList class
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    #print results of how many total expenses there are
    print("The count of all expenses: " + str(len(myBudgetList)))

    #loop through myBudgetList(because it is now iterable) to print each entry
    for entry in myBudgetList:
        print(entry)

    #create graph
    fig, ax = plt.subplots()
    #create labels and values for graph
    labels = ["Expenses", "Overages", "Budget"]
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    #add labels, values, and color to graph
    ax.bar(labels, values, color=['green', 'red', 'blue'])
    #add title for graph
    ax.set_title('Your total expenses vs. total budget')
    #display graph
    plt.show()

if __name__ == '__main__':
    main()