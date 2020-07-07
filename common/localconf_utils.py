import configparser
"""
config配置：方式一
直接取：比较简单


PS：方法统一 要不小写  要不大写
"""
import os
import configparser

current_path = os.path.dirname(os.getcwd())

config_path = os.path.join(current_path, '..', 'config/config.ini')
print(config_path)



class LocalconfUtils():
    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)

    @property   # 用修饰器@property把方法变为属性方法，调用直接写成local_conf.URL
    def URL(self):
        """获取URL值"""
        url_value = self.cfg.get('default','URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        """获取CASE_DATA_PATH值"""
        case_data_path_value = self.cfg.get('path','CASE_DATA_PATH')
        return case_data_path_value

    @property
    def LOG_PATH(self):
        """获取LOG_PATH值"""
        log_path_value = self.cfg.get('path','LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        """获取LOG_LEVEL值"""
        log_level_value = int( self.cfg.get('log','LOG_LEVEL') )
        return log_level_value


# 全局变量对象，在其他模块直接调用就好，不需要再次创建对象
local_conf = LocalconfUtils()

if __name__ == "__main__":
    print(local_conf.CASE_DATA_PATH)  #local_conf.URL()/local_conf.URL