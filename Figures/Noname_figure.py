from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_square(self):
        pass