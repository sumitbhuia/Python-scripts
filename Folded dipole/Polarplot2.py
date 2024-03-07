import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


csv_file_path = '/Users/sumit/Folded dipole/Folded dipole.csv'
df = pd.read_csv(csv_file_path)


angles = np.linspace(0,2*np.pi,73)
gain =list(df['Gain'])

df["gain"]=df['Gain']-max(list(df['Gain']))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})


plt.polar(angles, list(df["gain"]), label='Gain',marker=".")

plt.polar(angles,[-3]*73, label='-3 dB')


ax.set_ylim(min(list(df["gain"])),0)
ax.set_xlim(0,2*np.pi)

ax.legend()
plt.title('Folded dipole Antenna Gain Patterns')
plt.plot()
plt.show()