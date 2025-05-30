# 01_08 Challenge Set up a Jenkins server

In this challenge, you’ll create and configure the AWS resources needed to host a Jenkins server.

The challenge walks through the full setup process: from provisioning infrastructure in AWS to installing and configuring Jenkins with NGINX as a reverse proxy.

## **Overview**

You will complete  the following steps in this challenge:

1. **Create an IAM role** that allows EC2 instances to be accessed via Systems Manager (SSM).
1. **Create a security group** that enables HTTP and HTTPS access to your server.
1. **Create the Jenkins EC2 instance** using an Ubuntu AMI, associate the IAM role and security group, and assign an Elastic IP.
1. **Install Java, Jenkins, and NGINX** using the AWS Systems Manager session.
1. **Configure NGINX** to serve as a reverse proxy for Jenkins.
1. **Configure Jenkins** by unlocking it, installing default plugins, and setting up an admin account.

This challenge should take 20 to 25 minutes to complete.

<!-- FooterStart -->
---
[← 01_07 Configure Jenkins](../01_07_configure_jenkins/README.md) | [01_09 Solution Set up a Jenkins server →](../01_09_solution_set_up_a_jenkins_server/README.md)
<!-- FooterEnd -->
