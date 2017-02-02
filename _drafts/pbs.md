---
layout: post
title: Installing a PBS server on Ubuntu for deep learning
date: 2017-01-25
categories: ml
image:
  feature: constellations3.jpg
---

`sudo apt-get install torque-server torque-client torque-mom torque-pam`

`sudo /etc/init.d/torque-mom stop`
`sudo /etc/init.d/torque-scheduler stop`
`sudo /etc/init.d/torque-server stop`

Find the IP address of your machine on your local network using ifconfig..
In my case it was 192.168.156.196, but something like 192.168.1.1 is more
common.

`sudo echo $IP > /etc/torque/server_name`
`sudo echo $IP > /var/spool/torque/server_prev/acl_svr/acl_hosts`
`sudo echo root@localhost > /var/spool/torque/server_priv/acl_svr/operators`
`sudo echo root@localhost > /var/spool/torque/server_priv/acl_svr/managers`

Add to /etc/hosts:

$IP $SERVERNAME

`sudo echo "$SERVERNAME np=1" > /var/spool/torque/server_priv/nodes`
`sudo echo "pbs_server = $IP" > /var/spool/torque/mom_priv/config`

Restart everything
`sudo /etc/init.d/torque-server start`
`sudo /etc/init.d/torque-scheduler start`
`sudo /etc/init.d/torque-mom start`

`sudo qmgr -c 'set server scheduling = true'`
`sudo qmgr -c 'set server mom_job_sync = true'`

If the machine that is submitting these commands is different than the one
the server has been configured to expect, then you will get an "Unauthorized
request" error.  This can be fixed by monkeying around with the server
names, ip addresses, and user names in the configuration files above.  The
configuration I listed above worked on my machine, but the configuration on
Johann Briffa's webpage didn't work for me.  So my configuration might not
work for you.  If something needs to be different, this is where you'll see
it.

Set up a queue named "batch" (but can be anything you want):

`sudo qmgr -c 'create queue batch'`
`sudo qmgr -c 'set queue batch queue_type = execution'`
`sudo qmgr -c 'set queue batch started = true'`
`sudo qmgr -c 'set queue batch enabled = true'`

Set a few defaults.  I like a long default walltime limit.
`sudo qmgr -c 'set queue batch resources_default.walltime = 168:00:00'`
`sudo qmgr -c 'set queue batch resources_default.nodes = 1'`
`sudo qmgr -c 'set server default_queue = batch'`

This line will keep recently completed jobs visible in the queue for five
minutes.
`sudo qmgr -c 'set server keep_completed = 300'`

`sudo qmgr -c 'set server submit_hosts = '`
`sudo qmgr -c ''`

You can check the different settings of the PBS server by running

`qmgr -c 'print server'

(or `qmgr -c 'p s'` for short)

To test everything is as it should be,

`pbsnodes -a`

should show your one node with `state = free`.  If it doesn't, it could be
that the PBS server cannot find the mom server.  You can also try submitting
a job by running `qsub $SOMEJOB.SH`.  If the job hangs in the queue
indefinitely, that indicates that the PBS server probably cannot connect to
the mom server.  Check mom_logs in '/var/spool/torque/mom_logs' for hints
about what's going wrong.

## Job priority

It is very useful to be able to assign different priorities to your jobs.
The priority can be set with the `-p` flag in `qsub`.  1023 is the maximum
priority, and -1024 is the minimum.  However, on my machine, the default
configuration ignores any user-set priorities.  To fix this, edit 

```/var/spool/torque/sched_priv/sched_config```

There is a line that says PRIME OPTION, underneath which by default it says

```sort_by: shortest_job_first  ALL```

Comment out this line and add a line that says

```sort_by: high_priority_first ALL```

## Starving jobs
