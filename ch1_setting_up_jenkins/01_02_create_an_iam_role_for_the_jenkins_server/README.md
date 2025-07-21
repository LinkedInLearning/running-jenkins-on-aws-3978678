# 01_02 Create an IAM role for the Jenkins server

1. In the AWS Console, navigate to the **IAM dashboard**.
1. Select **Roles** from the sidebar, then choose **Create role**.
1. Select **AWS service** as the trusted entity, and choose **EC2** as the use case.
1. Select **Next** until you reach the name field.
1. Name the role `ec2-ssm`.
1. Add a tag: Key = `Name`, Value = `jenkins`.
1. Select **Create role**.

<!-- FooterStart -->
---
[← 01_01 Architect the Jenkins Environment on AWS](../01_01_architect_the_jenkins_environment_on_aws/README.md) | [01_03 Create a security group →](../01_03_create_a_security_group/README.md)
<!-- FooterEnd -->
