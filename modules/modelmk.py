from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

import pandas as pd

def train_model(df:pd.DataFrame, seed=64):

    # création des jeux de train/test
    X_train, X_test, y_train, y_test = train_test_split(df.drop('satisfaction', axis=1), df['satisfaction'], test_size=0.1, random_state=seed)

    # normaliser les données
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # convertir les données y aussi :
    y_train = y_train.squeeze().ravel()
    y_test = y_test.squeeze().ravel()

    # entrainement du modèle 
    forest = RandomForestClassifier(n_jobs=-1, random_state=seed)
    forest.fit(X_train, y_train)
    score = round(forest.score(X_test, y_test)*100, 2)


    return forest, score