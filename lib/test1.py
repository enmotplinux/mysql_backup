# -*- coding: utf-8 -*-

import oss2

auth = oss2.Auth('LTAIQFvh36NyxuxI', 'M6Au2n69pz7mZFVrICKaQaFKxTv2do')
#service = oss2.Service(auth, 'oss-cn-beijing.aliyuncs.com')
#print([b.name for b in oss2.BucketIterator(service)])
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'tplinuxmysqlbackup')


oss2.resumable_upload(bucket, 'a2', )
