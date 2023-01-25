from testrail_api import TestRailAPI
import pandas as pd

api = TestRailAPI("https://testrail.dwos.com/", "martin.carufel@dental-wings.com", "18,Mac&Amo")

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
def name_id(id):
    # print(id)
    # return api.users.get_user(int(id['created_by']))['name']
    return api.users.get_user(id)['name']


df_filtered = df[['test_id', 'status_id', 'created_by']]
df_filtered['tester name'] = df_filtered.apply(lambda row: name_id(int(row['created_by'])), axis=1)
# print(df[df["test_id"]==253185])
print(df_filtered)


