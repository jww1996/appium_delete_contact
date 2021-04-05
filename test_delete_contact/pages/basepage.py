from typing import Dict, List

import allure
import yaml
import json

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_delete_contact.conftest import root_log


class BasePage:


    # value 替换的变量，类型为字典，要替换的内容放在字典里
    _params = {}

    # 黑名单
    _black_list = [(MobileBy.ID, "com.tencent.wework:id/gu_")]

    # 黑名单查找最大次数
    _max_num = 3
    # 初始值
    _error_num = 0

    _eles1 = []  # 删除前的元素列表
    _eles2 = []  # 删除后的元素列表


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        root_log.info(f"find: by={by}, locator = {locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            return element
        except Exception as e:
            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            # 每次进except进行+1操作
            self._error_num += 1
            # 对黑名单进行遍历
            for black in self._black_list:
                # 如果找到黑名单，传入black，进行解元组
                # find_elements会返回元素的列表[element1,element2...]，如果没有元素返回空列表
                elements = self.driver.find_elements(*black)
                # 如果黑名单长度大于0
                if len(elements) > 0:
                    # 取出找到的第一个元素，点击
                    elements[0].click()
                    # 找到后跳出循环
                    return self.find(by, locator)

            # 如果黑名单处理完没有找到想要的元素，则抛出异常
            raise e

    # 查找点击
    def find_click(self, by, locator):
        return self.find(by, locator).click()

    # 输入
    def find_sendkeys(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def swip_click(self, text):
        """
        滑动查找
        :param text: 需要查找的text值
        :return:
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def wait_click(self, locator):
        """
        显示等待后点击
        :param locator:
        :return:
        """
        element = (MobileBy.XPATH, locator)
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        return ele.click()

    def steps(self, path, fun_name):
        """
        path -> 路径
        :param path:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            # 读取
            # steps :list[dict]作用跟driver: WebDriver类似，告诉编译器提供对应的方法
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]

            # json 序列化和反序列化
            # json.dumps() 序列化 python对象转化为字符串
            # json.loads（）反序列化 python字符串转化为python对象
            # ${"+key+"} 为自己设置的识别格式
            # raw = json.dumps(steps)
            # for key, value in self._params.items():
            #     raw = raw.replace("${"+key+"}", value)
            # steps = json.loads(raw)

            for step in steps:
                if step["action"] == "find_click":
                    self.find_click(step["by"], step["locator"])

                if step["action"] == "swip_click":
                    self.swip_click(step["text"])

                if step["action"] == "wait_click":
                    self.wait_click(step["locator"])

                if step["action"] == "find_sendkeys":
                    # value: ”{value}“ --> 可以从python的变量中取值
                    # content: str 提供字符串相关的方法
                    value: str = step["value"]

                    for param in self._params:
                        # 如果里面有指定的”{value}“，替换为现有的变量（现有的变量可以在上面自行定义）
                        # 如果yaml文件中”{value}“命中了_params中的字典中的某一个值时，把字典中的value替换为yaml中的value
                        value = value.replace("${"+param+"}", self._params[param])
                    self.find_sendkeys(step["by"], step["locator"], value)



