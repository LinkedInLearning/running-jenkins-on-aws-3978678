# 01_03 Create an IAM role for the Jenkins server

1. In the AWS Console, navigate to the **IAM dashboard**.
1. Select **Roles** from the sidebar, then choose **Create role**.
1. Select **AWS service** as the trusted entity, and choose **EC2** as the use case.
1. Select **Next** until you reach the name field.
1. Name the role `ec2-ssm`.
1. Add a tag: Key = `Name`, Value = `jenkins`.
1. Select **Create role**.

<!-- FooterStart -->
---
[← 01_02 Create a security group](../01_02_create_a_security_group/README.md) | [01_04 Create the Jenkins EC2 instance →](../01_04_create_the_jenkins_ec2_instance/README.md)
<!-- FooterEnd -->
