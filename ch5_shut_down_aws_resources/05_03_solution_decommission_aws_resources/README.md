# 05_03 Solution: Decommission AWS Resources

In this challenge, you'll clean up the AWS resources that were created during earlier lessons.

Removing unused resources is good practice; it keeps your AWS account organized, extends your use of the free tier, and helps you avoid unexpected charges.

Resources should be deleted in the reverse order they were created, starting with application-specific infrastructure and ending with foundational security components.

## Overview

1. Delete the CloudFormation stack used to deploy Lambda functions.
1. Terminate the EC2 instances used as the Jenkins server and build server.
1. Remove resources associated with the Jenkins server and build server:

    - Elastic IP address
    - Security groups
    - SSH key pair
    - IAM roles

This challenge should take 10 to 15 minutes to complete.

## Solution

### 1. Delete the CloudFormation Stack

1. In the **AWS Management Console**, go to **CloudFormation**
1. Select the stack used to deploy the Lambda functions (e.g., `python-api`)
1. Select **Delete**
1. Confirm the deletion when prompted
1. Wait for the status to change to **DELETE\_COMPLETE**

### 2. Terminate the EC2 Instances

1. In the **EC2 Console**, go to **Instances**
1. Locate the instances named `jenkins-server` and `build-server`
1. Select both instances using the checkboxes
1. Choose **Instance state → Terminate (delete) instance**
1. Confirm the termination
1. Wait until both instances are no longer listed as running

### 3. Remove Associated Resources

#### a. Delete the Elastic IP Address

1. In the **EC2 Console**, go to **Elastic IPs** under **Network & Security**
1. Locate the Elastic IP address associated with the Jenkins server
1. Select the checkbox next to the address and choose **Actions → Disassociate Elastic IP address**
1. Confirm the disassociation
1. With the IP still selected, choose **Actions → Release Elastic IP address**
1. Confirm the release

#### b. Delete the Security Groups

> [!IMPORTANT]
> The `build-server` security group references the `jenkins-server` group to allow SSH access. To avoid dependency errors, delete the `build-server` group first.

1. In the **EC2 Console**, go to **Security Groups**
1. Delete the `build-server` security group:

    - Select the `build-server` group
    - Choose **Actions → Delete security group**
    - Confirm the deletion

1. Next, delete the `jenkins-server` security group:

    - Select the `jenkins-server` group
    - Choose **Actions → Delete security group**
    - Confirm the deletion

#### c. Delete the SSH Key Pair

1. In the **EC2 Console**, go to **Key Pairs**
1. Locate the key pair named `build-server`
1. Select it and choose **Actions → Delete**
1. Confirm the deletion

#### d. Delete the IAM Roles

1. Go to the **IAM Console**, select **Roles**
1. Locate the roles used by the EC2 instances (e.g., `ec2-lambda`, `ec2-jenkins`)
1. Select each role, then choose **Delete role**
1. To confirm deletion, enter `delete` in the text input field
1. Select **Delete**

<!-- FooterStart -->
---
[← 05_02 Challenge: Decommission AWS Resources](../05_02_challenge_decommission_aws_resources/README.md) | [06_01 Next Steps →](../../ch6_conclusion/06_01_next_steps/README.md)
<!-- FooterEnd -->
