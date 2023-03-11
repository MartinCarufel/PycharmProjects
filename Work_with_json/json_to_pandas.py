import pandas as pd
import json


def get_expected_result(data):
    """
    :param data: Is the content of the test case dict 'custom_steps_separated'
    :return: String of all expected results
    """
    expected_result = []
    for i in range(len(data)):
        expected_result.append("Step: {}: {}".format(str(i+1), data[i]["expected"]))

    return "\n".join(expected_result)


pd.set_option("display.max_columns", 5)

with open(r"D:\user_data\Martin\OneDrive\Documents\json_response\get_cases\11362.json") as f:
    tspec = json.load(f)

df = pd.DataFrame(columns=["Step", "Description", "Requirement", "Expected Result", "Test Method / Objective Evidence"])

for i in range(len(tspec)):
    df.loc[i] = [
    i+1,
    "Test Case: {}\n{}".format(str(tspec[i]["id"]), tspec[i]["title"][3:]),
    str(tspec[i]["custom_io_requirement"]),
    get_expected_result(tspec[i]["custom_steps_separated"]),
    "z"
    ]

for i in range(len(df)):
    print("-------------------------------------------------------------")
    print(df.loc[i]["Description"])
    print(df.loc[i]["Expected Result"])
    print("-------------------------------------------------------------")



