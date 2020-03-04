# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class MessageTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .messages.create(to="+15558675310")

        values = {'To': "+15558675310", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "body": "Hello! \ud83d\udc4d",
                "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
                "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
                "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
                "direction": "outbound-api",
                "error_code": null,
                "error_message": null,
                "from": "+14155552345",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "num_media": "0",
                "num_segments": "1",
                "price": null,
                "price_unit": null,
                "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "sent",
                "subresource_uris": {
                    "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"
                },
                "to": "+14155552345",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.create(to="+15558675310")

        self.assertIsNotNone(actual)

    def test_create_wo_service_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "body": "Hello! \ud83d\udc4d",
                "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
                "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
                "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
                "direction": "outbound-api",
                "error_code": null,
                "error_message": null,
                "from": "+14155552345",
                "messaging_service_sid": null,
                "num_media": "0",
                "num_segments": "1",
                "price": null,
                "price_unit": null,
                "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "sent",
                "subresource_uris": {
                    "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"
                },
                "to": "+14155552345",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.create(to="+15558675310")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "body": "testing",
                "date_created": "Fri, 24 May 2019 17:18:27 +0000",
                "date_sent": "Fri, 24 May 2019 17:18:28 +0000",
                "date_updated": "Fri, 24 May 2019 17:18:28 +0000",
                "direction": "outbound-api",
                "error_code": 30007,
                "error_message": "Carrier violation",
                "from": "+12019235161",
                "messaging_service_sid": "MGdeadbeefdeadbeefdeadbeefdeadbeef",
                "num_media": "0",
                "num_segments": "1",
                "price": "-0.00750",
                "price_unit": "USD",
                "sid": "SMb7c0a2ce80504485a6f653a7110836f5",
                "status": "sent",
                "subresource_uris": {
                    "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5/Media.json",
                    "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5/Feedback.json"
                },
                "to": "+18182008801",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMb7c0a2ce80504485a6f653a7110836f5.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .messages.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages.json',
        ))

    def test_read_full_page1_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 1,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 2,
                "previous_page_uri": null,
                "messages": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "body": "testing",
                        "date_created": "Fri, 24 May 2019 17:44:46 +0000",
                        "date_sent": "Fri, 24 May 2019 17:44:50 +0000",
                        "date_updated": "Fri, 24 May 2019 17:44:50 +0000",
                        "direction": "outbound-api",
                        "error_code": null,
                        "error_message": null,
                        "from": "+12019235161",
                        "messaging_service_sid": null,
                        "num_media": "0",
                        "num_segments": "1",
                        "price": "-0.00750",
                        "price_unit": "USD",
                        "sid": "SMded05904ccb347238880ca9264e8fe1c",
                        "status": "sent",
                        "subresource_uris": {
                            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Media.json",
                            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c/Feedback.json"
                        },
                        "to": "+18182008801",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMded05904ccb347238880ca9264e8fe1c.json"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "body": "look mom I have media!",
                        "date_created": "Fri, 24 May 2019 17:44:46 +0000",
                        "date_sent": "Fri, 24 May 2019 17:44:49 +0000",
                        "date_updated": "Fri, 24 May 2019 17:44:49 +0000",
                        "direction": "inbound",
                        "error_code": 30004,
                        "error_message": "Message blocked",
                        "from": "+12019235161",
                        "messaging_service_sid": null,
                        "num_media": "3",
                        "num_segments": "1",
                        "price": "-0.00750",
                        "price_unit": "USD",
                        "sid": "MMc26223853f8c46b4ab7dfaa6abba0a26",
                        "status": "received",
                        "subresource_uris": {
                            "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Media.json",
                            "feedback": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26/Feedback.json"
                        },
                        "to": "+18182008801",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/MMc26223853f8c46b4ab7dfaa6abba0a26.json"
                    }
                ],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=2&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_read_empty_sentdate_less_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3C=2008-01-02&PageSize=25&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 25,
                "previous_page_uri": null,
                "messages": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3C=2008-01-02&PageSize=25&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_read_empty_sentdate_equals_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent=2008-01-02&PageSize=25&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 25,
                "previous_page_uri": null,
                "messages": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent=2008-01-02&PageSize=25&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_read_empty_sentdate_greater_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=25&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 25,
                "previous_page_uri": null,
                "messages": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2008-01-02&PageSize=25&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_read_empty_sentdate_greater_format1_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=06%2F11%2F2019+22%3A05%3A25+MST&PageSize=25&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 25,
                "previous_page_uri": null,
                "messages": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=06%2F11%2F2019+22%3A05%3A25+MST&PageSize=25&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_read_empty_sentdate_greater_format2_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2019-06-11+22%3A05%3A25.000&PageSize=25&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 25,
                "previous_page_uri": null,
                "messages": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=2019-06-11+22%3A05%3A25.000&PageSize=25&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_read_empty_sentdate_greater_format3_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=Wed%2C+19+Jun+2019+22%3A04%3A00+-0000&PageSize=25&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 25,
                "previous_page_uri": null,
                "messages": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages.json?To=%2B123456789&From=%2B987654321&DateSent%3E=Wed%2C+19+Jun+2019+22%3A04%3A00+-0000&PageSize=25&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(body="body")

        values = {'Body': "body", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "body": "Hello, this is trash Benson cut and pasted and probably does not do anything useful! \ud83d\udc4d",
                "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
                "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
                "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
                "direction": "outbound-api",
                "error_code": null,
                "error_message": null,
                "from": "+14155552345",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "num_media": "0",
                "num_segments": "1",
                "price": "-0.00750",
                "price_unit": "USD",
                "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "sent",
                "subresource_uris": {
                    "media": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media.json"
                },
                "to": "+14155552345",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .messages("MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(body="body")

        self.assertIsNotNone(actual)
