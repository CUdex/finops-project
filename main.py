from resources.base import LIST_FUNC

def main():
    for list_func in LIST_FUNC:
        for result in list_func():
            print(result)

if __name__ == '__main__':
    main()