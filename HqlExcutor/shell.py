#!/usr/bin/python2.6
#coding=utf8

import subprocess
import threading

#执行命令行(如hive,shell)
#stdout用线程读取
#stderr直接输出
class Shell:

        def write_to_file(self, p, pipe, file):
                f = open(file, 'a')
                for line in pipe:
                        line = line.rstrip('\r\n')
                        f.write(line+'\n')
                f.close()

        def run(self, cmd, stdout, stderr):
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		#stderr
                t1 = threading.Thread(target=self.write_to_file, args=(p, p.stdout, stdout))
                t1.start()
		#stderr
		f = open(stderr, 'a')
		while True:
                       line = p.stderr.readline()
                       if line == '' and p.poll() != None:
                                break

                       line = line.rstrip()
                       if line:
				f.write(line+'\n')
				f.flush()
		f.close()
                return p.returncode

if __name__ == '__main__':
        shell = Shell()
        #code = shell.run("hive -e \"select * from f_suda_log where dt='2013-07-03' and channel='www' limit 10\"", 'out.txt', 'err.txt')
        #code = shell.run("hive -e \"desc f_suda_log\"", 'out.txt', 'err.txt')
        code = shell.run("hive -e \"select sum(a1) a1,sum(a2) a2,sum(a3) a3,sum(a4) a4,sum(a5) a5,sum(a6) a6,sum(a7) a7,sum(a8) a8,sum(a9) a9,sum(a10) a10,sum(a11) a11,sum(a12) a12,sum(a13) a13,sum(a14) a14,sum(b1) b1,sum(b2) b2,sum(b3) b3,sum(b4) b4,sum(b5) b5,sum(b6) b6,sum(b7) b7,sum(b8) b8 from weibo_stock_user_stat where dt='20151101';\"", '/usr/home/suda_rpt/log/out.txt', '/usr/home/suda_rpt//log/err.txt')
        print code
