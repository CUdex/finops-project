from resources.base import LIST_FUNC, TagResultType
from boto3.session import Session
from items.item import Item, State

def has_tag_key(tags: TagResultType, key: str) -> bool:
    for tag in tags:
        if tag['Key'] == key:
            return True
    return False

def main():
    items: list[Item] = []

    for list_func in LIST_FUNC:
        for region in ["ap-northeast-2"]:
            for result in list_func(Session(region_name=region)):
                items.append(Item(result, region, result.__class__.__name__))

    for item in items:
        if has_tag_key(item.tags, 'asd'):
            item.state, item.reason = State.FILTERED, Exception('TAG_KEY_FILTER')
            continue
        else:
            err = item.delete()
            if err:
                item.state, item.reason = State.FAILED, err
            else:
                item.state = State.DELETE

    for item in items:
        print(item)
                
if __name__ == '__main__':
    main()