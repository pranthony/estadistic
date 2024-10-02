from abc import ABC, abstractmethod

class Homework(ABC):
    @abstractmethod
    def make_homework(self, topic):
        pass

class Overleaf(Homework):
    def make_homework(self, topic):
        return f'Making homework about {topic} with Overleaf'

class GoogleDocs(Homework):
    def make_homework(self, topic):
        return f'Making homework about {topic} with Google Docs'

class StrategyHomework(Homework):
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def make_homework(self, topic):
        return self._strategy.make_homework(topic)

if __name__ == '__main__':
    homework = StrategyHomework(Overleaf())
    print(homework.make_homework('causas y concecuencias de la independencia del Perú'))

    homework.set_strategy(GoogleDocs())
    print(homework.make_homework('impacto de la globalizacion'))
