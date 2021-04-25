#@project:  grpc_auto_project
#@author: heyeping
#@file: test_device2.py.py
#@ide: PyCharm
#@time: 2021/4/22 3:58 PM

import pytest,os
from clientFiles.Device_client import Device_client
from conftest import init_channel
import allure

@allure.feature('设备相关接口')
class TestDevice():

    def setup_class(self):
        self.base_url = os.path.abspath(os.path.dirname(os.getcwd()))
        self.yamlFile = os.path.join(self.base_url, 'config', 'token.yaml')
        self.dc = Device_client(self.yamlFile)

    @allure.story("正向：绑定设备")
    def test_bindDevice_01(self):
        """
        正向绑定设备
        :return:
        """
        res = self.dc.binDevice(0, "AC000W017943747", "hyp")
        #print(res)
        assert res

    @allure.story("设备名称为空")
    def test_bindDevice_02(self):
        """
        设备名称为空或超过限制
        :return:
        """
        res = self.dc.binDevice(0, "AC000W017943747", "")
        #print(res)
        assert "device nickname is invalid" in res

    @allure.story("deviceId为空")
    def test_bidDevice_03(self):
        """
        deviceId为空
        :return:
        """
        res = self.dc.binDevice(0, "", "jj")
        assert "server error" in res

    def test_bindDevice_04(self):
        """
        错误的deviceId
        :return:
        """
        res = self.dc.binDevice(0, "3233", "jj")
        assert "server error" in res

    def test_bindDevice_05(self):
        """
        设备名称超过限制（32个字）
        :return:
        """
        res = self.dc.binDevice(0, "AC000W017943747", "我是一个很可爱哭的人额外加肥加呢惹人惹人惹惹我惹温柔惹人额惹惹惹人")
        # print(res)
        assert "device nickname is invalid" in res

    def test_getDeviceList_01(self):
        """
        设备列表
        :return:
        """
        res = self.dc.getDeviceList()
        #print(res)
        assert "devices" in res

    def test_getDeviceInfo_01(self):
        """
        不符合规范的deviceId
        :return:
        """
        res = self.dc.getDeviceInfo("12323")
        assert "server error" in res

    def test_getDeviceInfo_02(self):
        """
        绑定在其他账号下的deviceId
        :return:
        """
        res = self.dc.getDeviceInfo("AC000W017956112")
        print(res)
        assert "server error" in res

    def test_getDeviceInfo_03(self):
        """
        正向获取设备信息
        :return:
        """
        res = self.dc.getDeviceInfo("AC000W017943747")
        assert "AC000W017943747" in res

    @pytest.mark.parametrize("deviceId,propertyName,propertyValue",
                             [
                              {"", "Switch_Control", "1"},
                              {"AC000W017943747", "", "1"},
                              {"AC000W017943747", "Switch_Control", ""}
                              ]
                             )
    def test_setDeviceProperty_01(self, deviceId, propertyName, propertyValue):
        """
        数据为空
        :param deviceId:
        :param propertyName:
        :param propertyValue:
        :return:
        """
        res = self.dc.setDeviceProperty(deviceId=deviceId, propertyName=propertyName, propertyValue=propertyValue)
        assert "server error" in res

    def test_setDeviceProperty_02(self, deviceId, propertyName, propertyValue):
        """
        正向的设置设备属性
        :param deviceId:
        :param propertyName:
        :param propertyValue:
        :return:
        """


if __name__ == '__main__':
    base_url = os.path.abspath(os.path.dirname(os.getcwd()))
    reportFile = os.path.join(base_url, 'report')
    #print(reportFile)
    pytest.main(["-vs", 'test_device2.py', f'--alluredir={reportFile}/data'])
    # 本地生成报告
    os.system(f'allure generate {reportFile}/data -o {reportFile}/html --clean')