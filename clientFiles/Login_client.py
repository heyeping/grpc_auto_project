#@project:  ayla_ui_project
#@author: heyeping
#@file: Login_test1.py
#@ide: PyCharm
#@time: 2021/3/30 11:58 AM

import os
from buf_grpc import Auth_pb2
from buf_grpc import Auth_pb2_grpc
import grpc
from util.Op_config import Config
from util.CertCreate import CertCreate

class LoginClient():

    def __init__(self, address):
        """
        链接服务器
        :param address: 服务器地址
        """
        self.cert = CertCreate()
        self.address = address
        self.chanel = grpc.secure_channel(self.address,self.cert)
        # 调用gpr服务
        self.stub = Auth_pb2_grpc.AuthServiceStub(self.chanel)

    def sendCode(self, phone):
        """
        请求验证码接口
        :param phone:手机号
        :return:
        """
        # 请求验证码接口
        response = self.stub.sendVerificationCode(Auth_pb2.VerificationCodeReq(phone=phone))
        #print("返回:", response)
        result = response.result
        print(result)
        #print(type(result))
        return result

    def login(self, phone, verificationCode):
        """
        请求登录接口
        :param phone:账号
        :param verificationCode:验证码
        :return:
        """
        #请求登录接口
        response = self.stub.login(Auth_pb2.LoginReq(phone=phone, verificationCode=verificationCode))
        print(response)
        base_url = os.path.abspath(os.path.dirname(os.getcwd()))
        if 'authToken' in str(response):
            print("登录成功")
            token = str(response.authToken)
            data = {
                "common": {
                    "token": token
                }
            }
            # 把token写入yaml文件中
            yamlFile = os.path.join(base_url, 'config', 'token.yaml')
            Config(yamlFile).writeYaml(data)
        else:
            print("登录失败")

if __name__ == "__main__":
    ads = "referenceapp-test.ayla.com.cn:9098"
    phone = "13267925075"
    verCode = "957858"
    loginTest = LoginClient(ads)
    #loginTest.sendCode("13267925075")
    token = loginTest.login(phone,verCode)
    #print(token)


