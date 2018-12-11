#!/usr/bin/python

import shell

class PrestoTask:

    def __init__(self, data):
        self.data = data
        self.basedir = "/data0/temp/suda_rpt/auto_job"
    def run(self):
        sh = shell.Shell()
        #pt="/data0/temp/suda_rpt/auto_job/20180322165658440_531732.sql"
        #print pt
        #self.errfile = open(pt, 'w')
        
	#self.errfile.write('%s;' % (self.data['data']['hql'],))
	#self.errfile.flush()
        cmd = 'presto --server 10.39.66.21:8080 --catalog hive --schema default --execute "' + self.data['data']['hql'] +'"'
        print cmd
        code = sh.run(cmd, self.data['outfile'], self.data['errfile'])
        return code

if __name__ == '__main__':
    #type = HiveTask({'outfile':'out.txt', 'errfile':'err.txt', 'data':{'hql':"select count(1) from f_suda_log where dt='2013-07-04' and channel='news'"}})
    type = PrestoTask({'psqlfile':'/home/loganalysis/log/test.sql','outfile':'/home/loganalysis/log/out.txt', 'errfile':'/home/loganalysis/log/err.txt', 'data':{'hql':"select count(1),count(distinct ustat) from ods_mbportal_suda where dt='20180320' and type='wap_valid'"}})
    print type.run()
