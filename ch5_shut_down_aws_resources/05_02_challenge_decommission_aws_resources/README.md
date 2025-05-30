# 05_02 Challenge: Decommission AWS Resources

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

<!-- FooterStart -->
---
[← 05_01 Decommission AWS resources](../05_01_decommission_aws_resources/README.md) | [05_03 Solution: Decommission AWS Resources →](../05_03_solution_decommission_aws_resources/README.md)
<!-- FooterEnd -->
