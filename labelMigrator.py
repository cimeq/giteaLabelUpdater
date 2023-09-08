import os
import giteapy
from pprint import pprint
from thefuzz import fuzz
from thefuzz import process

testOrg = "testOrg"

class LabelMigrator:
    def __init__(self, host_api, git_token, source_organisation):
        self.ref_organisation = source_organisation
        self.configuration = giteapy.Configuration()
        self.configuration.api_key['access_token'] = git_token
        self.configuration.host = host_api

    def __get_all_org(self) -> list:
        result = list()
        api_instance = giteapy.OrganizationApi(giteapy.ApiClient(self.configuration))
        api_response = api_instance.org_get_all()
        for response in api_response:
            result.append(response.name)
        return result

    def __get_ref_label(self, organisation: str):
        api_instance = giteapy.OrganizationApi(giteapy.ApiClient(self.configuration))
        api_response = api_instance.org_list_labels(organisation)
        return api_response

    def process(self):
        list_of_organisation = self.__get_all_org()
        list_of_organisation.remove(self.ref_organisation)

        for target_organisation in list_of_organisation:
            self.__process_organisation(target_organisation)
        # Next we need to foreach all org and compare with specific label reference

    def __process_organisation(self, target_organisation):
        label_from_source = self.__get_ref_label(self.ref_organisation)
        label_from_target = self.__get_ref_label(testOrg)

        for referenceLabel in label_from_source:
            referenceLabel.id = 0  # use id to mark when it's added

        for referenceLabel in label_from_source:
            result = self.__find_label_in_pool(referenceLabel, label_from_target)
            if result:
                referenceLabel.id = 1  # use id to mark when it's added
                print("UPDATE: {} -> {} ".format(result, referenceLabel.name))

        for referenceLabel in label_from_source:
            if referenceLabel.id != 1:
                print("CREATE: {}".format(referenceLabel.name))

    def __find_label_in_pool(self, reference_label, target_labels) -> str | None:
        list_label_from_target = list()
        for target_label in target_labels:
            list_label_from_target.append(target_label.name)
        result = process.extract(reference_label.name, list_label_from_target, limit=1)[0]

        accuracy = result[1]
        if accuracy > 70:
            # print("match({}) {} ~= {}".format(accuracy, reference_label.name, result[0]))
            return result[0]
        # print("no match for {}".format(reference_label.name))
        return None

    def test(self):
        self.__process_organisation(testOrg)

        # pprint(labelFromSource)
