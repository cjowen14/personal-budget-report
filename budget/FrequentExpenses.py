import Expense
import collections
import matplotlib.pyplot as plt

#save Expenses class in expenses variable
expenses = Expense.Expenses()

#read data into expenses variable
expenses.read_expenses('data/spending_data.csv')

#create list for spending categories
spending_categories = []

#add the categories from expenses to spending categories list
for expense in expenses.list:
    spending_categories.append(expense.category)

#count how many times each category shows up
spending_counter = collections.Counter(spending_categories)

#determine top5 most common categories
top5 = spending_counter.most_common(5)

#seperate category name and count into seperate lists
categories, count = zip(*top5)
print(count)

#build graph
fig, ax = plt.subplots()

#add categories and count as the axis
ax.bar(categories, count)

#add title to graph
ax.set_title('# of Purchases by Category')

#display graph
plt.show()