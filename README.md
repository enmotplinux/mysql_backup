# mysql_backup
MySQL innobackupex 自动备份并且上传到阿里云上

需要在 index.py 文件中指定 
备份机器的ip地址  用户名 端口 my.cnf 
单机版 后续会开发集群版


阿里云的oss需要替换一下
    auth = oss2.Auth('LTAIQFvh36NyxuxI', 'M6Au2n69pz7mZFVrICKaQaFKxTv2do')
    bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'tplinuxmysqlbackup')
    换成自己的
