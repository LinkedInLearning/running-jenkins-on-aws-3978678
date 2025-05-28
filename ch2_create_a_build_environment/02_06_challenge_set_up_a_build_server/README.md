# 02_06 Challenge Set up a build server

In this challenge, you'll create and configure the AWS resources needed to run a build server.

Once the server is online, you’ll connect it to the Jenkins server.

## Overview

1. Create the following AWS resources:

   1. an IAM role that allows full access to AWS Lambda
   1. a security group that allows SSH traffic from the jenkins-server security group
   1. an SSH key for connecting to the build server
   1. an EC2 instance using an Amazon Linux 2023 AMI for the build server. Apply the provided user data to configure the build server

2. Add the SSH key to Jenkins as a credential
3. Add the build server as a new node on the Jenkins server

This challenge should take 15 to 20 minutes to complete.

<!-- FooterStart -->
---
[← 02_05 Connect Jenkins to the build server](../02_05_connect_jenkins_to_the_build_server/README.md) | [02_07 Solution Set up a build server →](../02_07_solution_set_up_a_build_server/README.md)
<!-- FooterEnd -->
