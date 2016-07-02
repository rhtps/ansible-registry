docker-registry
=========

This role will set up a disconnected Docker registry

The Task will first install Docker. Next, it will install docker-registry and import any of the tarballs specified in the.


Requirements
------------

Tarballs available for Docker images.


<strong>NOTE:</strong> This will make sweeping changes to your host.  It is recommended you apply this role to a freshly provisioned host.

Role Variables
--------------
```yaml
---
# this is the path that your external images were imported from. Information needed
# to glean the full image names from the tarball.
registry_path : "registry.access.redhat.com"

# Local path on the host that the tarballs should be expected
ose_images_tar_path : "/ansible/"

# Device that Docker will use to create its storage
registry_dev : "/dev/xvdh"

# List of tarballs to import
ose_images_tar:
  ose3-builder-images.tar : ""
  ose3-images.tar : ""
  ose3-logging-metrics-images.tar : ""

# List of images from within tarballs to import and tag in registry
ose_images:
  openshift3/ose-haproxy-router : "v3.2.0.20-3"
  openshift3/ose-deployer : "v3.2.0.20-3"
  openshift3/ose-sti-builder : "v3.2.0.20-3"
  openshift3/ose-docker-builder : "v3.2.0.20-3"
  openshift3/ose-pod : "v3.2.0.20-3"
  openshift3/ose-docker-registry : "v3.2.0.20-3"
  openshift3/logging-deployment : "latest"
  openshift3/logging-elasticsearch : "latest"
  openshift3/logging-kibana : "latest"
  openshift3/logging-fluentd : "latest"
  openshift3/logging-auth-proxy : "latest"
  openshift3/metrics-deployer : "latest"
  openshift3/metrics-hawkular-metrics : "latest"
  openshift3/metrics-cassandra : "latest"
  openshift3/metrics-heapster : "latest"
  jboss-amq-6/amq62-openshift : "latest"
  jboss-eap-6/eap64-openshift : "latest"
  jboss-webserver-3/webserver30-tomcat7-openshift : "latest"
  jboss-webserver-3/webserver30-tomcat8-openshift : "latest"
  rhscl/mongodb-26-rhel7 : "latest"
  rhscl/mysql-56-rhel7 : "latest"
  rhscl/perl-520-rhel7 : "latest"
  rhscl/php-56-rhel7 : "latest"
  rhscl/postgresql-94-rhel7 : "latest"
  rhscl/python-27-rhel7 : "latest"
  rhscl/python-34-rhel7 : "latest"
  rhscl/ruby-22-rhel7 : "latest"
  openshift3/nodejs-010-rhel7 : "latest"
```
Dependencies
------------

None

Example Playbook
----------------

```yaml
# file: docker-registry.yaml
- hosts: registry
  roles:
  - ansible-role-docker-registry
  vars:
    ose_images_tar_path : "~/docker-tarballs/"
    registry_dev : "/dev/xvdh"
```
Example Inventory
-----------------
```ini
[registry]
10.0.0.2
```
Example Run
-----------
```bash
ansible-playbook -u ec2-user -b -i registry_inventory docker-registry.yaml
```

License
-------

Apache 2.0

Author Information
------------------

Matt Bagnara is a Red Hat consultant