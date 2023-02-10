import yaml
import requests
import json

from docx.document import Document
from docx.shared import Pt
from docx import Document
import logging
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(filename='test.log', mode='w')
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

class Create_csv_doc:
    def __init__(self, credential_user, credential_pwd):
        self.credential_user = credential_user
        self.credential_pwd = credential_pwd
        self.config = self.read_yaml()
        self.testrail_project_id = self.config["testrail project id"]
        self.testrail_parent_id = self.config["testrail parent section id"]
        self.docx_table_ref_id = {}
        if not self.config["use CSV template"]:
            self.docx_table_ref_id = self.config["table mapping"]
        self.child_list = []
        self.child_list2 = {}
        self.doc = Document(self.config["template path"])

    def read_yaml(self):
        """ A function to read YAML file"""
        with open('config.yml') as f:
            config = yaml.safe_load(f)
        return config       # Return dict of the config file

    def get_child_section_id(self, parent_id):
        """
        parent_id: (int) no de la section parente
        Return: List of integer of Test Rail section_id that have matching parent id
        """
        URL = "https://testrail.dwos.com//index.php?/api/v2/get_sections/2"   # get as dict all section in the project
                                                            # (id, name, description, parent_id, suite_id ...
        r = requests.get(URL, auth=(self.credential_user, self.credential_pwd),
                         headers={"Content-Type": "application/json"})
        for i in r.json():
            if i["parent_id"] == parent_id:
                table_id = self.found_corresponding_section_id(i)
                self.docx_table_ref_id[i["id"]] = table_id
        logger.debug("Number of sub section found: {}".format(len(self.docx_table_ref_id)))

    def found_corresponding_section_id(self, t_case_json_object):
        table_id = None
        if t_case_json_object["name"].upper() == 'INSTALLATION QUALIFICATION':
            table_id = 2
        if t_case_json_object["name"].upper() == 'OPERATIONAL QUALIFICATION':
            table_id = 3
        if t_case_json_object["name"].upper() == 'PERFORMANCE QUALIFICATION':
            table_id = 4
        if t_case_json_object["name"].upper() not in ['INSTALLATION QUALIFICATION', 'OPERATIONAL QUALIFICATION',
                                                      'PERFORMANCE QUALIFICATION']:
            logging.error("section '{}' named '{}' is not a valid name, check section title spelling"
                          .format(t_case_json_object["id"] ,t_case_json_object["name"]))
            table_id = None
        return table_id

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
        authentication = (self.credential_user, self.credential_pwd)
        head = {"Content-Type": "application/json"}

        for section, value in self.docx_table_ref_id.items():
            logging.debug("Create table for section: {}" .format(section))
            logging.debug("writing in table: {}  name: {}" .format(value, section))
            r = requests.get(URL + str(section), auth=authentication, headers=head)
            if r.status_code == 200:
                for i in range(len(r.json())):
                    element = r.json()[i]
                    logging.debug("There is {} table in word doc" .format(len(self.doc.tables)))
                    logging.debug("Start write row {} for test case: {} in table {}".format(i, element["id"], value))
                    self.doc.tables[value].cell(i+1, 0).text = str(i+1)
                    self.doc.tables[value].cell(i+1, 1).text = element['title'][3:] + "\n" + "Ref Test Rail: " + str(
                        element['id'])
                    try:
                        self.doc.tables[value].cell(i+1, 2).text = element['custom_io_requirement']
                    except TypeError:
                        self.doc.tables[value].cell(i + 1, 2).text = "Not defined"
                    try:
                        self.doc.tables[value].cell(i+1, 3).text = o.get_step_expected_result(element)
                    except TypeError:
                        self.doc.tables[value].cell(i + 1, 3).text = "Not Defined"
                    try:
                        self.doc.tables[value].cell(i+1, 4).text = element['custom_string_objective_evidence'] + " / " \
                                                                   + element['custom_test_objev']
                    except TypeError:
                        self.doc.tables[value].cell(i+1, 4).text = "Not Defined"
                    logging.debug("Finish write row {} for test case: {} in table {}".format(i, element["id"], value))
                    if i < len(r.json())-1:   # avoid adding extra line at the end of table
                        self.doc.tables[value].add_row()
                        logging.debug("add row")
                self.change_table_font(self.doc.tables[value], 9)

    def get_step_expected_result(self, test_case):
        list_of_expected_result = []
        try:
            for i in test_case['custom_steps_separated']:
                if i['expected'] != "":
                    list_of_expected_result.append(i['expected'])
                    return "\n".join(list_of_expected_result)
        except TypeError:
            return "No expected result defined in step"

    def save_doc(self):
        self.doc.save(self.config["output doc name"])
        logging.debug("File saved {}".format(self.config["output doc name"]))


if __name__ == "__main__":
    o = Create_csv_doc('martin.carufel@dental-wings.com', '18,Mac&Amo')
    if o.config["use CSV template"]:
        o.get_child_section_id(o.testrail_parent_id)
    o.docx_table_filling()
    o.save_doc()


