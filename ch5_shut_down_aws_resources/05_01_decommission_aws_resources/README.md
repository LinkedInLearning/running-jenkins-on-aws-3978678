# 05_01 Decommission AWS resources

Before finishing the course, it's important to **decommission AWS resources** that are no longer needed.

This helps your AWS account:

- Remain organized and tidy
- Stay within the **free tier**
- Avoid unexpected charges

To prevent dependency errors, decommission resources in the following order:

  1. **Delete the CloudFormation stack** used to deploy the Lambda function
  1. **Terminate the Jenkins server and build server**.
  1. Then delete the following in order:

        1. Build server Security group
        1. Jenkins server Security group
        1. Elastic IP address
        1. SSH key pair
        1. IAM roles

<!-- FooterStart -->
---
[← 04_07 Solution Deploy to AWS Lambda from GitHub](../../ch4_deploy_code_to_aws_lambda/04_07_solution_deploy_to_aws_lambda_from_github/README.md) | [05_02 Challenge: Decommission AWS Resources →](../05_02_challenge_decommission_aws_resources/README.md)
<!-- FooterEnd -->
