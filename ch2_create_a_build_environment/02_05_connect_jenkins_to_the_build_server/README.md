# 02_05 Connect Jenkins to the build server

Using the private IP address for the build server connection has benefits:

- Reduces network costs by minimizing ingress and egress from the AWS network.
- Keeps the connection between the Jenkins server and the build server fast, again, because the public internet is not traversed.
- The private IP address of an Amazon EC2 instance will remain the same after a shutdown and restart.  This saves us from having to reconfigure the connection between the build server and Jenkins if the build server is taken offline.

<!-- FooterStart -->
---
[← 02_04 Create the build server](../02_04_create_the_build_server/README.md) | [02_06 Challenge Set up a build server →](../02_06_challenge_set_up_a_build_server/README.md)
<!-- FooterEnd -->
