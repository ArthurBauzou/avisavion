from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

# import des données
dfx = pd.read_csv('data/x.csv')
dfy = pd.read_csv('data/y.csv')
SEED = 1234

print(dfx.columns)

# création des jeux de train/test
Xr, Xs, yr, ys = train_test_split(dfx, dfy, test_size=0.2, random_state=SEED)

# normaliser les données
scaler = MinMaxScaler()
Xr = scaler.fit_transform(Xr)
Xs = scaler.transform(Xs)

print(Xr[:10])
# model = RandomForestClassifier(n_jobs=-1, random_state=SEED)