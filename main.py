import os
from labelMigrator import LabelMigrator
import sys

from giteapy.rest import ApiException
from pprint import pprint


def fetch_git_token(token_base_path):
    # token_base_path = os.path.dirname(os.path.abspath(__file__)) + "/"
    token = open(token_base_path + "gitea-token").read().strip()
    return token

def main(arg):
    host = "https://git.cimeq.qc.ca/api/v1"
    org_name = arg[1]
    token = fetch_git_token(os.path.dirname(os.path.abspath(__file__)) + "/")

    label_migrator = LabelMigrator(host, token, org_name)

    try:
        # Returns the Person actor for a user
        label_migrator.process()
    except ApiException as e:
        print("Exception: %s\n" % e)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit(1)
    sys.exit(main(sys.argv) or 0)
