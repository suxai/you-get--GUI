import sys
from you_get import common

url = input("请输入视频链接:")     # 输入视频链接
directory = input("请输入保存地址:")  # 如果不输入，默认下载到当前目录

sys.argv = ["you_get", "-o", directory, url]  # sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
common.main()                               # 下载
