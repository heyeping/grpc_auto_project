#@project:  grpc_auto_project
#@author: heyeping
#@file: test_login.py
#@ide: PyCharm
#@time: 2021/4/14 5:20 PM

import pytest
import os,sys
from loguru import logger
from buf_grpc import Auth_pb2
from buf_grpc import Auth_pb2_grpc
import grpc
from conftest import init_channel
#from util.Op_config import Config

#@pytest.mark.usefixtures("test_init_channel")
class TestLoginClient():

    def setup_class(self):
        """
        链接rpc服务器，调用Auth服务
        :return:
        """
        self.channel = init_channel()
        self.stub = Auth_pb2_grpc.AuthServiceStub(self.channel)

    @pytest.mark.skip
    def test_sendCode(self):
        #self.stub = Auth_pb2_grpc.AuthServiceStub(test_init_channel)
        response = self.stub.sendVerificationCode(Auth_pb2.VerificationCodeReq(phone="13267925075"))
        result = response.result
        print(result)
        return result

    @pytest.mark.parametrize("phone,verificationCode", [{"13267925075","446711"}])
    def test_login(self, phone, verificationCode):
        response = self.stub.login(Auth_pb2.LoginReq(phone=phone, verificationCode=verificationCode))
        print(response)
        assert response.expireTime != 0

if __name__ == '__main__':
    pytest.main(["-vs", 'test_login.py'])