from typing import List, Tuple
from Types import FrequencyType

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class FrequencyAnalysis:
    def __init__(
        self, data: List[float | int],
        num_classes: int = 0,
        class_width: float = 0.0
    ):
        self.data = np.array(data)
        self.min = self.data.min()
        self.max = self.data.max()
        self.range = self.max - self.min
        self.num_classes = num_classes if num_classes else self._sturges_rule()
        self.class_width = class_width if class_width else self._calculate_class_width()
        self.intervals = self._create_intervals()
        self.absolute_freq = self._calculate_frequencies()
        self.relative_freq = self.absolute_freq / len(self.data)
        self.cumulative_freq = np.cumsum(self.absolute_freq)
        self.cumulative_relative_freq = np.cumsum(self.relative_freq)
        self.bins = np.arange(self.min, self.max + self.class_width, self.class_width)
        self.bins_center = (self.bins[:-1] + self.bins[1:]) / 2

    def _sturges_rule(self) -> int:
        return int(np.ceil(1 + 3.322 * np.log10(len(self.data))))

    def _calculate_class_width(self) ->  float|int:
        return np.ceil(self.range / self.num_classes)

    def _create_intervals(self) -> List[Tuple[float|int, float|int]]:
        return [
            (
              self.min + i * self.class_width,
              self.min + (i + 1) * self.class_width
            )
              for i in range(self.num_classes)
        ]

    def _calculate_frequencies(self) -> np.ndarray:
        return np.array([
            (
                (self.data >= lower) & 
                (self.data <= upper if i+1==self.num_classes else self.data < upper)
            ).sum()
            for i, (lower, upper) in enumerate(self.intervals)
        ])    

    def create_distribution_table(self) -> pd.DataFrame:
        return pd.DataFrame({
            "I": [f"{lower:.2f} - {upper:.2f}" for lower, upper in self.intervals],
            "fi": self.absolute_freq,
            "hi": self.relative_freq,
            "%i": self.relative_freq * 100,
            "Fi": self.cumulative_freq,
            "Hi": self.cumulative_relative_freq,
            "$i": self.cumulative_relative_freq * 100
        })

    def plot_histogram(self, relative=False, polygon=False):
        plt.figure(figsize=(10, 6))
        
        plt.hist(
            self.data,
            self.bins,
            weights=np.ones_like(self.data) / len(self.data) if relative else None,
            edgecolor='black',
        )

         # Agregar polígono de frecuencia
        if polygon:
            frecuencies = self.relative_freq if relative else self.absolute_freq
            plt.plot(self.bins_center, frecuencies, 'o-', label='Frequency Polygon')
        
        plt.title("Histogram of Data")
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.show()

    def plot_ogive(self, type_freceuncie: FrequencyType=FrequencyType.ABSOLUTE.value):
        """
        Plotea una ogiva de frecuencia.

        Parámetros:
        type_freceuncie (FrequencyType): Tipo de frecuencia a plotear. Puede ser:
            - FrequencyType.ABSOLUTE: Frecuencia absoluta.
            - FrequencyType.RELATIVE: Frecuencia relativa.
            - FrequencyType.ABSOLUTE_CUMULATIVE: Frecuencia absoluta acumulada.
            - FrequencyType.RELATIVE_CUMULATIVE: Frecuencia relativa acumulada.

        Valor por defecto:
        type_freceuncie = FrequencyType.ABSOLUTE

        Retorna:
        None
        """

        dict_type_frecuencies = {
            'absolute': self.absolute_freq,
            'relative': self.relative_freq,
            'absolute_cumulative': self.cumulative_freq,
            'relative_cumulative': self.cumulative_relative_freq
        }
        plt.figure(figsize=(10, 6))
        
        plt.plot(self.bins_center, dict_type_frecuencies[type_freceuncie], 'o-', label='Ogive')
        plt.title("Ogive of Cumulative Frequencies")
        plt.xlabel("Values")
        plt.ylabel("Cumulative Frequency")
        plt.legend()
        plt.show()

    def plot_pie_diagram(self):
      plt.pie(self._calculate_frequencies(), labels=[f"{lower:.2f} - {upper:.2f}" for lower, upper in self.intervals], autopct='%1.1f%%')
      plt.title("Pie Diagram of Data")
      plt.show()

    def calculate_statistics(self) -> dict:
        return {
            "Mean": np.mean(self.data),
            "Median": np.median(self.data),
            "Standard Deviation": np.std(self.data),
            "Variance": np.var(self.data),
            "Skewness": pd.Series(self.data).skew(),
            "Kurtosis": pd.Series(self.data).kurtosis()
        }
