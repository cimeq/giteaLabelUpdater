import os
import giteapy
from pprint import pprint


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

    def test(self):

        api_response = self.__get_all_org()
        api_response.remove(self.ref_organisation)
        pprint(api_response)
