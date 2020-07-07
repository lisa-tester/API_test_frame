import os
from common.config_utils import ConfigUtils
"""
只用来取数据
"""
config_path = os.path.join(os.path.dirname(__file__), '..', 'config/config.ini')
# 创建对象
configUtils = ConfigUtils(config_path)
URL = configUtils.read_value('default', 'URL')
CASE_DATA_PATH = configUtils.read_value('path', 'CASE_DATA_PATH')
