from desc.frecuence import FrequencyAnalysis

velocity_per_lab = [
    0.3, 0.9, 1.1, 1.7, 1.5, 0.8, 0.7, 1.1,
    0.8, 1.0, 1.3, 0.2, 1.6, 0.1, 0.5, 0.7,
    1.2, 1.5, 0.8, 0.9, 0.7, 0.5, 1.1, 1.5,
    0.1, 1.4, 0.7, 0.8, 0.6, 1.3, 1.2, 1.4,
    1.8, 0.7, 0.9, 1.0, 0.3, 1.2, 1.8, 1.0
]

 

def main():
    velocity_analisys = FrequencyAnalysis(velocity_per_lab, class_width=0.25)
    #velocity_analisys.plot_histogram()
    df = velocity_analisys.create_distribution_table()
    print(df)