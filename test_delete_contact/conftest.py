import logging

root_log = logging.getLogger(__name__)
for h in root_log.handlers[:]:
    root_log.removeHandler(h)
    h.close()

logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    # 打开日志文件的方式
                    filemode='a'
                    )

# #定义写入格式和路径
# logging.basicConfig(filename= 'runlog.log',
#                     format="%(asctime)s ""%(filename)s [line:%(lineno)d] ""%(levelname)s>""%(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S"
#                     ,filemode='a'
#                     )
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# # 创建一个handle输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# # 定义输出的格式
# fmt = "%(asctime)s ""%(filename)s [line:%(lineno)d] ""%(levelname)s>""%(message)s"
# formatter = logging.Formatter(fmt)
# ch.setFormatter(formatter)
# # 添加到handle
# logger.addHandler(ch)
