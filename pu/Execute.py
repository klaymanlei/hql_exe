# coding:utf-8
import time

class Execute:
    def __init__(self):
        self.hql = ''
        self.status = ''
        self.create_time = ''
        self.creator = ''

    def to_tuple(self):
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S')
        return (self.hql, self.status, self.create_time, cur_time, self.creator)

