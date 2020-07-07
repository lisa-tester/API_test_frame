import configparser
"""
config配置：方式一
分2个文件写，用的时候直接调用
由2个文件组合实现
config_utils和config
"""

class ConfigUtils():
    """配置文件操作类"""
    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()  # 创建配置对象
        self.cfg.read(config_path)  # 用read方法读取

    def read_value(self, section, key):
        # 读取配置文件中的数据
        value = self.cfg.get(section, key)
        return value
