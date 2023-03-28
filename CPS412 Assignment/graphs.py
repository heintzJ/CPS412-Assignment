import matplotlib.pyplot as plt
import numpy as np
import csv
import os

# Get the absolute path of the directory containing the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the "survey.csv" file
file_path = os.path.join(script_dir, 'survey.csv')


# graph of ages in the data
def graphOfAges():
  x = []
  y = []
  with open(file_path, 'r') as csvfile:
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

# graph the faculty of against the question: Do you think ChatGPT would inhibit education?
def facultyAndEducation():
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    faculties = {"Sciences Yes":0, "Non-Sciences Yes":0, "Sciences No":0, "Non-Sciences No":0}
    for row in plots:
        if row[3] == "Computer Science" or row[3] == "Engineering" or row[3] == "Health/Life Sciences" or row[3] == "Biomedical Sciences":
          # If the key exists, increment its value by 1
          if row[9] == "Yes":
            faculties["Sciences Yes"] += 1
          else:
            faculties["Sciences No"] += 1
        else:
            if row[9] == "Yes":
              faculties["Non-Sciences Yes"] += 1
            else:
              faculties["Non-Sciences No"] += 1

    faculty = []
    for k in faculties:
      faculty.append(k)
    yes = [faculties["Sciences Yes"], faculties["Non-Sciences Yes"]]
    no = [faculties["Sciences No"], faculties["Non-Sciences No"]]

  # plt.pie(y, labels=x)
  l = np.arange(len(yes))
  plt.bar(l-0.17, yes, color='#2ca02c', label='Yes', width=0.35, edgecolor = 'black', linewidth = 1.5)
  plt.bar(l+0.17, no, color='#d62728', label='No', width=0.35, edgecolor = 'black', linewidth = 1.5)
  plt.xlabel('Faculty')
  plt.xticks([i for i in range(2)], ['Science', 'Non-Science'])
  plt.ylabel('Student Responses')
  plt.title('Do you think that using ChatGPT is a form of plagiarism?')
  plt.legend(['Yes', 'No'], frameon=False)
  for i, v in enumerate(yes):
    if v > 0:
      plt.text(i-0.17, v+0.1, str(v), ha='center', va='bottom', fontweight='bold')
  for i, v in enumerate(no):
    if v > 0:
      plt.text(i+0.17, v+0.1, str(v), ha='center', va='bottom', fontweight='bold')
  plt.show()

# Faculty vs ChatGPT usage
def chatgptUsage():
  x = []
  yes = []
  no_will = []
  no_willnot = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    faculties = {"Computer Science":[0, 0, 0],
                 "Media":[0, 0, 0],
                 "Humanities":[0, 0, 0],
                 "Engineering":[0, 0, 0],
                 "Health/Life Sciences":[0, 0, 0],
                 "Business":[0, 0, 0]}
    for row in plots:
        if row[3] in faculties.keys():
          # If the key exists, increment its value by 1
          if row[6] == "Yes":
            faculties[row[3]][0] += 1
          elif row[6] == "No, but I am planning to":
            faculties[row[3]][1] += 1
          elif row[6] == "No, and I am not planning to":
            faculties[row[3]][2] += 1
    for k in faculties:
      x.append(k)
      yes.append(faculties[k][0])
      no_will.append(faculties[k][1])
      no_willnot.append(faculties[k][2])

  plt.figure(figsize=(10,6))
  shift = np.arange(len(x))
  colors = ['black' if y > 0 else 'white' for y in yes]
  plt.bar(shift, yes, color='b', width=0.3, label="Yes", align='center', edgecolor = colors, linewidth = 1.5)
  colors = ['black' if y > 0 else 'white' for y in no_will]
  plt.bar(shift-0.3, no_will, color='orange', width=0.3, label='No, but I am planning on it', align='center', edgecolor = colors, linewidth = 1.5)
  colors = ['black' if y > 0 else 'white' for y in no_willnot]
  plt.bar(shift+0.3, no_willnot, color='red', width=0.3, label='No, and I am not planning on it', align='center', edgecolor = colors, linewidth = 1.5)

# Add labels to the bars. Does not show 0 if there is no bar. If you want it to show 0 just remove the if statement.
  for i, v in enumerate(yes):
    if v > 0:
      plt.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')
  for i, v in enumerate(no_will):
    if v > 0:
      plt.text(i-0.3, v, str(v), ha='center', va='bottom', fontweight='bold')
  for i, v in enumerate(no_willnot):
    if v > 0:
      plt.text(i+0.3, v, str(v), ha='center', va='bottom', fontweight='bold')

  plt.xlabel('Faculty')
  plt.xticks(np.arange(len(x)), x)
  plt.ylabel('Student Responses')
  plt.title('Have you Used ChatGPT?')
  plt.legend()
  plt.show()

def institutions():
  x = []
  y = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    unis = {}
    for row in plots:
      if row[5] not in unis:
        unis[row[5]] = 1
      else :
        unis[row[5]] += 1
    
    for k in unis:
      x.append(k)
      y.append(unis[k])
    plt.pie(y, labels = x)
    plt.show()
    
def howDoYouUseChatGTP():
  x = []
  y = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    useCases = {'Help with assignments': 0,
                'Work related information': 0,
                'Entertainment purposes': 0,
                'Media production': 0,
                'Other': 0}
    for row in plots:
        if row[7] in useCases.keys():
          # If the key exists, increment its value by 1
          useCases[row[7]] += 1
        else:
          useCases['Other'] += 1
    for k in useCases:
      x.append(k)
      y.append(useCases[k])

  plt.bar(x, y, color='g', width=0.72, label="Count")
  plt.xlabel('Response')
  plt.ylabel('Number of Responses')
  plt.title('What do You Use ChatGPT For?')
  plt.legend()
  plt.show()

#graphOfAges()
# facultyAndEducation()
# chatgptUsage()
# howDoYouUseChatGTP()
institutions()