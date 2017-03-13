#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''Tests for our URL endpoints titles.'''

import os.path
import sys
import unittest

# Add webcompat module to import path
sys.path.append(os.path.realpath(os.pardir))
import webcompat

# Any request that depends on parsing HTTP Headers (basically anything
# on the index route, will need to include the following: environ_base=headers
headers = {'HTTP_USER_AGENT': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; '
                               'rv:31.0) Gecko/20100101 Firefox/31.0')}


class TestURLs(unittest.TestCase):
    def setUp(self):
        webcompat.app.config['TESTING'] = True
        self.app = webcompat.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        '''Page title format for different URIs.'''
        issueNum = '1000'
        defaultTitle = 'Web Compatibility'
        website_uris = [
            ('/', defaultTitle),
            ('/about', 'About'),
            ('/contributors', 'Contributors'),
            ('/tools/cssfixme', 'CSS Fix Me'),
            ('/issues/' + issueNum, 'Issue #' + issueNum),
            ('/issues', 'Issues'),
            ('issues/new', 'New Issue'),
            ('/privacy', 'Privacy Policy'),
            ('/404', defaultTitle)
        ]
        for uri, title in website_uris:
            rv = self.app.get(uri, environ_base=headers)
            expected = '<title>{title} | webcompat.com</title>'.format(
                title=title)
            self.assertTrue(expected in rv.data)

if __name__ == '__main__':
    unittest.main()
