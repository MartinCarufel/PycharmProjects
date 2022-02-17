# coding: utf-8


def get_number_part(to_filter):
    number = []
    for i in to_filter:
        if i.isdigit():
            number.append(i)
    result = "".join(number)
    print(result)
    return result


def main():
    print("Hello world")



if __name__ == '__main__':
    main()
