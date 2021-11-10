""" Slack Module """

import json
import requests

# CONSTANTS
API_ENDPOINT = 'https://slack.com/api'

class Slack:
    """ Slack API wrapper.
    :api_token: Slack API Token
    """
    def __init__(self, api_token):
        """
        Constructor
        """
        self._base_url = API_ENDPOINT
        self._api_token = api_token

    def __generate_headers(self, include_content_type=False):
        """
        Generates headers for the request.
        """
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self._api_token)
        }
        if include_content_type == True:
            headers['Content-Type'] = 'application/json'
        return headers

    def __get_files_upload_api_url(self):
        """
        Gets URL for the files upload API.
        """
        return '{}/files.upload'.format(API_ENDPOINT)

    def __get_post_message_api_url(self):
        """
        Gets URL for the post message API.
        """
        return '{}/chat.postMessage'.format(API_ENDPOINT)

    def send_file(self, channel, file, comment=''):
        """
        Send the specified file to the channel with the comment.
        """
        return requests.post(
            url=self.__get_files_upload_api_url(),
            headers=self.__generate_headers(),
            files={
                'file': (file, open(file, 'rb')),
                'initial_comment': (None, comment),
                'channels': (None, channel),
                'icon_emoji': ':izakaya_lantern:'
            }
        )

    def send_message(self, channel, message, user_name, icon=':izakaya_lantern:'):
        """
        Send the specified file to the channel with the comment.
        """
        params = {
            'channel': channel,
            'username': user_name,
            'text': message,
            'icon_emoji': icon
        }

        return requests.post(
            url=self.__get_post_message_api_url(),
            headers=self.__generate_headers(True),
            data=json.dumps(params)
        )

