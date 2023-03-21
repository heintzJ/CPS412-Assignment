import matplotlib.pyplot as plt
import csv

x = []
y = []

def graphOfAges():
  with open('survey.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    ages = {'18-22': 0, '23-29': 0, '30-39': 0, '40-49': 0}
    for row in plots:
        if row[1] in ages.keys():
          # If the key exists, increment its value by 1
          ages[row[1]] += 1
    for k in ages:

      x.append(k)
      y.append(ages[k])

  plt.bar(x, y, color='g', width=0.72, label="Count")
  plt.xlabel('Ages')
  plt.ylabel('Student Responses')
  plt.title('What Age Range Do You Fall Into?')
  plt.legend()
  plt.show()

graphOfAges()