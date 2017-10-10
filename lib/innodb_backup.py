#!/usr/local/bin/python3.5
import os,time
def backup(host,user,password,port,my_conf):
    back_dir="/backup/mysql_%s/full"%port
    log_dir="/backup/mysql_%s/log"%port
    ticks = time.strftime("%Y%d%m_%H%M")
    time_log='full_%s.log'%(ticks)
    os.system("mkdir -p %s"%back_dir)
    os.system("mkdir -p %s"%log_dir)

    MySQL_CMD = "--defaults-file=%s --user=%s --password=%s --host %s --port %s %s " \
                % (my_conf, user, password, host, port,back_dir)
    inno_backup='innobackupex %s'%MySQL_CMD

    os.system( 'innobackupex %s > %s/%s 2>&1' %(MySQL_CMD,log_dir,time_log) )
    find_find="find {0} -mindepth 1 -maxdepth 1 " \
              "-type d -printf '%P\n' | sort -nr | head -1".format(back_dir)
    find_f=os.popen(find_find).read().strip()
    apply_time_log='apply_%s.log'%(ticks)
    os.system("innobackupex --apply-log %s/%s > %s/%s 2>&1 "%(back_dir,find_f,log_dir,apply_time_log))
    file="%s/%s"%(back_dir,find_f)
    #os.system("tar -zcvf %s.tar.gz %s"%(file,file))
    os.system('tar -zcf %s.tar.gz %s '%(file,file))

    return file


