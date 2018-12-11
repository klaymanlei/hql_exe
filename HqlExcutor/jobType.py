#!/usr/bin/python2.6
#coding=utf8

import time

import PrestoTask
import database


class JobType:
    def __init__(self, job):
        self.job = job
        self.database = database.Database()

    def createTask(self, task):
        type = task['task_type']
        #if type == 'hive':
        #    taskObj = hiveTask.HiveTask(task)
        #el
        if type == 'presto':
            taskObj = PrestoTask.PrestoTask(task)
        return taskObj

    def startJob(self, job):
        return None

    def endJob(self, job):
        return None

    def run(self, task):
        taskObj = self.createTask(task)
        code = taskObj.run()
        if code != 0:
            task['status'] = 'S'
            error = True
        else:
            # task
            task['end_date'] = time.time()
            task['status'] = 'E'

