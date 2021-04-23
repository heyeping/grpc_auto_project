#@project:  grpc_auto_project
#@author: heyeping
#@file: test_device.py
#@ide: PyCharm
#@time: 2021/4/14 6:31 PM
import pytest,os
import grpc
from clientFiles import Device_client
from buf_grpc import DeviceService_pb2
from buf_grpc import DeviceService_pb2_grpc
from conftest import init_channel
from util.Op_config import Config

class TestDevice():

    def setup_class(self):
        """
        链接rpc服务器，调用Auth服务
        :return:
        """
        self.channel = init_channel()
        self.stub = DeviceService_pb2_grpc.DeviceServiceStub(self.channel)
        base_url = os.path.abspath(os.path.dirname(os.getcwd()))
        self.file = os.path.join(base_url, 'config', 'token.yaml')
        # 从yaml文件中读取token
        self.token = Config(self.file).readYaml("common", "token")

    @pytest.mark.parametrize("cuId,deviceId,nickName",[{0, "1213", "tests"}])
    def test_bind_device_01(self, cuId, deviceId, nickName):
        """
        错误的deviceId
        :param cuId:0为ayla，1为阿里
        :param deviceId:
        :param nickName:
        :return:
        """

        response, call = self.stub.bindDevice.with_call(
            request=DeviceService_pb2.BindDeviceReq(cuId=cuId, deviceId=deviceId, nickName=nickName),
            metadata=(('authorization', self.token),)
        )
        msg = dict(call.trailing_metadata())["errormsg"]
        print("返回是：", msg)
        assert "server error" in msg

    def test_bind_device_02(self):
        """
        nickName为空：device nickname is invalid
        :return:
        """
        response, call = self.stub.bindDevice.with_call(
            request=DeviceService_pb2.BindDeviceReq(cuId=0, deviceId="121323", nickName=""),
            metadata=(('authorization', self.token),)
        )
        msg = dict(call.trailing_metadata())["errormsg"]
        #print("返回是：", msg)
        assert "device nickname is invalid" in msg

    def test_bind_device_03(self):
        """
        deviceId已被绑定：server error
        :return:
        """
        response, call = self.stub.bindDevice.with_call(
            request=DeviceService_pb2.BindDeviceReq(cuId=0, deviceId="AC000W011316466", nickName="6466"),
            metadata=(('authorization', self.token),)
        )
        msg = dict(call.trailing_metadata())["errormsg"]
        # print("返回是：", msg)
        assert "server error" in msg

    def test_bind_device_04(self):
        """
        正向情况
        :return:
        """



if __name__ == '__main__':
    pytest.main(["-vs", 'test_device.py'])