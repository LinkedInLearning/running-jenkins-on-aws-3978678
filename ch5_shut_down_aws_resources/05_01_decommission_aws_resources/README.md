# 05_01 Decommission AWS resources

As we wind down this course, we need to take a few minutes to decommission AWS resources.

Removing the resources that you no longer need keeps your account tidy, helps you stay within the free tier, and prevents unexpected charges from AWS.  No one wants that!

Start by deleting the Lambda function CloudFormation stack.

Then, remove the build server, its security group, SSH key, and IAM role.

Finally, remove the Jenkins server along with its elastic IP address, security group, and IAM role.

<!-- FooterStart -->
---
[← 04_07 Solution Deploy to AWS Lambda from GitHub](../../ch4_deploy_code_to_aws_lambda/04_07_solution_deploy_to_aws_lambda_from_github/README.md) | [05_02 Challenge: Decommission AWS Resources →](../05_02_challenge_decommission_aws_resources/README.md)
<!-- FooterEnd -->
