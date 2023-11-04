import pandas as pd

def prepdata(passenger_filter:dict, flight_filter:dict, dataframe:pd.DataFrame, take_delay_in=True):

    passengers_criteria = ['female', 'male', 'age', 'loyal customer', 'disloyal customer']
    flight_criteria = ['business', 'eco', 'eco plus', 'business travel', 'personal travel', 'flight distance']
    df = dataframe

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
        elif k == 'rm_class':
            for rm in v : df = df.loc[df[rm] == 0]
        else:
            df = df.loc[df[v] == 1]

    df = df.drop(flight_criteria, axis=1)

    # DELAY FILTER
    if not take_delay_in : df = df.drop('arrival delay in minutes', axis=1)


    return df
