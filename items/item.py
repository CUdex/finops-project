from items.state import State
from resources.base import ResourceBase, TagResultType
from typing import TypedDict
from boto3.session import Session
from resources.utils import convert_dict_to_tags

class ItemDict(TypedDict):
    state: State
    reason: Exception | None
    region: str
    resource: ResourceBase
    type: str


class Item:
    def __init__(self, resource: ResourceBase, region: str, name: str):
        self.__item = {
            "state": State.NEW,
            "reason": Exception | None,
            "region": region,
            "resource": resource,
            "type": name
        }

    def __str__(self):
        return f'{self.__item['region']} - {self.__item['type']} - {self.__item['resource']} - {self.__item['state']} - {self.__item['reason']}'
    
    def delete(self):
        self.__item['resource'].delete()

    @property
    def state(self):
        return self.__item['state']
    
    @state.setter
    def state(self, value):
        self.__item['state'] = value
    
    @property
    def reason(self):
        return self.__item['reason']
    
    @reason.setter
    def reason(self, value):
        self.__item['reason'] = value

    @property
    def tags(self) -> TagResultType:
        return convert_dict_to_tags(self.__item['resource'].tags)
