import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), '..', 'config/config.ini')

cfg = configparser.ConfigParser()  # 创建配置对象
cfg.read(config_path)  # 用read方法读取

print(cfg.get('path', 'CASE_DATA_PATH'))