import pandas as pd

dfx = pd.read_csv('data/clean_aiplane.csv')

print(dfx.columns)

passenger_filter = {
    'gender': 'female',
    'age': (35, '+'),
    # 'type': 'loyal customer'
}

flight_filter = {
    # 'flight distance': (1200, '+'),
    # 'class': ['eco', 'eco plus'],
    'reason': 'personal travel'
}

def prepdata(passenger_filter:dict, flight_filter:dict, dataframe:pd.DataFrame, take_delay_in=True):

    passengers_criteria = ['female', 'male', 'age', 'loyal customer', 'disloyal customer']
    flight_criteria = ['business', 'eco', 'eco plus', 'business travel', 'personal travel', 'flight distance']
    
    df = dataframe.copy()

    # PASSENGERS FILTERS
    for k,v in passenger_filter.items():
        if k == 'age':
            df = df.loc[df['age'] >= v[0]] if v[1] == '+' else df.loc[df['age'] <= v[0]]
        else:
            df = df.loc[df[v] == 1]

    df = df.drop(passengers_criteria, axis=1)

    # FLIGHT FILTERS
    for k,v in flight_filter.items():
        if k == 'flight distance':
            df = df.loc[df['flight distance'] >= v[0]] if v[1] == '+' else df.loc[df['flight distance'] <= v[0]]
        elif k == 'class':
            for clas in v : df = df.loc[df[clas] == 0]
        else:
            df = df.loc[df[v] == 1]

    df = df.drop(flight_criteria, axis=1)
    if not take_delay_in : df = df.drop('arrival delay in minutes', axis=1)

    return df


testx = prepdata(passenger_filter, flight_filter, dfx)

print(testx)