__author__ = '@britodfbr'
from abc import ABC, abstractmethod


class SanitizarBehavior(ABC):
    @abstractmethod
    def run(self, cls):
        raise NotImplementedError


class FormatarBehavior(ABC):
    @abstractmethod
    def run(self, cls):
        raise NotImplementedError


class EstilizarStatusOkBehavior(ABC):
    @abstractmethod
    def run(self, cls):
        raise NotImplementedError


class AlterarBodyIdBehavior(ABC):
    @abstractmethod
    def run(self, cls):
        raise NotImplementedError


class InserirMsgRevogBehavior(ABC):
    @abstractmethod
    def run(self, cls):
        raise NotImplementedError


class SalvarBehavior(ABC):
    @abstractmethod
    def run(self, cls):
        raise NotImplementedError
