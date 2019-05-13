"""
This is main class which send actual request to server
"""

import requests
from requests.exceptions import RequestException


class RequestBaseClass:
    """
    Master class that will pass through to python-requests depending on usage.

    If we use WebFrontEndRequests style, it goes to the request_obj, then python-requests.
    IF we user Locust.io, it goes to locust, then to python-requests.
    """

    def __init__(self, domain):
        """
        Initialize the class.

        Input:
            domain: It's the base url to create request object.



        Note for the _Methods called:

        Since we are wrapping around the python-requests and requiests-sessions,
        It might be prudent to have the accepted items as of python-requests 2.19:
        Here is a subset we commonly use from the requests documentation:

        https://github.com/requests/requests/blob/master/requests/models.py#L199
        :param method:  HTTP method to use.
        :param url:     URL to send.
        :param headers: dictionary of headers to send.
        :param files:   dictionary of {filename: fileobject} files to multipart upload.
        :param data:    the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.

        :param json:    json for the body to attach to the request (if files or data is not specified).
        :param params:  URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.

        :param auth:    Auth handler or (user, pass) tuple.
        :param cookies: dictionary or CookieJar of cookies to attach to this request.

        """
        self.domain = domain
        self.request_ob = requests

    def _post(self, url, data, headers=None, params=None, **requests_kwargs):
        """
        POST request.

        Gets passed to requests_obj(python-requests),
        via _do_request.
        """
        return self._do_request(
            'POST',
            url,
            data,
            headers=headers,
            params=params,
            **requests_kwargs
        )

    def _get(self, path, name, data=None, headers=None, params=None, **requests_kwargs):
        """
        GET request.

        Gets passed to requests_obj(python-requests),
        via _do_request.
        """
        return self._do_request(
            'GET',
            path,
            data=data,
            headers=headers,
            params=params,
            **requests_kwargs
        )

    def _put(self, path, name, data=None, headers=None, params=None, **requests_kwargs):
        """
        PUT request.

        Gets passed to requests_obj(python-requests),
        via _do_request.
        """
        return self._do_request(
            'PUT',
            path,
            data=data,
            headers=headers,
            params=params,
            **requests_kwargs
        )

    def _patch(self, path, name, data=None, headers=None, params=None, **requests_kwargs):
        """
        PATCH request.

        Gets passed to requests_obj(python-requests).
        """
        return self._do_request(
            'PATCH',
            path,
            data=data,
            headers=headers,
            params=params,
            **requests_kwargs
        )

    def _delete(self, path, name, data=None, headers=None, params=None, **requests_kwargs):
        """
        DELETE request.

        Gets passed to requests_obj(python-requests).
        """
        return self._do_request(
            'DELETE',
            path,
            data=data,
            headers=headers,
            **requests_kwargs
        )

    def _do_request(self, method, url, data=None, headers=None, params=None, **requests_kwargs):
        """
        Common function which process all get/post/patch/put/delete requests and return response.

        This is a pass-through that will inevitably hit a python-requests module at the end.
        """
        if data is None:
            data = {}

        try:
            if "https" not in url:
                url = self.domain + url

            if method == 'GET':
                response = self.request_ob.get(url,
                                               data=data,
                                               headers=headers,
                                               params=params,
                                               **requests_kwargs)
            elif method == 'PUT':
                response = self.request_ob.put(url,
                                               data=data,
                                               headers=headers,
                                               params=params,
                                               **requests_kwargs)
            elif method == 'PATCH':
                response = self.request_ob.patch(url,
                                                 data=data,
                                                 headers=headers,
                                                 params=params,
                                                 **requests_kwargs)
            elif method == 'DELETE':
                response = self.request_ob.delete(url,
                                                  data=data,
                                                  headers=headers,
                                                  params=params,
                                                  **requests_kwargs)
            else:

                response = self.request_ob.post(url,
                                                data=data,
                                                headers=headers,
                                                params=params,
                                                **requests_kwargs)

            try:
                response.raise_for_status()
            except RequestException as e:
                print(
                    "request method {} of {} result in response code of {}, "
                    "and with exception as {}".format(
                        method, url, response.status_code, str(e)))
                ret_output = {"response": response,
                              "success": False,
                              "response_text": response.text,
                              "http_status": response.status_code}
            else:
                ret_output = {"response": response,
                              "success": True,
                              "response_text": response.text,
                              "http_status": response.status_code}

        except BaseException:

            raise
        print(ret_output)
        return ret_output
