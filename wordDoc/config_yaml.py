import yaml
import requests
import json


class Create_csv_doc:
    def __init__(self, credential_user, credential_pwd):
        self.credential_user = credential_user
        self.credential_pwd = credential_pwd
        config = self.read_yaml()
        self.testrail_project_id = config["testrail project id"]
        self.testrail_parent_id = config["testrail parent section id"]
        self.docx_table_ref_id = config["table_mapping"]
        self.child_list = []

    def read_yaml(self):
        """ A function to read YAML file"""
        with open('config.yml') as f:
            config = yaml.safe_load(f)

        return config

    def get_child_section_id(self, parent_id):
        """
        parent_id: (int) no de la section parente
        Return: List of integer of Test Rail section_id that have matchin parent id
        """
        URL = "https://testrail.dwos.com//index.php?/api/v2/get_sections/2"
        r = requests.get(URL, auth=(self.credential_user, self.credential_pwd), headers={"Content-Type": "application/json"})
        # section_list = []
        for i in r.json():
            if i["parent_id"] == parent_id:
                self.child_list.append(i["id"])
        pass

    def docx_table_filling(self):

        pass

if __name__ == "__main__":
    # read the config yaml
    o = Create_csv_doc('martin.carufel@dental-wings.com', '18,Mac&Amo')
    o.get_child_section_id(11473)
    print(o.child_list)


