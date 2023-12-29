from abc import ABCMeta, abstractmethod
from botocore.client import BaseClient
from typing import Generator, Callable, List
from boto3.session import Session


type DeleteResultType = Exception | None
type ListResultType = Generator[ResourceBase, None, None]
type ResourceType = Callable[[Session], ListResultType]
type TagType = dict[str, str]
type TagResultType = List[TagType] | None


LIST_FUNC: list = []


class ResourceBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, sess: BaseClient) -> None:
        self.sess: BaseClient = sess

    @abstractmethod
    def delete(self) -> DeleteResultType:
        pass
    
    @property
    @abstractmethod
    def tags(self) -> TagResultType:
        pass

    @abstractmethod
    def __str__(self) -> str | None:
        pass