from typing import List, Tuple

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

    def _sturges_rule(self) -> int:
        return int(np.ceil(1 + 3.322 * np.log10(len(self.data))))

    def _calculate_class_width(self) -> float:
        return np.ceil(self.range / self.num_classes)

    def _create_intervals(self) -> List[Tuple[float, float]]:
        return [
            (
              self.min + i * self.class_width,
              self.min + (i + 1) * self.class_width
            )
              for i in range(self.num_classes)
        ]

    def _calculate_frequencies(self) -> np.ndarray:
        return np.array([
            ((self.data >= lower) & (self.data < upper)).sum()
            for lower, upper in self.intervals
        ])

    def create_distribution_table(self) -> pd.DataFrame:
        absolute_freq = self._calculate_frequencies()
        relative_freq = absolute_freq / len(self.data)
        cumulative_freq = np.cumsum(absolute_freq)
        cumulative_relative_freq = np.cumsum(relative_freq)

        return pd.DataFrame({
            "I": [f"{lower:.2f} - {upper:.2f}" for lower, upper in self.intervals],
            "fi": absolute_freq,
            "hi": relative_freq,
            "%i": relative_freq * 100,
            "Fi": cumulative_freq,
            "Hi": cumulative_relative_freq,
            "$i": cumulative_relative_freq * 100
        })

    def plot_histogram(self, relative=False):
        plt.figure(figsize=(10, 6))

        plt.hist(
            self.data,
            bins=self.num_classes,
            weights=np.ones_like(self.data) / len(self.data) if relative else None,
            edgecolor='black',

        )
        
        plt.title("Histogram of Data")
        plt.xlabel("Values")
        plt.ylabel("Frequency")
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
