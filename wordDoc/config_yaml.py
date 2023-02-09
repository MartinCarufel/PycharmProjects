import yaml
import requests
import json

from docx.document import Document
from docx.shared import Pt

try:
    d = Document("QUF63-5448 Template CSV Validation Specifications (v1.2).docx")
except TypeError:
    from docx import Document
    d = Document("QUF63-5448 Template CSV Validation Specifications (v1.2).docx")


class Create_csv_doc:
    def __init__(self, credential_user, credential_pwd):
        self.credential_user = credential_user
        self.credential_pwd = credential_pwd
        self.config = self.read_yaml()
        self.testrail_project_id = self.config["testrail project id"]
        self.testrail_parent_id = self.config["testrail parent section id"]
        self.docx_table_ref_id = self.config["table_mapping"]
        self.child_list = []
        self.child_list2 = {}


    def read_yaml(self):
        """ A function to read YAML file"""
        with open('config.yml') as f:
            config = yaml.safe_load(f)
        return config       # Return dict of the config file

    def get_child_section_id(self, parent_id):
        """
        parent_id: (int) no de la section parente
        Return: List of integer of Test Rail section_id that have matchin parent id
        """
        URL = "https://testrail.dwos.com//index.php?/api/v2/get_sections/2"     # get as dict all section in the project
                                                                                #(id, name, description, parent_id, suite_id ...
        r = requests.get(URL, auth=(self.credential_user, self.credential_pwd), headers={"Content-Type": "application/json"})
        print(r.status_code)
        # for data in r.json():
        #     print("{} - {} - {}" .format(data["id"], data["name"], data["parent_id"]))

        for i in r.json():
            if i["parent_id"] == parent_id:
                self.child_list.append([i["id"], i["name"]])
                self.child_list2[i["name"].upper()] = i["id"]
        print(self.child_list2)

    def found_corresponding_section_id(self, key):
        if key == 'IQ':
            section = self.child_list2["INSTALLATION QUALIFICATION"]
        if key == 'OQ':
            section = self.child_list2["OPERATIONAL QUALIFICATION"]
        if key == 'PQ':
            section = self.child_list2["PERFORMANCE QUALIFICATION"]
        return section

    def change_table_font(self, table, font_size_pt):
        """Table: docx x table ex: d.table[0] where d in docx object"""
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        font = run.font
                        font.size = Pt(font_size_pt)

    def docx_table_filling(self):
        section = None
        URL = "https://testrail.dwos.com//index.php?/api/v2/get_cases/2&section_id="
        authentification = (self.credential_user, self.credential_pwd)
        head = {"Content-Type": "application/json"}

        for section, value in self.docx_table_ref_id.items():
            section = self.found_corresponding_section_id(section)
            print(section)
            print("writting in table: {}  name: {}" .format(value, section))
            # r = requests.get(URL+str(section[0]), auth=(self.credential_user, self.credential_pwd), headers=head)
            r = requests.get(URL + str(section), auth=(self.credential_user, self.credential_pwd), headers=head)
            if r.status_code == 200:
                for i in range(len(r.json())):
                    element = r.json()[i]
                    print(len(d.tables))
                    print("Start write row {} for test case: {} in table {}".format(i, element["id"], value))
                    d.tables[value].cell(i+1, 0).text = str(i+1)
                    d.tables[value].cell(i+1, 1).text = element['title'][3:] + "\n" + "Ref Test Rail: " + str(
                        element['id'])
                    d.tables[value].cell(i+1, 2).text = element['custom_io_requirement']
                    d.tables[value].cell(i+1, 3).text = o.get_step_expected_result(element)
                    d.tables[value].cell(i+1, 4).text = element['custom_string_objective_evidence'] + " / " + element['custom_test_objev']
                    print("Finish write row {} for test case: {} in table {}".format(i, element["id"], value))
                    if i < len(r.json())-1:   # avoid adding extra ligne at the end of table
                        d.tables[value].add_row()
                        print("add row")
                self.change_table_font(d.tables[value], 9)

    def get_step_expected_result(self, test_case):
        list_of_expected_result = []

        for i in test_case['custom_steps_separated']:
            if i['expected'] != "":
                list_of_expected_result.append(i['expected'])
        return "\n".join(list_of_expected_result)


if __name__ == "__main__":
    # read the config yaml
    o = Create_csv_doc('martin.carufel@dental-wings.com', '18,Mac&Amo')
    o.get_child_section_id(o.testrail_parent_id)
    o.docx_table_filling()
    d.save(o.config["output doc name"])


