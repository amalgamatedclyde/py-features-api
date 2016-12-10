##Rolling Deployments

strategy: 2 instances are always up. when a push occurs, a new third instance pops up. after it passes the health checks it goes online and one of the other instances is stopped for the update.
at that point one instance is running the update and the other is running the previous build. when the second instance passes the health check it goes online and the remaining instance is terminated.
