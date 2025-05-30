# 01_02 Create a security group

1. Navigate to the **EC2 Dashboard** and select **Security Groups** under Network & Security.
1. Select **Create Security Group**.
1. Name the group `jenkins-server` and add a description like `Allow web traffic`.
1. Keep the default VPC setting.
1. Add the following **inbound rules**:

    - HTTP (port 80) from **Anywhere (IPv4)**
    - HTTPS (port 443) from **Anywhere (IPv4)**

1. Leave the **outbound rules** as-is (allowing all traffic).
1. Add a tag: Key = `Name`, Value = `jenkins-server`.
1. Select **Create security group**.

<!-- FooterStart -->
---
[← 01_01 Architect the Jenkins Environment on AWS](../01_01_architect_the_jenkins_environment_on_aws/README.md) | [01_03 Create an IAM role for the Jenkins server →](../01_03_create_an_iam_role_for_the_jenkins_server/README.md)
<!-- FooterEnd -->
