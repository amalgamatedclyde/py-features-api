##Architecture

The high availability rolling-deployment configuration for the **Markable py-features-api** development site is launched from an **AWS stack**. 
The stack configuration is specified in a YAML file which can be sourced locally or from an S3 bucket. This file is tracked by git.

Currently the stack uses an auto-scaling group to launch 2 EC-2 instances behind a classic load balancer. 

###Instance configuration

Each **EC2** instance boots from a custom image running **ubuntu 16.04**, currently:

ami-ba2428ad

At boot time **NGINX** starts 4 workers (1 per core) using separate processes. The process controller, **Supervisor** ,
then starts as a daemon and launches 4 **Tornado** servers using 4 processes (1 per core), each listening on a separate port, from :8000 to :8003

**NGINX** reverse proxies these to port 80 for http traffic, load balancing across the 4 tornado ports. 
An EC-2 load balancer balances across the instances. This provides redundancy and restart on failure at every level.

###Log file locations as of 12/12

**NGINX** logs at /var/log/nginx 

These include access.log which logs requests like this:
172.31.11.81 - - [10/Dec/2016:17:46:14 +0000] "GET / HTTP/1.1" 200 8 "-" "ELB-HealthChecker/1.0"

and error.log which logs errors like this:

2016/12/10 17:36:15 [error] 1083#1083: *2 no live upstreams while connecting to upstream, client: 172.31.42.232, server: , request: "GET / HTTP/1.1", upstream: "http://frontends/", host: "172.31.45.82"

**SUPERVISOR** maintains logs for itself and the processes it controls and these are located at /var/log/supervisor
Logs are as follows:
supervisord.log  tornado-stderr.log  tornado-stdout.log

**Supervisord** is the Supervisor daemon. Its config file is located at /opt/anaconda2/etc/supervisord.conf

Currently planning on implementing a centralized logging system using CloudWatch.

##Fleet Configuration
Right now we're running 2x m4.xlarge instances behind an AWS classic load balancer. That gives us 8 CPUs or 32 Tornado processes.

##Rolling Deployments

**Strategy:** At least 2 instances must be healthy and available at all times. Deployments trigger a third instance.

##Deployment tool chain
TBD. Still working on this

