# 介绍
这是一个Python库，它可以查看当前的IP地址
# 获取iPv4地址
import cniptest
print(cniptest.ip())
# 获取ipv6地址
import cniptest
print(cniptest.ipv6())
# 检测是否有ipv6，如果有那么就返回ipv6，如果没有就返回iPv4
import cniptest
print(cniptest.test())