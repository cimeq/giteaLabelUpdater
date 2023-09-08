import os
import giteapy


class LabelMigrator:
    def __init__(self, host_api, git_token, source_organisation):
        self.ref_organisation = source_organisation
        self.configuration = giteapy.Configuration()
        self.configuration.api_key['access_token'] = git_token
        self.configuration.host = host_api

    def test(self):
        api_instance = giteapy.MiscellaneousApi(giteapy.ApiClient(self.configuration))
        api_response = api_instance.get_version()
        print(api_response)
