import networkx as nx
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('Data/large_twitch_features.csv')

possible_vals = {column: tuple(data[column].unique())
                 for column in data.columns
                 if isinstance(data[column][0], str)} # numerikus változókat ne nézzük

# konvertáljuk át a kategorikus változókat numerikussá
def tr_to_numeric(col):
    name = col.name

    if name not in possible_vals:
        # már eleve numerikus
        return col

    return col.map(lambda val: possible_vals[col.name].index(val))

# konvertált adathalmaz
num_data = data.transform(tr_to_numeric, axis = 0)

# korrelációs mátrix
corr_mtx = num_data.corr()

# korrelációs mátrix ábrázolása



plt.figure(figsize = (10, 10))
plt.title('Korrelációs mátrix')

# csak az alsó háromszöget mutassa
mask = np.fromfunction(lambda i, j: i <= j, shape = corr_mtx.shape)

sns.heatmap(corr_mtx.round(2), center = 0, vmin = -1, vmax = 1, mask = mask)
plt.show()


print(0)
