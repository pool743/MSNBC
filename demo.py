import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

seq = open('msnbc990928.txt')

lines = seq.readlines()

linesNoSpace = [x[:-1] for x in lines]


#######FIRST HIT ANALYSIS########


""" page1first = []
page2first = []
page3first = []
page4first = []
page5first = []
page6first = []
page7first = []
page8first = []
page9first = []
page10first = []
page11first = []
page12first = []
page13first = []
page14first = []
page15first = []
page16first = []
page17first = []


for x in linesNoSpace:
    firstCharacter = x[:2]

    if firstCharacter == '1 ':
        page1first.append(firstCharacter)
    elif firstCharacter == '2 ':
        page2first.append(firstCharacter)
    elif firstCharacter == '3 ':
        page3first.append(firstCharacter)
    elif firstCharacter == '4 ':
        page4first.append(firstCharacter)
    elif firstCharacter == '5 ':
        page5first.append(firstCharacter)
    elif firstCharacter == '6 ':
        page6first.append(firstCharacter)
    elif firstCharacter == '7 ':
        page7first.append(firstCharacter)
    elif firstCharacter == '8 ':
        page8first.append(firstCharacter)
    elif firstCharacter == '9 ':
        page9first.append(firstCharacter)
    elif firstCharacter == '10':
        page10first.append(firstCharacter)
    elif firstCharacter == '11':
        page11first.append(firstCharacter)
    elif firstCharacter == '12':
        page12first.append(firstCharacter)
    elif firstCharacter == '13':
        page13first.append(firstCharacter)
    elif firstCharacter == '14':
        page14first.append(firstCharacter)
    elif firstCharacter == '15':
        page15first.append(firstCharacter)
    elif firstCharacter == '16':
        page16first.append(firstCharacter)
    elif firstCharacter == '17':
        page17first.append(firstCharacter)



g = globals()
firstHit = []

for i in range(1,18):
    varname = 'page{}first'.format(i)
    g[varname] = firstHit.append(len((g[varname])))


mylabels = ['frontpage', 'news', 'tech', 'local', 'opinion', 'on-air', 'misc', 'weather', 'msn-news', 'health', 'living', 'business', 'msn-sports', 'sports', 'summary', 'bbs', 'travel']




plt.pie(firstHit, labels=mylabels, autopct="%1.1f%%")
plt.title("First Hits")

plt.show() """


######LAST HIT ANALYSIS#######

""" page1last = []
page2last = []
page3last = []
page4last = []
page5last = []
page6last = []
page7last = []
page8last = []
page9last = []
page10last = []
page11last = []
page12last = []
page13last = []
page14last = []
page15last = []
page16last = []
page17last = []


for x in linesNoSpace:
    lastCharacter = x[:-3]

    if lastCharacter == ' 1 ':
        page1last.append(lastCharacter)
    elif lastCharacter == ' 2 ':
        page2last.append(lastCharacter)
    elif lastCharacter == ' 3 ':
        page3last.append(lastCharacter)
    elif lastCharacter == ' 4 ':
        page4last.append(lastCharacter)
    elif lastCharacter == ' 5 ':
        page5last.append(lastCharacter)
    elif lastCharacter == ' 6 ':
        page6last.append(lastCharacter)
    elif lastCharacter == ' 7 ':
        page7last.append(lastCharacter)
    elif lastCharacter == ' 8 ':
        page8last.append(lastCharacter)
    elif lastCharacter == ' 9 ':
        page9last.append(lastCharacter)
    elif lastCharacter == '10 ':
        page10last.append(lastCharacter)
    elif lastCharacter == '11 ':
        page11last.append(lastCharacter)
    elif lastCharacter == '12 ':
        page12last.append(lastCharacter)
    elif lastCharacter == '13 ':
        page13last.append(lastCharacter)
    elif lastCharacter == '14 ':
        page14last.append(lastCharacter)
    elif lastCharacter == '15 ':
        page15last.append(lastCharacter)
    elif lastCharacter == '16 ':
        page16last.append(lastCharacter)
    elif lastCharacter == '17 ':
        page17last.append(lastCharacter)



g = globals()
lastHit = []

for i in range(1,18):
    varname = 'page{}last'.format(i)
    g[varname] = lastHit.append(len((g[varname])))


mylabels = ['frontpage', 'news', 'tech', 'local', 'opinion', 'on-air', 'misc', 'weather', 'msn-news', 'health', 'living', 'business', 'msn-sports', 'sports', 'summary', 'bbs', 'travel']

plt.pie(lastHit, labels=mylabels, autopct="%1.1f%%")
plt.title("Last Hits")

plt.show() """










####HOW MANY REQUESTS PER USER DISTRIBUTION#######

linesWithX =[]
totalvisits = []

for x in linesNoSpace:
    y = re.sub(r"10|11|12|13|14|15|16|17", "x", x)
    z = re.sub("\s", "", y)
    linesWithX.append(z)

for x in linesWithX:
    vistis = len(x)
    totalvisits.append(vistis)

""" binwidth = 20
plt.hist(totalvisits, bins=range(0, 15000, binwidth))
plt.title("Frequency of Requests")
plt.yscale('log', nonposy='clip')
plt.xlabel("Frequency")
plt.ylabel("Number of Requests")
plt.show()


stdDev = np.std(totalvisits)
mean = np.mean(totalvisits)
#mode
vals,counts = np.unique(totalvisits, return_counts=True)
index = np.argmax(counts)



print(vals[index])
print(mean)
print(stdDev) """



######FINDING THE BOT BEHAVIOUR 15000 hits frontpage over and over#####
############ bot at ~2380 random?########
#######bot at 2064 only 3#########
########## bot at ~2274 likes 14########
#####bot  at 7500 seems to hover on one page then switch#####
#####bot at 1923 likes 10,2 and 14#######
############ 2 bots at ~1029 are they identical?#############

def BotInvestigation(y,z):
    botPositions = []

    for x in totalvisits:
        position = totalvisits.index(x)
        if x < y and x > z :
            botPositions.append(position)


    print(botPositions)

    botPositionInt = int(botPositions[0])

    bot = linesNoSpace[botPositionInt]

    botList = bot.split()

    botListCount = Counter(botList)

    out = dict(list(botListCount.items())[0:50]) 
    print(str(out))
    print(len(botList))

    print(botList[0:200]) 
    plt.bar(range(len(botListCount)), list(botListCount.values()), align='center')
    plt.xticks(range(len(botListCount)), list(botListCount.keys()))
    plt.xlabel("Category")
    plt.ylabel("Number of visits")
    plt.title("Bot Behaviour")
    plt.show()

BotInvestigation(2300,2250)

##### in function y is equal to upper number and x lower number to narrow down and pick out bot position in user sequence #####




##########take out bots and redoing analysis ###########

""" withoutBots = []
for x in totalvisits:
    if x < 300:
        withoutBots.append(x)

binwidth = 5
plt.hist(withoutBots, bins=range(0, 300, binwidth))
plt.yscale('log', nonposy='clip')
plt.title("Frequency of Requests")
plt.xlabel("Number of Requests")
plt.ylabel("Frequency")
plt.show()


stdDev = np.std(withoutBots)
mean = np.mean(withoutBots)
#mode
vals,counts = np.unique(withoutBots, return_counts=True)
index = np.argmax(counts)



print(vals[index])
print(mean)
print(stdDev)
print(sum(withoutBots))
print(sum(totalvisits)) """


#######most likely to go after pages########

def whatcomesnext(firstpage):
    startsWith = []
    secondPage1 = []
    secondPage2 = []
    secondPage3 = []
    secondPage4 = []
    secondPage5 = []
    secondPage6 = []
    secondPage7 = []
    secondPage8 = []
    secondPage9 = []
    secondPage10 = []
    secondPage11= []
    secondPage12= []
    secondPage13= []
    secondPage14= []
    secondPage15= []
    secondPage16= []
    secondPage17 = []
    empties = []
    alltogehter = []

    for x in linesNoSpace:
        if x.startswith("{}".format(firstpage)):
            startsWith.append(x)

    for x in startsWith:
        y = x[2:]
        if y == '':
            empties.append(y)
        elif y.startswith('1 '):
            secondPage1.append(y)

        elif y.startswith('2 '):
            secondPage2.append(y)

        elif y.startswith('3 '):
            secondPage3.append(y)

        elif y.startswith('4 '):
            secondPage4.append(y)

        elif y.startswith('5 '):
            secondPage5.append(y)

        elif y.startswith('6 '):
            secondPage6.append(y)

        elif y.startswith('7 '):
            secondPage7.append(y)

        elif y.startswith('8 '):
            secondPage8.append(y)

        elif y.startswith('9 '):
            secondPage1.append(y)

        elif y.startswith('10'):
            secondPage10.append(y)

        elif y.startswith('11'):
            secondPage11.append(y)

        elif y.startswith('12'):
            secondPage12.append(y)

        elif y.startswith('13'):
            secondPage13.append(y)

        elif y.startswith('14'):
            secondPage14.append(y)

        elif y.startswith('15'):
            secondPage15.append(y)

        elif y.startswith('16'):
            secondPage16.append(y)

        elif y.startswith('17'):
            secondPage17.append(y)


    alltogehter.append(len(secondPage1))
    alltogehter.append(len(secondPage2))
    alltogehter.append(len(secondPage3))
    alltogehter.append(len(secondPage4))
    alltogehter.append(len(secondPage5))
    alltogehter.append(len(secondPage6))
    alltogehter.append(len(secondPage7))
    alltogehter.append(len(secondPage8))
    alltogehter.append(len(secondPage9))
    alltogehter.append(len(secondPage10))
    alltogehter.append(len(secondPage11))
    alltogehter.append(len(secondPage12))
    alltogehter.append(len(secondPage13))
    alltogehter.append(len(secondPage15))
    alltogehter.append(len(secondPage16))
    alltogehter.append(len(secondPage17))
    print(alltogehter)
    zz = alltogehter
    mylabels = ['homepage', 'news', 'tech', 'local', 'opinion', 'on-air', 'misc', 'weather', 'msn-news', 'health', 'living', 'business', 'msn-sports', 'sports', 'summary', 'bbs', 'travel']
    plt.pie(zz, autopct="%1.1f%%", labels=mylabels)
    plt.title("Where Next After Sports?")
    

    plt.show()


whatcomesnext(5)


