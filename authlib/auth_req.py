"""
frontreq.create
~~~~~~~~~~~~~~~~~~~~

This class contains all the create service related front end request calls
"""

import json

from .common_lib import sm_common_header, urls


class AuthRequest:

    def __init__(self, request_obj):
        """
        initialize the class.

        based on existing session object create class object gets initialized

        :param request_obj: (optional)   existing common session object to manage and persist settings across requests
        """

        self.request_obj = request_obj

    def verify_token(self, token):
        """
        :func:`question_autocomplete` load auto complete data

        :param token:    `string/int` survey id
        :return: returns front request response with details like http_code, html etc.
        :rtype: `dict`

        # url: '/user/verify-email/?sm={}'
        response = self.request_obj._get(
          urls.userweb_urls['user_verify_email']['url'].format(email_token),
          urls.userweb_urls['user_verify_email']['name'],
          headers=sm_common_header())
        """

        if token:
            payload = {
                'token': token
            }
            response = self.request_obj._post(
                urls['verify_user_token']['url'],
                json.dumps(payload),
                headers=sm_common_header())
            return response
        else:
            return {"status": "ERROR", "err_msg": "Please enter user token"}


