# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

url = "https://www.w-index.com/"

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

aaa = soup.select("b")

for i in range(len(aaa)):
    print(aaa[i])

bbb = aaa[1]

print(bbb)

bbb = str(bbb)

bbb = bbb.replace("<b id=\"i-4\">", "")
bbb = bbb.replace("<span class=\"red\">", "")
bbb = bbb.replace("</span></b>", "")
bbb = bbb.replace("<span class=\"green\">", "")
ccc = ""

for i in range(len(bbb)):
    if (bbb[i] == "-" or bbb[i] == "+"):
        break
    else:
        ccc += bbb[i]

kabuka = [random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3)]
plt.plot(range(0, 11), kabuka)
plt.savefig("population.png")

# plt.show()

print()
print(ccc)

ddd = bbb.replace(ccc, "")

print(ddd)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# population = np.array([144850, 140660, 33480, 27910, 22950, 21670, 21540, 16790, 14580, 13160, 12560])
population = [random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3)]
labels = ["China", "India", "USA", "Indonesia", "Pakistan", "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico", "Japan"]
colors = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan", "black", ]
# 円グラフを描画
plt.pie(population, colors=colors, labels=labels, autopct="%1.1f%%", counterclock=False, startangle=90, pctdistance=1.5)
# plt.plot(population, colors=colors, labels=labels, autopct="%1.1f%%", counterclock=False, startangle=90, pctdistance=1.5)
# plt.legend()
plt.title(ccc + "   " + ddd)

# plt.savefig("population.png")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
