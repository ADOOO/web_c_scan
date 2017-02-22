# C段WEB服务扫描

这是初版，至扫描80端口，后续增加其它端口
采用gevent和threading两种多线程方式，经过对比，两者效率差不多

使用了第三方库 IPy 用来识别键入的ip地址格式

IPy的安装：`pip install IPy`
