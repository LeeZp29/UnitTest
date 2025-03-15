def main():
    str = input("Nhập chuỗi: ")
    print(value(str))
    print(value_startswith(str))

def value(greeting:str):
    if greeting.lower().find('hello')==0:
      return 0
    if greeting.lower().find('h')==0:
        return 20
    return 100
    # # wrong
    # if greeting.lower().find('hello')==0:
    #   return 100
    # return 0

def value_startswith(greeting:str):
    if greeting.lower().startswith("hello"):
        return 0
    if greeting.lower().startswith('h'):
        return 20
    return 100

if __name__ == "__main__":
    main()