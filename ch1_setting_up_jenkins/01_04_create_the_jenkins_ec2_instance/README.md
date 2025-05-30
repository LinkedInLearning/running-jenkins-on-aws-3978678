# 01_04 Create the Jenkins EC2 instance

1. On the EC2 Dashboard, select **Launch Instance**.
1. Set the instance name to `jenkins-server`.
1. Choose the AMI: **Ubuntu Server 24.04 LTS**.
1. Choose instance type: **t2.micro** (eligible for free tier).
1. Under **Key pair**, choose **Proceed without a key pair**.
1. Under **Network settings**:

    - Enable **Auto-assign Public IP**.
    - Select the existing security group: `jenkins-server`.

1. Under **Storage**, set the root volume size to **20 GB**.
1. Under **Advanced Details**, select the IAM role: `ec2-ssm`.
1. Select **Launch Instance**.
1. After launching, allocate a new **Elastic IP**.
1. Associate the Elastic IP with the EC2 instance.

<!-- FooterStart -->
---
[← 01_03 Create an IAM role for the Jenkins server](../01_03_create_an_iam_role_for_the_jenkins_server/README.md) | [01_05 Install Java, Jenkins, NGINX →](../01_05_install_java_jenkins_nginx/README.md)
<!-- FooterEnd -->
