import winreg
import os
import sys
import shutil
import subprocess

print("知乎 @LeoLeeYM 开发，项目在Github开源，地址：https://github.com/LeoLeeYM/WXFileRWU")
wxpath = input("请输入您的微信文件地址：")

c_drive = os.getenv("SystemDrive")
config_content = wxpath

with open(os.path.join(c_drive, "/wxfilerwu.ini"), "w") as file:
    if config_content[-1] == '\\' or config_content[-1] == '/':
        file.write(config_content)
    else:
        file.write(config_content + '\\')


try:
    startup_folder = os.path.expanduser('~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
    shutil.copy(os.getcwd() + "/" + 'wxfilerwu.exe', startup_folder)

    exe_path = startup_folder.replace('/','\\') + '\\wxfilerwu.exe'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers",
                                0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, exe_path, 0, winreg.REG_SZ, "~ RUNASADMIN")
    winreg.CloseKey(key)
except:
    input("权限不足，请以管理员权限运行本程序，按回车退出...")

input("安装成功，按回车键退出安装程序，程序将在重启后生效...")