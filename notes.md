##Architecture

###Instance configuration

**EC2** instance boots from a custom image running **ubuntu 16.04** and starts 4 **NGINX** workers. **Supervisor** then starts from .bashrc creating 4 **Tornado** servers using 4 processes each listening on a separate port, from :8000 to :8003

**NGINX** reverse proxies to port 80 for http traffic, load balancing across the 4 tornado ports.

###Log file locations

**NGINX** logs at /var/log/nginx and include access.log which logs requests like this:
172.31.11.81 - - [10/Dec/2016:17:46:14 +0000] "GET / HTTP/1.1" 200 8 "-" "ELB-HealthChecker/1.0"

and error.log which logs errors like this:

2016/12/10 17:36:15 [error] 1083#1083: *2 no live upstreams while connecting to upstream, client: 172.31.42.232, server: , request: "GET / HTTP/1.1", upstream: "http://frontends/", host: "172.31.45.82"

**System** log at /var/log/syslog

**SUPERVISOR** maintains logs for itself and the processes it controls and these are located at ~/log
Logs are as follows:
supervisord.log  tornado-stderr.log  tornado-stdout.log

**Supervisord** is the Supervisor daemon. Its config file is located at /opt/anaconda2/etc/supervisord.conf

**Python App** runs from /home/ubuntu/py-features-api and the web server is web.py


##Fleet Configuration
Right now we'll run 2x m4.xlarge instances behind an AWS classic load balancer. That'll give us 8 CPUs or 32 Tornado processes.


##Rolling Deployments

**Strategy:** 2 instances are always up. when a push occurs, a new third instance pops up. after it passes the health checks it goes online and one of the other instances is stopped for the update.
at that point one instance is running the update and the other is running the previous build. when the second instance passes the health check it goes online and the remaining instance is terminated.
