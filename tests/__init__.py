#Crear todos los unit tests para la clase FrecuencyAnalisys
import unittest
from desc.frecuence import FrequencyAnalysis  # Importa la clase FrequencyAnalysis
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para testing de gráficos

class TestFrequencyAnalysis(unittest.TestCase):

    def test_init_with_text(self):
        fa = FrequencyAnalysis("Este es un texto de prueba")
        self.assertEqual(fa.text, "Este es un texto de prueba")

    def test_init_with_data(self):
        fa = FrequencyAnalysis(["palabra1", "palabra2", "palabra3"])
        self.assertEqual(fa.data, ["palabra1", "palabra2", "palabra3"])

    def test_calculate_frequencies_empty_text(self):
        fa = FrequencyAnalysis("")
        self.assertEqual(fa.calculate_frequencies(), {})

    def test_calculate_frequencies_single_word(self):
        fa = FrequencyAnalysis("palabra")
        self.assertEqual(fa.calculate_frequencies(), {"palabra": 1})

    def test_calculate_frequencies_multiple_words(self):
        fa = FrequencyAnalysis("palabra1 palabra2 palabra1")
        self.assertEqual(fa.calculate_frequencies(), {"palabra1": 2, "palabra2": 1})

    def test_calculate_frequencies_punctuation(self):
        fa = FrequencyAnalysis("palabra1, palabra2. palabra1!")
        self.assertEqual(fa.calculate_frequencies(), {"palabra1": 2, "palabra2": 1})

    def test_get_top_n_frequencies_empty_text(self):
        fa = FrequencyAnalysis("")
        self.assertEqual(fa.get_top_n_frequencies(5), [])

    def test_get_top_n_frequencies_single_word(self):
        fa = FrequencyAnalysis("palabra")
        self.assertEqual(fa.get_top_n_frequencies(1), [("palabra", 1)])

    def test_get_top_n_frequencies_multiple_words(self):
        fa = FrequencyAnalysis("palabra1 palabra2 palabra1")
        self.assertEqual(fa.get_top_n_frequencies(2), [("palabra1", 2), ("palabra2", 1)])

    def test_get_top_n_frequencies_n_greater_than_total(self):
        fa = FrequencyAnalysis("palabra1 palabra2 palabra1")
        self.assertEqual(fa.get_top_n_frequencies(5), [("palabra1", 2), ("palabra2", 1)])

    def test_plot_frequencies_empty_text(self):
        fa = FrequencyAnalysis("")
        try:
            fa.plot_frequencies()
        except Exception as e:
            self.fail("plot_frequencies() raised an exception: " + str(e))

    def test_plot_frequencies_single_word(self):
        fa = FrequencyAnalysis("palabra")
        try:
            fa.plot_frequencies()
        except Exception as e:
            self.fail("plot_frequencies() raised an exception: " + str(e))

    def test_plot_frequencies_multiple_words(self):
        fa = FrequencyAnalysis("palabra1 palabra2 palabra1")
        try:
            fa.plot_frequencies()
        except Exception as e:
            self.fail("plot_frequencies() raised an exception: " + str(e))

    def test_frequency_analysis_with_stop_words(self):
        fa = FrequencyAnalysis("palabra1 de la palabra2")
        self.assertEqual(fa.calculate_frequencies(), {"palabra1": 1, "palabra2": 1})

    def test_frequency_analysis_with_case_insensitivity(self):
        fa = FrequencyAnalysis("Palabra1 palabra1")
        self.assertEqual(fa.calculate_frequencies(), {"palabra1": 2})

if __name__ == '__main__':
    unittest.main()