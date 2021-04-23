#@project:  ayla_ui_project
#@author: heyeping
#@file: Device_client.py.py
#@ide: PyCharm
#@time: 2021/3/30 4:41 PM
#编译命令：python3 -m grpc_tools.protoc --python_out=../buf_grpc --grpc_python_out=../buf_grpc -I. DeviceService.proto

from util.Op_config import Config
from buf_grpc import DeviceService_pb2
from buf_grpc import DeviceService_pb2_grpc
from clientFiles.Login_client import LoginClient
from google.protobuf.json_format import MessageToJson
import grpc,json,os
from loguru import logger
from util.CertCreate import CertCreate

class Device_client():

    def __init__(self, file):
        """
        链接服务器
        :param address: 服务器地址
        """
        self.cert = CertCreate()
        self.base_usrl1 = os.path.abspath(os.path.dirname(os.getcwd()))
        self.path = os.path.join(self.base_usrl1, 'config', 'testdata.yaml')
        self.address = Config(self.path).readYaml("testhost", "prodAds")
        self.chanel = grpc.secure_channel(self.address, self.cert)
        self.file = file
        # 从yaml文件中读取token
        self.token = Config(self.file).readYaml("common", "token")
        try:
            grpc.channel_ready_future(self.chanel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit('Error connection to server')
        else:
            # 调用gpr服务
            self.stub = DeviceService_pb2_grpc.DeviceServiceStub(self.chanel)
        #调用LogintClient，获取token
        #self.login_client = LoginClient(self.address)
        #self.token = self.login_client.login(phone, verificationCode)
        #print(self.token)

    def binDevice(self, cuId, deviceId, nickName):
        """
        绑定设备接口
        :param cuId: 设备品牌，0为艾拉，1为阿里
        :param deviceId: 设备dsn
        :param nickName: 设备名称
        :return:
        """
        response, call = self.stub.bindDevice.with_call(
            request=DeviceService_pb2.BindDeviceReq(cuId=cuId, deviceId=deviceId, nickName=nickName),
            metadata=(('authorization', self.token),)
        )
        #print(response)
        #print(dict(call.trailing_metadata()))
        #if dict(call.trailing_metadata()) != None:
            #print("11")
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            #return response
            #print("绑定设备成功",response.result)
            return response.result

    def getDeviceList(self):
        """
        获取设备接口
        :return:
        """
        response, call = self.stub.getDeviceList.with_call(
            request=DeviceService_pb2.DeviceListResp(),
            metadata=(('authorization', self.token),)
        )
        #将protobuf对象序列化为JSON
        #response = MessageToJson(response)
        #print(dict(call.trailing_metadata()))
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            response = MessageToJson(response)
            #print("设备列表",response.devices)
            return response

    def getDeviceInfo(self, deviceId):
        """
        获取设备信息
        :param deviceId: dsn
        :return:
        """
        response, call = self.stub.getDeviceInfo.with_call(
            request=DeviceService_pb2.DeviceReq(deviceId=deviceId),
            metadata=(('authorization', self.token),)
        )
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            response = MessageToJson(response)
            print("设备信息",response)
            return response


    def setDeviceProperty(self, deviceId, propertyName, propertyValue):
        """
        设置设备属性
        :param deviceId: 设备dsn
        :param propertyName: 属性名称
        :param propertyValue: 属性值
        :return:
        """
        response, call = self.stub.setDeviceProperty.with_call(
            request=DeviceService_pb2.SetDevicePropertyReq(deviceId=deviceId, propertyName=propertyName, propertyValue=propertyValue),
            metadata=(('authorization', self.token),)
        )
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            #response = MessageToJson(response)
            print("设置属性",response)
            return response

    def getDeviceProperty(self, deviceId, propertyName):
        """
        获取设备属性
        :param deviceId: 设备dsn
        :param propertyName: 属性名称
        :return:
        """
        response, call = self.stub.getDeviceProperty.with_call(
            request=DeviceService_pb2.GetDevicePropertyReq(deviceId=deviceId, propertyName=propertyName),
            metadata=(('authorization', self.token),)
        )
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            #response = MessageToJson(response)
            print("设备属性",response)
            return response

    def getDeviceProperties(self, deviceId):
        """
        获取某个设备全部属性
        :param deviceId: DSN
        :return:
        """
        response, call = self.stub.getDeviceProperties.with_call(
            request=DeviceService_pb2.GetDevicePropertiesReq(deviceId=deviceId),
            metadata = (('authorization', self.token),)
        )
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            #response = MessageToJson(response)
            print("设备全部属性",response)
            return response

    def unBindDevice(self, deviceId):
        """
        解绑设备
        :param deviceId:
        :return:
        """
        response, call = self.stub.unBindDevice.with_call(
            request=DeviceService_pb2.UnBindDeviceReq(deviceId=deviceId),
            metadata=(('authorization', self.token),)
        )
        print(dict(call.trailing_metadata()))

        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            return response.deviceId

    def updateDevice(self, deviceId, nickName):
        """
        编辑设备信息
        :param deviceId:
        :param nickName:
        :return:
        """
        response, call = self.stub.updateDevice.with_call(
            request=DeviceService_pb2.UpdateDeviceReq(deviceId=deviceId, nickName=nickName),
            metadata=(('authorization', self.token),)
        )
        for key in dict(call.trailing_metadata()):
            if "errorcode" in key:
                msg = dict(call.trailing_metadata())["errormsg"]
                return msg
        else:
            #response = MessageToJson(response)
            print("编辑设备信息",response)
            return response

if __name__ == "__main__":
    base_url = os.path.abspath(os.path.dirname(os.getcwd()))
    yamlFile = os.path.join(base_url, 'config', 'token.yaml')
    dc = Device_client(file=yamlFile)
    cuId = 0
    deviceId = "AC000W017943747"
    nickName = "hhh"
    propertyName = "Switch_Control"
    property_value = "1"
    #dc.binDevice(cuId,deviceId,nickName)
    dc.getDeviceList()
    #print(listhh)
    dc.getDeviceInfo(deviceId)
    dc.getDeviceProperties(deviceId)
    dc.setDeviceProperty(deviceId,propertyName,property_value)
    dc.updateDevice(deviceId,nickName)
    dc.unBindDevice(deviceId)

