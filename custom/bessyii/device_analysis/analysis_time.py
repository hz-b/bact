import numpy as np
import pandas as pd


tag_seconds = 24 * 60 * 60
woche_seconds = tag_seconds * 7
jahr_seconds = tag_seconds * 365.25
monat_seconds = jahr_seconds / 12
# https://de.wikipedia.org/wiki/Weltalter
universe_age = 4.354e17

df_input = pd.DataFrame(
        columns=["val", "unit", "conversion"],
        data=[
            (1.355e47, "Plankzeit original (CGS)", 1.38e-43),
            # https://de.wikipedia.org/wiki/Planck-Zeit
            (1.355e47, "Plankzeit Wikipedia (SI)", 5.391e-44),
            (7.2e21, "Attoseconds",  1e-18),
            (7.2e18, "Femtoseconds", 1e-15),
            (7.2e15, "Pikoseconds",  1e-12),
            (7.2e12, "Nanoseconds",  1e-9),
            (7.2e9, "Mikroseconds", 1e-6),
            (7.2e6, "Milliseconds", 1e-3),
            (7.2e3, "Seconds", 1),
            (120, "Minutes", 60),
            (0.083, "Tage", tag_seconds),
            (0.011, "Wochen", woche_seconds),
            (0.002, "Monate", monat_seconds),
            (0.0002, "Jahre", jahr_seconds),
            (0.0002, "Jahrzehnte", jahr_seconds * 10),
            (0.0002, "Jahrhunderte", jahr_seconds * 100),
            (1./2.41e14, "Gesamtalter des Universums", universe_age)
    ])

df = df_input.copy()
df.loc[:, "cross_check"] = df_input.val * df_input.conversion
df.loc[:, "computed_values"] = 7200 / df_input.conversion
df.columns = ["orig values", "unit name", "unit in sceconds", "check ", "computed_values"]
df
print(df.head(n=20))
