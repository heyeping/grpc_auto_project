#@project:  grpc_auto_project
#@author: heyeping
#@file: test_login.py
#@ide: PyCharm
#@time: 2021/4/14 5:20 PM

import pytest
import os,sys
from buf_grpc import Auth_pb2
from buf_grpc import Auth_pb2_grpc
import grpc
#from util.Op_config import Config

@pytest.mark.usefixtures("test_init_channel")
class TestLoginClient():

    # def __init__(self, test_init_channel):
    #     self.stub = Auth_pb2_grpc.AuthServiceStub(test_init_channel)
    #     print(self.stub)

    def test_sendCode(self, test_init_channel):
        self.stub = Auth_pb2_grpc.AuthServiceStub(test_init_channel)
        response = self.stub.sendVerificationCode(Auth_pb2.VerificationCodeReq(phone="13267925075"))
        result = response.result
        print(result)
        return result

    def test_login(self, test_init_channel):
        self.stub = Auth_pb2_grpc.AuthServiceStub(test_init_channel)
        response = self.stub.login(Auth_pb2.LoginReq(phone="13267925075", verificationCod="123456"))
        print(response)

if __name__ == '__main__':
    pytest.main()