import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


csv_file_path = '/Users/sumit/Yagi Uda datasheet - Sheet1.csv'
df = pd.read_csv(csv_file_path)


angles = np.linspace(0,2*np.pi,37)
gain_3_element =list(df['Gain(3 element)'])
gain_5_element =list(df['Gain(5 element)'])
gain_7_element =list(df['Gain(7 element)'])

df["gain3"]=df['Gain(3 element)']-max(list(df['Gain(3 element)']))
df["gain5"]=df['Gain(5 element)']-max(list(df['Gain(5 element)']))
df["gain7"]=df['Gain(7 element)']-max(list(df['Gain(7 element)']))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})


plt.polar(angles, list(df["gain3"]), label='3-Element Yagi',marker=".")

plt.polar(angles, list(df["gain5"]), label='5-Element Yagi',marker=".")

plt.polar(angles, list(df["gain7"]), label='7-Element Yagi',marker=".")

plt.polar(angles,[-3]*37, label='-3 dB')


ax.set_ylim(min(list(df["gain5"])),0)
ax.set_xlim(0,2*np.pi)

ax.legend()
plt.title('Yagi-Uda Antenna Gain Patterns')
plt.plot()
plt.show()