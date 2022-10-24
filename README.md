# 介绍
这是一个Python库，它可以查看当前的IP地址
# 安装
输入以下代码
```
pip install cniptest
```
# 获取iPv4地址
输入以下代码
```
import cniptest
print(cniptest.ip())
```
# 获取ipv6地址
输入以下代码
```
import cniptest
print(cniptest.ipv6())
```
# 检测是否有ipv6，如果有那么就返回ipv6，如果没有就返回iPv4
输入以下代码
```
import cniptest
print(cniptest.test())
```