#!/usr/bin/env python3

from crontab import CronTab

cron = CronTab(user='root')
cron.remove_all()
current_job = cron.new(command='sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" /opt/service_state', comment='update file by cron')
current_job.minute.every(1)
cron.write()
print('_ _ _ _ _ _ _ _ _Start_ _ _ _ _ _ _ _ _ _ _')
