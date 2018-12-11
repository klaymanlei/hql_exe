#!/usr/bin/python2.6

import MySQLdb

class Database:

	def connect(self, conf):
		self.conf = conf #dbms,host,user,password,database,charset

		if not 'charset' in self.conf:
			self.conf['charset'] = 'utf8'
		self.conn = MySQLdb.connect(host = self.conf['host'], port = self.conf['port'], user = self.conf['user'], passwd = self.conf['password'], db =
self.conf['database'])
		self.execute('set names '+self.conf['charset'])
		self.conn.autocommit(True)
			
        def execute(self, sql, data=()):
                cur = self.conn.cursor()
                cur.execute(sql, data)
                cur.close()

	def query(self, sql, data=()):
		cur = self.conn.cursor()
		cur.execute(sql, data)
		row = cur.fetchone()
		while row:
			yield row
			row = cur.fetchone()
		cur.close()

	def close(self):	
		self.conn.close()

	def insert_id(self):
		return self.conn.insert_id()
