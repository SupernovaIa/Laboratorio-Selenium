import pandas as pd


def crear_df(tabla):

    df = pd.DataFrame(tabla.split("\n"))
    df.drop([0,1], inplace=True)
    df[0] = df[0].str.replace(' °F', '')
    df[0] = df[0].str.replace(' mph', '')
    df[0] = df[0].str.replace(' in', '')
    df[0] = df[0].str.replace(' %', '')
    df = df[0].str.split(' ', expand=True)
    df.columns = datos = ["Date", "High Temp (ºF)", "Avg Temp (ºF)", "Low T (ºF)", "High Dew Pt (ºF)", "Avg Dew Pt (ºF)", "Low Dew Pt (ºF)", "High Hum (%)", "Avg Hum (%)", "Low Hum (%)", "High Spe (mph)", "Avg Spe (mph)", "Low Spe (mph)", "High Press (in)", "Low Press (in)", "Sum Prec (In)"]
    df.set_index('Date', inplace=True)
    df = df.applymap(lambda x: float(x))
    return df