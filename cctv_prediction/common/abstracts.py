from abc import *


class PrintBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass


class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass


class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def driver(self):
        pass
