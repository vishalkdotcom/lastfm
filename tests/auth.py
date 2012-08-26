# -*- coding: utf-8 -*-
from src.auth import Auth
from nose.tools import assert_equal
from nose.tools import assert_true
from secrets import mysession


class TestAuth():

    def setup(self):
        """ Execute for every test case """
        self.auth = Auth(mysession)

    def test_get_token(self):
        """ Testing the token request """
        auth = Auth()
        token = auth.getToken()
        assert_true(isinstance(token, basestring))
        assert_equal(len(token), 32)

    def test_signature_generation(self):
        """ Testing the signature generation from Auth class """
        data = {'method': "falsemethodfortest", 'limit': "10"}
        signature = self.auth.sign(data)
        assert_true(isinstance(signature, basestring))
        assert_equal(len(signature), 32)

    def test_get_user_session(self):
        """ Testing the user session request """
        session = self.auth.get_session()
        assert_true(isinstance(session, basestring))
        assert_equal(len(session), 32)
