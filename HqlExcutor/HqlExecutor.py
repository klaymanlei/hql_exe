#!/usr/bin/python2.6
#coding=utf8

import database

class HqlExecutor:
    def __init__(self):
        self.database = database.Database()

    def log(self, info):
        print info

    def fetch_jobs(self):
        sql = """
            select * from test_presto_jobs    
        """
        jobs = []
        for row in self.database.query(sql):
            try:
                job = self.createJob(row)
                jobs.append(job)
            except Exception, e:
                print e
        return jobs

    def createJob(self, row):
        job = {'job_id':row[0], 'job_name':row[1], 'param':eval(str(row[2])), 'log_id':row[3], 'job_type':row[5], 'task_list':row[4], 'email':row[6],
            'job_source':row[8], 'create_user': row[9], 'push_name':row[10], 'rsync_dest': row[11], 'rsync_pwd':row[12]
        }
        return job

    def runJobs(self, q):
        while True:
            try:
                job = q.get()
                self.log("run job: %s" % job['job_id'])
                jobObj = jobType.JobType(job)
                jobObj.run()
            except Exception, e:
                print e

