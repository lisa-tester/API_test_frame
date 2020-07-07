import logging

# 创建对象
logger = logging.getLogger("logger")
# 设置日志级别 DEBUG10,INFO20,30,40,50
logger.setLevel(10)  # 全局日志级别
# 日志打印到控制台
handler1 = logging.StreamHandler()
handler1.setLevel(10) #局部
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")  # 输入日志格式
handler1.setFormatter(formatter)
logger.addHandler(handler1)

# 文本输出
handler2 = logging.FileHandler('./test.log', 'a', encoding='utf-8')  # 从当前目录生成test.log文件，以追加格式写入文件
handler2.setLevel(logging.DEBUG)
handler2.setFormatter(formatter)
logger.addHandler(handler2)

logger.info("hello")