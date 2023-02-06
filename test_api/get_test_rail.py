import requests
import json


def print_list_of_dict(req_lst):
    if req_lst.status_code == 200:
        for i in req_lst.json():
            for key, data in i.items():
                print(f"{key}: {data}")
            print("--------------------------------------------------------\n")
    else:
        print(f"Request status code: {req_lst.status_code}")

def get_section_per_parent_id(request, parent_id):
    """
    request: HTML Request response
    parent_id: (int) no de la section parente
    Return: List of integer of Test Rail section_id that have matchin parent id
    """
    section_list = []
    for i in request.json():
        if i["parent_id"] == parent_id:
            section_list.append(i["id"])
    return section_list


def get_step_expected_result(test_case):
    list_of_expected_result = []

    for i in test_case['custom_steps_separated']:
        if i['expected'] != "":
            list_of_expected_result.append(i['expected'])

    return "\n".join(list_of_expected_result)

def ex1():
    iurl = 'https://the-one-api.dev/v2'
    command = '/book'
    section_id = '11476'

    cr2 = ('martin.carufel@dental-wings.com', '18,Mac&Amo')
    # URL = "https://testrail.dwos.com//index.php?/api/v2/get_case/42400"


    """... get_cases/2&section_id=" + case_id 
                --> /2  Project ID
                --> &section_id=   filter on section_id field 
    """

    URL = "https://testrail.dwos.com//index.php?/api/v2/get_cases/2&section_id=" + section_id
    r = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
    # print(r.status_code)
    if r.status_code == 200:
        for i in r.json():
            for key, data in i.items():
                print(f"{key}: {data}")
            print("--------------------------------------------------------\n")
    else:
        print(f"Request status code: {r.status_code}")

def ex2():
    section_id = 11473

    cr2 = ('martin.carufel@dental-wings.com', '18,Mac&Amo')

    URL = "https://testrail.dwos.com//index.php?/api/v2/get_sections/2"
    r = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
    section_list = get_section_per_parent_id(r, section_id)
    # print(r.status_code)
    # print_list_of_dict(r)
    # print(r.json())
    print(section_list)

def ex3():
    section_id = '11476'
    cr2 = ('martin.carufel@dental-wings.com', '18,Mac&Amo')
    URL = "https://testrail.dwos.com//index.php?/api/v2/get_sections/2"
    list_section = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
    for i in get_section_per_parent_id(list_section, 11473):
        URL = "https://testrail.dwos.com//index.php?/api/v2/get_cases/2&section_id=" + str(i)
        r = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
        print_list_of_dict(r)
# ex1()
# ex2()
ex3()

