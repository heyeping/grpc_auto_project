#@project:  ayla_ui_project
#@author: heyeping
#@file: Auth_login_client.py.py
#@ide: PyCharm
#@time: 2021/3/26 2:29 PM

import grpc
from buf_grpc import Auth_pb2
from buf_grpc import Auth_pb2_grpc
from util.CertCreate import CertCreate

def getToken():

    # 获取安全证书
    cert = CertCreate()
    # 连接rpc服务器，不是HTTPS不需要证书可以使用grpc.insecure_channel()
    channel = grpc.secure_channel(target="referenceapp-test.ayla.com.cn:9098", credentials=cert)
    stub = Auth_pb2_grpc.AuthServiceStub(channel)
    #请求登录接口
    response, call = stub.login.with_call(
        Auth_pb2.LoginReq(phone="13267925075", verificationCode="427585")
    )
    ret = dict(call.trailing_metadata())
    print(response)
    print(ret)
    for key, value in call.trailing_metadata():
        print("获取到的key=%s, value=%s" % (key, value))
    #print("authToken:", response.authToken)

if __name__ == '__main__':
    token = getToken()
    print(token)