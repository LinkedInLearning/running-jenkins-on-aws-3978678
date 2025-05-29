# 04_01 Initialize the deployment target in AWS Lambda

In this lab, you'll initialize a deployment target in AWS by launching a Lambda function using a CloudFormation template. This template defines all the resources required to host a Python-based API.

Once deployed, you'll explore the CloudFormation stack details and identify key information needed to configure your deployment pipeline.

This lab should take 5 to 10 minutes to complete.

## Overview

1. Download the exercise files
1. Deploy the CloudFormation stack

## Instructions

### 1. Download the Exercise Files

> [!NOTE]
> If you've already downloaded the exercise files, you can skip this step!

1. Visit the course GitHub repository.
1. From the home page of the repository, select **Code > Download ZIP**.
1. Extract the ZIP file on your local system to view its contents.
1. Navigate to the lesson folder:
   `ch4_deploy_code_to_aws_lambda/04_01_initialize_the_deployment_target_in_AWS_Lambda`

### 2. Deploy the CloudFormation Template

> [!IMPORTANT]
> Make sure you deploy the CloudFormation stack in the same region where your Jenkins server and Build server are deployed.

1. Log in to your AWS account and navigate to the **CloudFormation** service.
1. Select **Create Stack**.
1. On the *Create stack* screen, select **Upload a template file**.
1. Click **Choose file** and upload `lambda_function_cloudformation.yml` located in the `04_01_initialize_the_deployment_target_in_AWS_Lambda` folder.
1. Select **Next**.
1. For the *Stack name*, enter: `python-api`
1. Since this template has no parameters, select **Next** again.
1. On the *Configure stack options* screen, scroll to the bottom.
1. Check the box acknowledging that AWS CloudFormation might create IAM resources with custom names.
1. Select **Next**.
1. On the *Review* screen, scroll to the bottom and select **Submit**.
1. Wait for the stack to finish deploying. Click the **refresh icon** periodically until the status changes to **CREATE_COMPLETE**.
1. Once deployment is complete, select the **Resources** tab to view the Lambda function, its permissions, and the function's URL.
1. Select the **Outputs** tab to view operational details such as:

    - AWS region
    - Lambda function name
    - Function URL

1. Record the values shown in the Outputs tab. You’ll use these values to configure the Jenkins deployment job in the next lessons.

<!-- FooterStart -->
---
[← 03_08 Create and test a webhook with Bitbucket](../../ch3_connect_jenkins_with_webhooks/03_08_create_a_webhook_with_bitbucket/README.md) | [04_02 Create a GitHub repository for the application code →](../04_02_create_a_github_repository_for_the_application_code/README.md)
<!-- FooterEnd -->
