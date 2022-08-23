
import random

import redis



class RedisHelper(object):
    """redis的读写封装"""

    def __init__(self, host='localhost', port=6379,
                 db=0, password='123456'):
        self.__redis = redis.StrictRedis(host=host, port=port,
                                         db=db, password=password)

    def get(self, key):
        """获取redis中的数据"""
        if self.__redis.exists(key):
            value = self.__redis.brpop(key)
            return value
        else:
            return ''

    def index(self,key,l=0):
        """
        获取下标为l的键值
        :param key: 键
        :param l: 下标
        :return: 值
        """
        return self.__redis.lindex(key,l)

    def random_pop(self, key):
        """随机返回列表中的一个数据"""
        list_len = random.randint(0,self.get_len(key)-1)
        return self.__redis.lindex(key,list_len)

    def set(self, key, value):
        """redis中存入数据"""
        self.__redis.lpush(key, value)

    def get_len(self, key):
        """
        判断当前redis库的长度
        :param key 相应的key
        """
        current_len = self.__redis.llen(key)
        return current_len

    def remove(self,name,value,count=0):
        """删除相应的cookie"""
        return self.__redis.lrem(name=name,count=count,value=value)
