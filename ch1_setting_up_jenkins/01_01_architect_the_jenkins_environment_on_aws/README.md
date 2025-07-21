# 01_01 Architect the Jenkins Environment on AWS

The Jenkins environment will be hosted on an **EC2 instance** running **Ubuntu Linux**.

Key AWS components include:

- An **IAM role** for secure terminal access
- A **security group** allowing incoming HTTP traffic
- An **Elastic IP address** for consistent web access

The following Software installed on the server running Jenkins:

- **JDK 21** (Java Development Kit)
- **NGINX** (as a reverse proxy)
- **Jenkins LTS** (Long-Term Support version)
- These components form the foundation for the Jenkins CI/CD pipeline we’ll build.

<!-- FooterStart -->
---
[← 00_02 What you should know](../../ch0_introduction/00_02_what_you_should_know/README.md) | [01_02 Create an IAM role for the Jenkins server →](../01_02_create_an_iam_role_for_the_jenkins_server/README.md)
<!-- FooterEnd -->
