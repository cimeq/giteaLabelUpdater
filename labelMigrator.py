import os
import giteapy
from pprint import pprint
from thefuzz import fuzz

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
        api_response = self.__get_all_org()
        api_response.remove(self.ref_organisation)
        pprint(api_response)
        # Next we need to foreach all org and compare with specific label reference

    def __find_label_in_pool(self, reference_label, target_labels) -> bool:
        for target_label in target_labels:
            accuracy = fuzz.partial_ratio(str(reference_label.name), str(target_label.name))
            if accuracy > 70:
                # print("match({}) {} ~= {}".format(accuracy, reference_label.name, target_label.name))
                return True
        # print("no match for {}".format(reference_label.name))
        return False

    def test(self):
        labelFromSource = self.__get_ref_label(self.ref_organisation)
        labelFromTarget = self.__get_ref_label(testOrg)

        for referenceLabel in labelFromSource:
            referenceLabel.id = 0  # use id to mark when it's added

        for referenceLabel in labelFromSource:
            if self.__find_label_in_pool(referenceLabel, labelFromTarget):
                referenceLabel.id = 1  # use id to mark when it's added
                # print(referenceLabel.name)

        for referenceLabel in labelFromSource:
            if referenceLabel.id == 1:
                print("match {}".format(referenceLabel.name))
            else:
                print("to create {}".format(referenceLabel.name))
        # pprint(labelFromSource)
