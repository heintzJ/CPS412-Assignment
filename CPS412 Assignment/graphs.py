# Jack Heintz (501162746)
# Tristan Cheng (501163280)
# Felipe Quiroga (501153511)
# Brandon Liyanage (501162078)

# All of lines that call the graph methods are uncommented, to see one at a time, just comment out all the others

import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import textwrap

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
  colours = ['lightcoral', 'indianred','firebrick','darkred']
  plt.bar(x, y, color=colours, width=0.72, label="Count", edgecolor='black',linewidth = 1.2)
  plt.xlabel('Ages')
  plt.ylabel('Student Responses')
  plt.title('Age Distribution of Survey Respondents')
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
  plt.title('Public Opinion on ChatGPT and Plagiarism')
  plt.legend(['Yes', 'No'], frameon=False)

  #displays number of responses for each bar option
  for i, v in enumerate(yes):
    if v > 0:
      plt.text(i-0.17, v+0.1, str(v), ha='center', va='bottom', fontweight='bold')
  for i, v in enumerate(no):
    if v > 0:
      plt.text(i+0.17, v+0.1, str(v), ha='center', va='bottom', fontweight='bold')
  plt.show()

# Faculty vs ChatGPT usage
def chatgptUsageByMajor():
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
  plt.title('ChatGPT Adoption Rates Among Different Majors')
  plt.legend()
  plt.show()

#chatGPT usage regardless of major
def chatgptUsage():
  options = []
  data = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    response = {}

    for row in plots:
      if row[6] not in response:
        response[row[6]] = 1
      else:
        response[row[6]] += 1

    for k in response:
      options.append(k)
      data.append(response[k])

    colours = ["cyan", "purple", "gray"]
    explode = (0.1,0,0)
    _, _, graph = plt.pie(data, labels = options, colors=colours, explode=explode, shadow=True, autopct='%1.1f%%',
                          textprops={'horizontalalignment': 'center', 'verticalalignment': 'center'},
                          wedgeprops={'edgecolor': 'black'})
    plt.title('ChatGPT Usage: Survey Results')
    plt.show()

def institutions():

  name = []
  data = []
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
      name.append(k)
      data.append(unis[k])

    total = sum(data)
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
  wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: f'{pct:.1f}%' if pct > 5 else '', textprops={'weight':'bold', 'fontsize':20}, startangle=33)
  #box around label
  bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
  kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")
  #lines connecting to pie graph and label
  for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    if data[i] / total > 0.05:
      ax.annotate(f'{name[i]} ({data[i]})', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
              horizontalalignment=horizontalalignment, **kw)
    else:
      ax.annotate(name[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
              horizontalalignment=horizontalalignment, **kw)

  ax.set_title("Institution Distribution of Survey Respondents")
  plt.show()

def howDoYouUseChatGPT():
  x = []
  y = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    useCases = {'Help with assignments': 0,
                ' Work related information': 0,
                ' Entertainment purposes': 0,
                ' Media production': 0,
                'Other': 0}
    for row in plots:
        s = str(row[7])
        splitString = s.split(",")
        for w in splitString:
          if w in useCases.keys():
            # If the key exists, increment its value by 1
            useCases[w] += 1
          elif w == '':
            pass
          else:
            useCases['Other'] += 1
    for k in useCases:
      x.append(k)
      y.append(useCases[k])

  plt.figure(figsize=(8,5))
  colours = ['orangered','coral','lightsalmon','darksalmon','mistyrose']
  plt.bar(x, y, color=colours, width=0.5, edgecolor='black',linewidth=1.2)
  plt.xticks(fontsize=6)
  plt.xlabel('Response')
  plt.ylabel('Number of Responses')
  plt.title('Primary Uses of ChatGPT as Reported by Survey Respondents')
  for i, v in enumerate(y):
    plt.text(i, v+0.1, str(v), color='black', fontweight='bold', ha='center', va='bottom', fontsize=10)
  plt.show()

def gender():
  x = []
  y = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    gender = {}
    for row in plots:
      if row[2] not in gender:
        gender[row[2]] = 1
      else :
        gender[row[2]] += 1
    
    for k in gender:
      x.append(k)
      y.append(gender[k])

    explode = (0, 0, 0.1)
    colours = ["purple", "blue", "hotpink"]
    _, _, graph = plt.pie(y, labels = x, colors=colours, autopct='%1.1f%%', explode=explode, shadow=True)
    for text in graph:
      text.set_color('white')
    plt.title("Gender Distribution of Survey Respondents")
    plt.show()

def potentialUses():
  x = []
  y = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    # skip first line
    next(plots)
    cases = {}
    for row in plots:
      if row[10] not in cases:
        cases[row[10]] = 1
      else :
        cases[row[10]] += 1
    
    for k in cases:
      x.append(k)
      y.append(cases[k])

    _, _, graph = plt.pie(y, autopct='%1.1f%%')
    for text in graph:
      text.set_color('white')
    plt.legend(x, title="Response", loc="right", bbox_to_anchor=(1.6,0,0.05,2))
    plt.title("Potential Applications of ChatGPT for Students: Survey Results")
    plt.show()

def chatgptInWork():
  labels = []
  data = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    #skip the first 6 lines
    for i in range(6):
      next(plots)

    options = {}

    for row in plots:
        if row[-1] not in options:
          options[row[-1]] = 1
        else:
          options[row[-1]] += 1

    for k in options:
      labels.append(k)
      data.append(options[k])

    colours = ['aqua','turquoise','lightseagreen','teal']
    plt.barh(labels, data, color=colours, height=0.5, edgecolor='black', linewidth=1.1)
    # able to split the labels in multiple lines rather than one long line
    wrapped_labels = [ '\n'.join(textwrap.wrap(label, width=20)) for label in labels ]
    plt.yticks(labels, wrapped_labels)
    plt.title("Attitudes Toward ChatGPT in the Workplace")
    plt.subplots_adjust(left=0.25)
    for i, v in enumerate(data):
      plt.text(v + 0.2, i, str(v), color='black', fontweight='bold')
    plt.show()

def chatgptPlagiarism():
  labels = []
  data = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    #skip the first 6 lines
    for i in range(6):
      next(plots)

    options = {}

    for row in plots:
      if row[10] not in options:
        options[row[10]] = 1
      else:
        options[row[10]] += 1

    for k in options:
      labels.append('\n'.join(textwrap.wrap(k, 15)))
      data.append(options[k])

    colours = ['darkkhaki','khaki','gold','goldenrod']
    explode = (0.1,0,0,0)
    _, _, graph = plt.pie(data, labels=labels, colors=colours, explode=explode, shadow=True, autopct='%1.1f%%',
                          textprops={'horizontalalignment': 'center', 'verticalalignment': 'center', 'weight':'bold'},
                          wedgeprops={'edgecolor': 'black'}, startangle=-105, labeldistance=1.2)
    plt.title("Public Opinion on ChatGPT and Plagiarism")
    plt.show()

#Does ChatGPT inhibit education?
def chatgptAndEdu():
  labels = []
  data = []
  with open(file_path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)

    options = {}

    for row in plots:
      if row[9] not in options:
        options[row[9]] = 1
      else:
        options[row[9]] += 1

    for k in options:
      labels.append(k)
      data.append(options[k])
    
    colours = ['palegreen','lawngreen']
    explode = (0.1,0)
    _, _, graph = plt.pie(data, labels = options, colors=colours, explode=explode, shadow=True, autopct='%1.1f%%',
                          textprops={'horizontalalignment': 'center', 'verticalalignment': 'center', 'weight':'bold'},
                          wedgeprops={'edgecolor': 'black'}, startangle=-105, labeldistance=1.2)

    plt.title("Understanding Student Perceptions on ChatGPT and Education")
    plt.show()

if __name__ == '__main__':    
  graphOfAges()
  facultyAndEducation()
  chatgptUsageByMajor()
  chatgptUsage()
  howDoYouUseChatGPT()
  institutions()
  gender()
  potentialUses()
  chatgptInWork()
  chatgptPlagiarism()
  chatgptAndEdu()
  