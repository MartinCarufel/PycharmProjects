import re

mount_days = {"regular":[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
              "bisextile":[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]}



bisextile = None

def next_first_day_num(current_date, bisextile):
    """
    :current_date : yyyy-mm-dd
    :param bisextile: False / True
    :return: first week day in format yyyy-mm-dd
    """
    year = int(current_date[0:4])
    mount = int(current_date[5:7])
    day = int(current_date[8:10])
    if bisextile:
        this_year_mount_days = mount_days["bisextile"]
    else:
        this_year_mount_days = mount_days["regular"]


    new_date_num = day + 7
    if new_date_num > this_year_mount_days[mount-1]:
        new_date_num = new_date_num - this_year_mount_days[mount-1]
        mount = mount + 1
    if mount > 12:
        year = year + 1
        mount = 1
    return "{}-{}-{}".format(str(year), str(mount), str(new_date_num))

def format_date(input_date):
    """

    :param input_date:
    :return:
    """
    date = input_date.split("-")
    year = str(date[0])
    if int(date[1]) < 10:
        mount = "0" + date[1]
    else:
        mount = date[1]
    if int(date[2]) < 10:
        day = "0" + date[2]
    else:
        day = date[2]

    return "{}-{}-{}".format(date[0], mount, day)

def bisextile_selection():
    while True:
        print("1 for Bisextile year")
        print("2 for non- bisextile year")
        choice_selection = input("your choice and press ENTER: ")
        if choice_selection in ["1", "2"]:
            if choice_selection == "1":
                selection = True
            else:
                selection = False
            return selection
        else:
            print("\nWrong selection, type number 1 or 2 only\n")

def get_first_day():
    if bisextile:
        this_year_mount_days = mount_days["bisextile"]
    else:
        this_year_mount_days = mount_days["regular"]

    pattern_ex = "[0-9]{4}-[0-9]{2}-[0-9]{2}"
    test_pattern = re.compile(pattern_ex)

    while True:
        date = input("Enter the first day in following format (yyyy-mm-dd) : ")

        regex_test = test_pattern.fullmatch(date)
        if regex_test == None:
            print("\nWrong date format\n")
            continue
        date_split = date.split(sep="-")
        if int(date_split[1]) == 0 or int(date_split[1]) > 12:
            print("Mount cannot be 0 or higer than 12 (Dec)")
            continue
        if int(date_split[2]) == 0 or int(date_split[2]) > this_year_mount_days[int(date_split[1])-1]:
            print("\nWrong day number 0 not allowed or too big for the mount {} have only {} days.\n"
                  .format(int(date_split[1]), this_year_mount_days[int(date_split[1])-1]))
            continue
        return (date)

def bisextile_finder(date):
    year = int(date.split(sep="-")[0])
    rem = year % 4
    if rem == 0:
        return True
    else:
        return False

# date = "2023-12-31"
date = get_first_day()
# bisextile = bisextile_selection()
bisextile = bisextile_finder(date)
print(date)
for w in range(52):

    new_date = next_first_day_num(date, bisextile_finder(date))
    new_date = format_date(new_date)
    date = new_date
    print(new_date)