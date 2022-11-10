import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from os import path
#data_dir is the location of the csv where we are pulling data
DATA_DIR = '/Users/loganoscher/Downloads/ltcwbb-files-0.8.1/data'

#section one!! sorting by pitch speed, using pitches csv :)
df = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'pitches.csv'))

# common pitches (idk what these are)
df = df.query("pitch_type in ('FF', 'SL', 'CH', 'FT', 'CU', 'SI', 'FC', 'FS', 'KC')")

df['mph'].quantile(.9)
df.query("pitch_type == 'FF'")['mph'].quantile(.9)
df[['mph', 'spin_rate']].describe()

g = sns.displot(df, x='mph', kind='kde', fill=True)

# density plot of pitch seeds (by what kinda pitch it is)
g = sns.displot(df, x='mph', kind='kde', hue='pitch_type', fill=True,
                aspect=1.75)

# desnity plot of pitch speeds (by what kinda pitch it is AND strikes)
g = sns.displot(df, x='mph', kind='kde', hue='pitch_type', col='s', fill=True)

#making some new rows and stuff :)
g = sns.displot(df, x='mph', kind='kde', hue='s', col='pitch_type', col_wrap=3)

# from textbook, setting the height and stuff
g = sns.displot(df, kind='kde', x='mph', col='s', row='b', hue='pitch_type',
                fill=True, aspect=1.75, height=2)
g = sns.displot(df, kind='kde', x='mph', hue='s', col='pitch_type')
g = sns.displot(df, kind='kde', x='mph', hue='s', col='pitch_type', col_wrap=2)
g.fig.subplots_adjust(top=0.9) # adding a title
g.fig.suptitle('Distribution of Pitch Speeds by Type, Strikes')
g.set(xlim=(65, 105))
g.set_xlabels('MPH')
g.set_ylabels('Density')
g.savefig('speed_by_types_strike.png')

# setting colours, making columns

#pulling up some more data
