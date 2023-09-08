import os
import giteapy
import sys

from giteapy.rest import ApiException
from pprint import pprint


def fetch_git_token(token_base_path):
    # token_base_path = os.path.dirname(os.path.abspath(__file__)) + "/"
    token = open(token_base_path + "gitea-token").read().strip()
    return token

def main(arg):
    configuration = giteapy.Configuration()
    token_base_path = fetch_git_token(os.path.dirname(os.path.abspath(__file__)) + "/")
    configuration.api_key['access_token'] = token_base_path
    configuration.host = "https://git.cimeq.qc.ca/api/v1"

    api_instance = giteapy.MiscellaneousApi(giteapy.ApiClient(configuration))


    try:
        # Returns the Person actor for a user
        api_response = api_instance.get_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MiscellaneousApi->get_version: %s\n" % e)

if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
