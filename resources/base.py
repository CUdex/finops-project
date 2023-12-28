from abc import ABCMeta, abstractmethod
from botocore.client import BaseClient


LIST_FUNC: list = []


class ResourceBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, sess: BaseClient) -> None:
        self.sess: BaseClient = sess

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def __str__(self):
        pass