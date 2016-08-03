swarm-ansible
============

This is currently a work in progress - the Ansible should mostly work completely, but the corresponding terraform scripts have not been released yet.

There are a few moving parts to this system:
* The "admin" node will run an instance of cfssl, which is used to create and hand out x.509 certificates to the swarm clients
* The manager node as well as the swarm nodes will run a consul server and client, which is used to coordiante the Docker cluster. There is an encryption key specified in the variables directory, but I highly recommend changing it!
* When the plays are done, there should be a working swarm cluster using the consul k/v store, with the ability to use overlay networks and other fun features

## swarm.yml
This contains the roles for the different types of nodes, of which there are three:

### swarm_admin
This is the node that runs `cfssl` in order to create and hand out SSL certificates. This node is the only node that is designed to communicate over the public internet. 

### swarm_nodes
These are follower nodes who are only running the swarm client when this is done

### swarm_manager
This is the swarm leader, which is running the swarm client as well as the master server

