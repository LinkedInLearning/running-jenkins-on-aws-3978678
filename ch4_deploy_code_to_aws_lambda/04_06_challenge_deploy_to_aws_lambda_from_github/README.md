# 04_06 Challenge Deploy to AWS Lambda from GitHub

In this challenge, you’ll verify the integration between your GitHub repository and Jenkins by making a visible code change, committing it to the repo, and confirming that Jenkins automatically deploys the update to your application.

This process demonstrates how Continuous Deployment works in a real-world CI/CD workflow.

If you haven’t already done so, review and complete the steps from the following exercise files:

1. [Initialize the deployment target in AWS Lambda](https://github.com/LinkedInLearning/running-jenkins-on-aws-3978678/blob/main/ch4_deploy_code_to_aws_lambda/04_01_initialize_the_deployment_target_in_AWS_Lambda/README.md)
2. [Create a GitHub repository for the application code](https://github.com/LinkedInLearning/running-jenkins-on-aws-3978678/blob/main/ch4_deploy_code_to_aws_lambda/04_02_create_a_github_repository_for_the_application_code/README.md)
3. [Create a freestyle job to deploy code from GitHub, part 1](https://github.com/LinkedInLearning/running-jenkins-on-aws-3978678/blob/main/ch4_deploy_code_to_aws_lambda/04_03_create_a_freestyle_job_to_deploy_code_from_github_part_1/README.md)
4. [Create a freestyle job to deploy code from GitHub, part 2](https://github.com/LinkedInLearning/running-jenkins-on-aws-3978678/blob/main/ch4_deploy_code_to_aws_lambda/04_04_create_a_freestyle_job_to_deploy_code_from_github_part_2/README.md)

## Overview

Make sure the following tabs are open in your browser:

- **TAB 1**: GitHub repository with the application code
- **TAB 2**: Jenkins job page for `python-api`
- **TAB 3**: Live application running the Python API

You’ll complete the following steps:

1. **Update and commit a code change**
2. **Review the Jenkins job triggered by the commit**
3. **Confirm the change in the live application**

This challenge should take 10 to 15 minutes to complete.

<!-- FooterStart -->
---
[← 04_05 Deploy to AWS Lambda from GitHub](../04_05_deploy_to_aws_lambda_from_github/README.md) | [04_07 Solution Deploy to AWS Lambda from GitHub →](../04_07_solution_deploy_to_aws_lambda_from_github/README.md)
<!-- FooterEnd -->
