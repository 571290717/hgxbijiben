# -*- coding: utf-8  -*-
# @Author: ty
# @File name: cache.py 
# @IDE: PyCharm
# @Create time: 2/10/21 11:02 PM
# @Description:
from django.conf import settings
from redis import Redis as _Redis
from pickle import dumps, loads


class Redis(_Redis):
    """接口与原生redis接口保持一致, 增加自动序列化, 反序列化"""

    def __init__(self, *args, **kwargs):
        super(Redis, self).__init__(*args, **kwargs)

    # 取出所有的key
    def keys(self, pattern='*'):
        'return a list of  keys matching "pattern"'
        return sorted(_Redis.keys(self, pattern))  # 对结果列表进行了排序

    def set(self, key, value, timeout=0):
        if timeout > 0:
            return self.setex(key, dumps(value, 1), timeout)  # 序列化, 并添加过期时间
        else:
            return _Redis.set(self, key, dumps(value, 1))  # 只进行序列化操作

    # 不存在时设置
    def setnx(self, key, value, timeout=0):
        res = _Redis.setnx(self, key, dumps(value, 1))
        if res and timeout > 0:
            _Redis.expire(self, key, timeout)
        return res

    def get(self, key, default=None):
        value = _Redis.get(self, key)  # 并没有对查询出来的结果进行反序列化
        return default if value is None else value

    # 设置多个值,并使用dumps进行序列化
    def mset(self, mapping):
        return _Redis.mset(self, {k: dumps(v, 1) for k, v in mapping.items()})

    # 获取多个值
    def mget(self, keys, default=None):
        values = _Redis.mget(self, keys)
        return [default if v is None else v for v in values]

    def hset(self, name, key, value):
        return _Redis.hset(self, name, key, dumps(value, 1))

    def hget(self, name, key, default=None):
        value = _Redis.hget(self, name, key)
        return default if value is None else value

    def hmset(self, name, mapping):
        return _Redis.hmset(self, name, {k: dumps(v, 1) for k, v in mapping.items()})

    def hmget(self, name, keys, default=None):
        values = _Redis.hmget(self, name, keys)
        return [default if v is None else v for v in values]

    def pop(self, key, default=None):
        pipe = self.pipeline()
        pipe.get(key)
        pipe.delete(key)
        value, res = pipe.execute()
        return default if value is None or res != 1 else value

    def hpop(self, name, key, default=None):
        pipe = self.pipeline()
        pipe.hget(name, key)
        pipe.hdel(name, key)
        value, res = pipe.execute()
        return default if value is None or res != 1 else value

    def hscan_iter(self, name, match=None, count=None):
        cursor = '0'
        found = []
        while cursor != 0:
            cursor, data = self.hscan(name, cursor=cursor, match=match, count=count)
            for k, v in data.items():
                if k not in found:
                    found.append(k)
                    yield k, v

    # 反序列化
    def unpickle(self, data):
        try:
            # 类型判断
            if isinstance(data, bytes):  # bytes类型
                return loads(data)
            elif isinstance(data, (list, tuple)):  # 列表或元组
                return [self.unpickle(v) for v in data]
            elif isinstance(data, dict):  # 字典类型
                return {k: self.unpickle(v) for k, v in data.items()}
            else:
                return data
        except (UnpickleError, TypeError, ValueError, EOFError):
            return data

    # 从redis中统一的返回出口
    def parse_response(self, connection, command_name, **options):
        'parses a response from the redis server'
        response = _Redis.parse_response(self, connection, command_name, **options)
        return self.unpickle(response)

    # 管道 事务操作
    def pipeline(self, transaction=True, shard_hint=None, origin=False):
        if origin:
            return _Redis.pipeline(self, transaction, shard_hint)
        else:
            return Pipeline(self.connection_pool, self.response_callbacks, transaction, shard_hint)


class Pipeline(BasePipeline, Redis):
    """覆盖原生的Pipeline类"""

    def execute(self, raise_on_error=True):
        result = super(Pipeline, self).execute(raise_on_error)
        return [self.unpickle(data) for data in result]


class MSRedis(object):
    """读写分离客户端"""

    def __init__(self, conf):
        self.master = Redis(**conf['Master'])  # 主机实例
        self.master = Redis(**conf['Slave'])  # 从机实例
        # 读命令
        self.read_commands = [
            'ttl', 'exists', 'expire', 'get', 'keys', 'hget', 'hgetall', 'hkeys', 'hmget',
            'sismember', 'smember', 'sdiff', 'sinter', 'sunion', 'zrevrange', 'zrevrangebyscore', 'zrevrank', 'zscore'
        ]

        # 读写分离的数据库, 写主要发生在主master上, 读发生在从slave上

    def __getattribute__(self, name):
        # 对操作命令进行分流
        if name in ['master', 'slave', 'read_commands']:
            return object.__getattribute__(self, name)
        elif name in self.read_commands:
            return self.slave.__getattribute__(name)
        else:
            return self.master.__getattribute__(name)


rds = MSRedis(settings.REDIS)
