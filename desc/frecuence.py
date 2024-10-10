from typing import List, Tuple
from Types import FrequencyType

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st

class FrequencyAnalysis:
    def __init__(
        self, data: List[float | int],
        num_classes: int = 0,
        class_width: float = 0.0
    ):
        self.data = np.array(data)
        self.data_len = len(self.data)
        self.min = self.data.min()
        self.max = self.data.max()
        self.mean = np.mean(self.data)
        self.range = self.max - self.min
        self.num_classes = num_classes if num_classes else self._sturges_rule()
        self.class_width = class_width if class_width else self._calculate_class_width()
        self.intervals = self._create_intervals()
        self.absolute_freq = self._calculate_frequencies()
        self.relative_freq = self.absolute_freq / self.data_len
        self.cumulative_freq = np.cumsum(self.absolute_freq)
        self.cumulative_relative_freq = np.cumsum(self.relative_freq)
        self.bins = np.arange(self.min, self.max + self.class_width, self.class_width)
        self.bins_center = (self.bins[:-1] + self.bins[1:]) / 2

    def _sturges_rule(self) -> int:
        return int(np.ceil(1 + 3.322 * np.log10(self.data_len)))

    def _calculate_class_width(self) ->  float|int:
        return np.ceil(self.range / self.num_classes)

    def _create_intervals(self) -> List[Tuple[float|int, float|int]]:
        return np.array([
            (
              self.min + i * self.class_width,
              self.min + (i + 1) * self.class_width
            )
              for i in range(self.num_classes)
        ])

    def _calculate_frequencies(self) -> np.ndarray:
        return np.array([
            (
                (self.data >= lower) & 
                (self.data <= upper if (i + 1) == self.num_classes else self.data < upper)
            ).sum()
            for i, (lower, upper) in enumerate(self.intervals)
        ])    

    def create_distribution_table(self) -> pd.DataFrame:
        return pd.DataFrame({
            "I": [ 
                f"[ {lower} - {upper}{' )' if i + 1 != len(self.intervals) else ' ]'}"
                for i, (lower, upper) in enumerate(self.intervals)
            ],
            "mi": self.bins_center,
            "fi": self.absolute_freq,
            "hi": self.relative_freq,
            "%i": self.relative_freq * 100,
            "Fi": self.cumulative_freq,
            "Hi": self.cumulative_relative_freq,
            "$i": self.cumulative_relative_freq * 100
        }, range(1, len(self.intervals)+1))

    def plot_histogram(self, relative=False, polygon=False):
        # Crear una nueva figura y ejes
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Calcular los pesos si es relativo
        weights = np.ones_like(self.data) / self.data_len if relative else None
        
        # Crear el histograma
        hist = ax.hist(
            self.data,
            self.bins,
            weights=weights,
            edgecolor='black',
        )

        frecuencias = self.relative_freq if relative else self.absolute_freq
        
        # Etiquetar cada barra con su frecuencia
        for rect, freq in zip(hist[2], frecuencias):
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                height,
                f'{round(freq, 2)}',
                va='bottom',
                ha='center'
            )
        
        # Agregar polígono de frecuencia si se solicita
        if polygon:
            ax.plot(self.bins_center, frecuencias, 'o-', label='Polígono de frecuencia')
            ax.legend()
        
        # Configurar título y etiquetas de ejes
        ax.set_title('Histograma')
        ax.set_xlabel('Intervalos')
        ax.set_ylabel(f"Frecuencia {'relativa' if relative else 'absoluta'}")
        
        # Ajustar el diseño
        plt.tight_layout()

        plt.close(fig)
        # Retornar la figura
        return fig

    def plot_ogive(self, type_frecuency: FrequencyType=FrequencyType.ABSOLUTE):
        """
        Plotea una ogiva de frecuencia.

        Parámetros:
        type_frecuency (FrequencyType): Tipo de frecuencia a plotear. Puede ser:
            - FrequencyType.ABSOLUTE: Frecuencia absoluta.
            - FrequencyType.RELATIVE: Frecuencia relativa.
            - FrequencyType.ABSOLUTE_CUMULATIVE: Frecuencia absoluta acumulada.
            - FrequencyType.RELATIVE_CUMULATIVE: Frecuencia relativa acumulada.

        Valor por defecto:
        type_frecuency = FrequencyType.ABSOLUTE

        Retorna:
        None
        """

        dict_type_frecuencies = {
            FrequencyType.ABSOLUTE: (
                self.absolute_freq,
                'absoluta'
            ),
            FrequencyType.RELATIVE: (
                self.relative_freq,
                'relativa'
            ),
            FrequencyType.ABSOLUTE_CUMULATIVE: (
                self.cumulative_freq,
                'absoluta acumulada'
            ),
            FrequencyType.RELATIVE_CUMULATIVE: (
                self.cumulative_relative_freq,
                'relativa acumulada'
            ),
            FrequencyType.ABSOLUTE_CUMULATIVE_LT: (
                list(reversed(self.cumulative_freq)),
                'absoluta acumulada (menor que)'
            ),
            FrequencyType.RELATIVE_CUMULATIVE_LT: (
                list(reversed(self.cumulative_relative_freq)),
                'relativa acumulada (menor que)'
            )
        }
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(
            self.bins_center,
            dict_type_frecuencies[type_frecuency][0],
            'o-', label='Ogiva'
        )

        # Etiquetar cada barra con su frecuencia
        for rect, freq in zip(self.bins_center, dict_type_frecuencies[type_frecuency][0]):
            ax.text(
                rect,
                freq,
                f'{round(freq, 2)}',
                va='bottom',
                ha='center'
            )
        
        ax.set_title("Diagrama de ogiva")
        ax.set_xlabel("Intervalos")
        ax.set_ylabel(f'Frecuencia {dict_type_frecuencies[type_frecuency][1]}')
        ax.legend()

        # Ajustar el diseño
        plt.tight_layout()

        plt.close(fig)
        return fig    

    def plot_pie_diagram(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.pie(
            self.absolute_freq,
            labels=[f"{lower} - {upper}" for lower, upper in self.intervals],
            autopct='%1.1f%%'
        )
        
        ax.set_title("Diagrama de torta")

        plt.close()

        return fig

    def calculate_statistics(self) -> dict:
        return {
            "Mean": self.mean,
            "Median": np.median(self.data),
            "Standard Deviation": np.std(self.data),
            "Variance": np.var(self.data),
            "Skewness": pd.Series(self.data).skew(),
            "Kurtosis": pd.Series(self.data).kurtosis()
        }
    
    def calculate_varianze(self):
        
        return 1/(self.data_len-1)*(sum(self.data**2)-self.data_len*(self.mean**2))
