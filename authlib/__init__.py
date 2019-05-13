from .auth_req import AuthRequest
from .common_lib import get_host_details
from .request import RequestBaseClass


class Requests_Holder():
    """
    This Class initialize objects of all service requests at one go.

    How to call:
    request_holder = Requests_Holder(domain)
    return request_holder
    """

    def __init__(self):
        host, domain = get_host_details()
        self._request_obj = RequestBaseClass(domain=host)
        self.auth_obj = AuthRequest(self._request_obj)
