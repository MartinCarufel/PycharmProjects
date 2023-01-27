from testrail_api import TestRailAPI
import pandas as pd

api = TestRailAPI("https://testrail.dwos.com/", "martin.carufel@dental-wings.com", "18,Mac&Amo")
def main():

    # result = api.tests.get_test(253181)
    # print(result)

    # re1 = api.results.get_results(253181)
    # print(re1)

    full_result = api.results.get_results_for_run(1494)
    # for i in full_result:
    #     print(i)

    df = pd.DataFrame.from_dict(full_result)
    """
    Index(['id', 'test_id', 'status_id', , 'created_on',
           'assignedto_id', 'comment', 'version', 'elapsed', 'defects',
           'custom_step_results', 'custom_dwio_serial_number',
           'custom_handpiece_serial_number', 'custom_pod_serial_number',
           'custom_sample_size_used'],
          dtype='object')
    """
    # df_filtered = df[['test_id', 'status_id', 'created_by']]
    df_filtered = df.loc[:, ('test_id', 'status_id', 'created_by')]
    # df_filtered['tester name'] = df_filtered.apply(lambda row: name_id(int(row['created_by'])), axis=1)
    df_filtered.loc[:,'tester name'] = df_filtered.apply(lambda row: name_id(int(row['created_by'])), axis=1)
    # print(df[df["test_id"]==253185])
    print(df_filtered)

def get_attachment():
    import requests
    from requests.auth import HTTPBasicAuth


    client = APIClient('https://testrail.dwos.com/')

    URL = 'https://testrail.dwos.com/'
    credential = HTTPBasicAuth('martin.carufel@dental-wings.com', '18,Mac&Amo')
    r = requests.get(URL, auth=credential, data="index.php?/api/v2/get_attachment/29771")

    print(r.text)
    # att = api.attachments.get_attachments_for_run_bulk(1494)
    # print(att)
    # api.attachments.get_attachment()


def name_id(id):
    # print(id)
    # return api.users.get_user(int(id['created_by']))['name']
    return api.users.get_user(id)['name']


if __name__ == "__main__":
    main()
    # get_attachment()




