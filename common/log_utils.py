import os
import logging
import time


current_path = os.path.dirname(__file__)
# 日志存放路径
log_path = os.path.join(current_path, '..', 'logs')


class LogUtils():
    def __init__(self, log_path=log_path):
        self.log_name = os.path.join(log_path, 'ApiTest_%s.log' % time.strftime('%Y_%m_%d'))  # 日志文件名格式设置
        self.logger = logging.getLogger("ApiTestLog")
        self.logger.setLevel(10)

        console_handler = logging.StreamHandler()  # 控制台输出
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 文件输出
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")  # 从当前目录生成test.log文件，以追加格式写入文件
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()  # 防止打印日志重复
        file_handler.close()     # 防止打印日志重复

    def get_logger(self):
        return self.logger


logger = LogUtils().get_logger()   # 防止打印日志重复

if __name__ == '__main__':
    logger.info('hello')
