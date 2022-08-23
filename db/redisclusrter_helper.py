# -*- coding: utf-8 -*-
# @author:六柒
# @time  :2019-10-10 11:52:10
from rediscluster import RedisCluster


class RedisClusterHelper(object):
    def __init__(self):
        redis_nodes = [{'host': '107.150.103.97', 'port': 7000},
                       {'host': '107.150.105.125', 'port': 7001},
                       {'host': '107.150.105.113', 'port': 7002},
                       {'host': '107.150.103.97', 'port': 7003},
                       {'host': '107.150.105.125', 'port': 7004},
                       {'host': '107.150.105.113', 'port': 7005}]
        self.rediscluster = RedisCluster(startup_nodes=redis_nodes, password="Changeme_123", skip_full_coverage_check=True)

    def delete(self, name):
        self.rediscluster.delete(name)
        print('redis 数据删除成功')

    def set(self, key, value):
        try:
            self.rediscluster.set(key, value)
            print('redis集群插入数据:', 'success')
            return True
        except:
            print('redis集群插入数据:', 'failure')
            return False

    def get(self, key):
        try:
            value = self.rediscluster.get(key)
            # print('redis集群获取数据%s:' % value, 'success')
            return value
        except:
            # print('redis集群获取数据:', 'failure')
            return False

    def push(self, key, value):
        try:
            self.rediscluster.lpush(key, value)
            print('redis插入成功:', 'Success')
            return True
        except:
            print('redis插入失败:', 'Failure')
            return False

    def pop(self, key):
        try:
            value = self.rediscluster.rpop(key)
            print('redis剔除成功:', 'Success')
            # value值可能为None
            return value
        except:
            print('redis剔除失败:', 'Failure')
            return False

    def get_len(self, key):
        try:
            len = self.rediscluster.llen(key)
            return len
        except Exception as e:
            print('获取redis %s长度过程中报错:' % key, e)


if __name__ == '__main__':
    kk = RedisClusterHelper()
    value = kk.pop('age')
    kk.push('age', 'gbk0')
    kk.get_len('age')
    kk.push('age', 'gbk1')
    kk.get_len('age')
    kk.push('age', 'gbk2')
    kk.get_len('age')
    value1 = kk.pop('age')
    value2 = kk.pop('age')
    print(value)
    print(value1)
    print(value2)
    while True:
        value = input("是否继续?YorN")
        if value == 'N' or 'n':
            value = kk.pop('age')
            kk.get_len('age')
            # print(value.decode())
            print(value)
        else:
            value = kk.pop('age')
            print(value)
