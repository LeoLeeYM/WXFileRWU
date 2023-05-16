微信自从更新3.9.0之后，所有接收的文件全部变成了只读属性，最近正好在写一篇报告，要接收各个项目成员的文件，然后就被这个机制深深的恶心到了...<br>
昨晚实在受不了了，写了个脚本，这个脚本会自动监听微信接收文件夹的文件变动，将新增的文件自动设置为可读可写可执行，使用Python实现，代码放在下面。<br>
对于不会用Python或者懒得折腾的朋友，我也打包了一个一键傻瓜式安装，链接放在底下，需要自取，使用教程也放在后面。
### 一键安装
- 链接：https://pan.baidu.com/s/1lHbKWrb5l7lGJK6FPjzKCQ?pwd=f2pd 
- 提取码：f2pd
### 一键安装的教程
- 下载解压后，以管理员权限运行`install.exe`，在弹出的窗口中输入你的微信文件夹地址
  - 获取微信文件夹地址的方式：
    - 打开微信-左下角三条横线-设置-文件管理-打开文件夹-在弹出的文件夹里打开`FileStorage`文件夹-打开`File`文件夹。
    - 这个文件夹的路径就是你的微信文件夹路径，比如我的就是这样的`H:\SystemFile\Documents\WechatFile\WeChat Files\wxid_3nfz3ftycsxxxx\FileStorage\File `
- 然后回车，显示安装成功，重启电脑即可
### Tips
- 安装过程中因为要设置开机自启动和注册表，杀毒软件可能会阻止，请允许即可，本程序完全开源，不存在任何病毒或者木马
- 安装程序要以管理员身份运行
- 完成上述的步骤，就完成安装啦，每次开机服务会自动启动，全程无感。
### 其他
- 该程序一键安装脚本使用`Pyinstaller`打包，所以会比较大。
- wxfilerwu.py中有一段代码：
  ```python
  with open(os.path.join(c_drive, "/wxfilerwu.ini"), "r", encoding="utf-8") as file: 
      path = file.read()
  path = path
  ```
  这段代码是为了一键安装的功能服务的，如果不需要一键安装服务，可以直接将
  ```python
  with open(os.path.join(c_drive, "/wxfilerwu.ini"), "r", encoding="utf-8") as file: 
      path = file.read()
  ```
  删掉，然后将`path`变量值修改为你的微信文件夹路径即可。
