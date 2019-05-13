import argparse
import os
import socket

try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs

import tldextract
import yaml

__author__ = 'rakesh jain'

content_types = {
    "urlencoded": "application/x-www-form-urlencoded; charset=UTF-8",
    "json": "application/json"
}


# get all url details from configuration/yaml file
def load_urls(path=None):
    realpath = os.path.join(os.path.dirname(__file__), 'config', 'urls.yaml')
    locator_resource = yaml.load(open(realpath))
    print(locator_resource)
    if path:
        locator_resource = locator_resource[path]
    return locator_resource


# get all common configurationn details from configuration/yaml file
def load_all_common_configurations():
    locator_resource = {'default_env': 'mt1',
                        'default_host_name': 'https://www.mercury.com'}
    return locator_resource


urls = load_urls()
common_conf = load_all_common_configurations()

# Global variables
# domain of the test running on
domain = 'www.mercury.com'

# resolved environment, like mt1, or mt1_n9
resolved_env = None


def get_env():
    """
    Used to get the environment shortcut
    """
    global resolved_env
    resolved_env = get_env_from_sysarg()
    print("the resolved_env is {}".format(resolved_env))
    return resolved_env


def get_domain():
    """
    Used to get the middle domain name like monkeytest, surveymonkey etc. without www or com part
    """
    arg_domain = get_domain_from_sysarg()
    ext = tldextract.extract(arg_domain)
    return ext.domain


def get_host_name():
    """
    Used to get the global os.env host name or default configured host name
    """
    host_name, domain = get_host_details()
    return host_name


def get_env_name():
    """
    Used to get the global os.env short env name or default configured env name
    """
    host, domain = get_host_details()

    if host:
        env = get_env_from_sysarg(domain)
    else:
        env = common_conf['default_env']
    return env


def get_host_details():
    """
    Used to get the the domain name like http://127.0.0.1:8000, http://127.0.0.1:8000 etc.
    """
    global domain
    return "http://127.0.0.1:8000", "127.0.0.1:8000"


def get_domain_from_sysarg():
    """
    Used to get the the domain name like www.monkeytest.com, www.surveymonkey.com etc.
    """
    global domain
    host, domain = get_host_details()
    return domain


def get_env_from_sysarg(ext_domain=None):
    """
    get short form of env
    """
    if not ext_domain:
        ext_domain = get_domain_from_sysarg()

    if 'prod' in ext_domain:
        return 'prod'
    elif 'dev' in ext_domain:
        return 'dev'
    elif 'uat' in ext_domain:
        return 'uat'
    else:
        print("Unknown environment: {}".format(domain))
        return ''


def sm_common_header(referee_url=None, content_type=content_types['json'], x_request_with="XMLHttpRequest"):
    """
    common header details that needs to sent by default with front end request
    """
    host = 'http://127.0.0.1:8000'
    headers = {
        "User-Agent": socket.gethostname(),
        "Origin": host,
    }

    if content_type:
        headers["Content-Type"] = content_type

    return headers

# def check_wait(seconds=None):
#     """
#     gevent sleep
#     """
#     if not seconds:
#         seconds = 5
#     gevent.sleep(seconds)
