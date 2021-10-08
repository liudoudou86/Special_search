# -*- coding:utf-8 -*-
# Author:lz

import os
import subprocess

def search(executable_file):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    # print(desktop_path)
    for root, dirs, files in os.walk(desktop_path):
        for name in files:
            file_path = os.path.join(root, name)
            if executable_file in name:
                # print(os.path.split(file_path))
                # os.popen(file_path)
                proc = subprocess.Popen(
                    file_path,
                    shell=True,
                    bufsize=0,
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT, 
                    stdin=subprocess.PIPE # 重定向输入值
                )
                proc.stdin.close() # 既然没有命令行窗口，那就关闭输入
                proc.wait()
                proc.stdout.close()