from resources.base import LIST_FUNC
from boto3.session import Session
from items.item import Item, State



def main():
    items: list[Item] = []

    for list_func in LIST_FUNC:
        for region in ["ap-northeast-2"]:
            for result in list_func(Session(region_name=region)):
                items.append(Item(result, region, result.__class__.__name__))

    for item in items:
        print(item)
        err = item.delete()
        if err:
            item.state, item.reason = State.FAILED, err
        else:
            item.state = State.DELETE
                
if __name__ == '__main__':
    main()