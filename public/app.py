from desc.frecuence import FrequencyAnalysis
from mock import medidas

import numpy as np
import pandas as pd
import streamlit as st


analisys = FrequencyAnalysis(medidas)

df = analisys.create_distribution_table()
st.write(df)