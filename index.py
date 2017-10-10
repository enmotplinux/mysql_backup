#!/usr/local/bin/python3.5
import os,time,sys,time
import oss2

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  lib import innodb_backup as lib_innodb_backup

def upload(host,user,password,port,my_conf):
    abc=lib_innodb_backup.backup(host,user,password,port,my_conf)

    auth = oss2.Auth('LTAIQFvh36NyxuxI', 'M6Au2n69pz7mZFVrICKaQaFKxTv2do')
    # service = oss2.Service(auth, 'oss-cn-beijing.aliyuncs.com')
    # print([b.name for b in oss2.BucketIterator(service)])
    ticks = time.strftime("%Y%d%m_%H%M")
    bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'tplinuxmysqlbackup')
    oss2.resumable_upload(bucket, ticks+'.tar.gz', "%s.tar.gz"%abc)



upload('127.0.0.1','root','redhat',3306,'/etc/my.cnf')
