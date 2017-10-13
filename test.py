import os,time,sys,time
import oss2
from itertools import islice

def download():
    auth = oss2.Auth('LTAIQFvh36NyxuxI', 'M6Au2n69pz7mZFVrICKaQaFKxTv2do')
    bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'tplinuxmysqlbackup')
    ticks = time.strftime("%Y%d%m_%H%M")
    file=ticks+'.tar.gz'
    #bucket.get_object_to_file("20171010_2340.tar.gz",file)
    list=[]
    for b in islice(oss2.ObjectIterator(bucket), 100):
        list.append(b.key)
    print(list[-1])

    bucket.get_object_to_file(list[-1],list[-1])
download()
