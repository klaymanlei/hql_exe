# coding:utf-8
import sys
import traceback

import MySQLdb
import sqls
from util.config_script import *

reload(sys)
sys.setdefaultencoding('utf8')

#def fetch_holding(date_start, date_end=''):
#    if date_end == '':
#        date_end = date_start
#    try:
#        hlds = []
#        sql = sqls.get_sql('hld_by_day', date_start, date_end)
#        # print sql
#        rows = query(sql)
#        # print rows
#        for row in rows:
#            hld = holding()
#            hld.date = row[0]
#            hld.portfolio = row[1]
#            hld.code = row[2]
#            hld.sec_type = row[3]
#            hld.quantity = float(row[4])
#            hld.amount = float(row[5])
#            hlds.append(hld)
#        # print hlds
#        return hlds
#    except Exception, e:
#        print "Error occured"
#        traceback.print_exc()

def delete_hld(date_start, date_end):
    try:
        sql = sqls.get_sql('delete_hld_by_day', date_start, date_end)
        update(sql)
    except Exception, e:
        traceback.print_exc()

def save_hld(hlds):
    try:
        sql_template = sqls.sql_dict['save_hld']
        for (portfolio, code), hld in hlds.items():
            sql = sql_template % hld.to_tuple()
            # print sql
            update(sql)
    except Exception, e:
        traceback.print_exc()

def hld_load_data(path, date_start, date_end):
    load_data(path, 't_holding', date_start, date_end)

def load_data(path, table, date_start, date_end):
    try:
        sql_template = sqls.sql_dict['load_data']
        sql = sql_template % (path, table)
        print sql
        update(sql)
    except Exception, e:
        traceback.print_exc()

def delete_ast(date_str):
    try:
        sql = sqls.get_sql('delete_ast_by_day', date_str)
        update(sql)
    except Exception, e:
        traceback.print_exc()

def save_exe(execute):
    try:
        sql_template = sqls.sql_dict['save_execute']
        sql = sql_template % execute.to_tuple()
        update(sql)
    except Exception, e:
        traceback.print_exc()

def query(sql):
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close()
    return rows

def update(sql):
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def connect():
    db = MySQLdb.connect(
        host=DB_SERVER,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PW,
        charset='utf8',
        db=DB
    )
    return db

