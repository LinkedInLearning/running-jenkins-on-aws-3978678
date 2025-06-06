# 02_01 Plan the build environment

With the Jenkins server up and running, it's time to plan the full build environment.

Follow best practices by removing all **executors** from the primary Jenkins server, ensuring it only manages builds, not runs them.

Key components of the build environment include:

- A **key pair** and **security group** for SSH-based agent communication
- A dedicated **build server** to execute jobs and return results to Jenkins
- An **IAM role** for the build server to securely run AWS commands without needing static credentials

The focus of the course will be on **deploying to AWS Lambda**, using a Git-triggered CI/CD pipeline.

<!-- FooterStart -->
---
[← 01_09 Solution Set up a Jenkins server](../../ch1_setting_up_jenkins/01_09_solution_set_up_a_jenkins_server/README.md) | [02_02 Create an IAM role for the build server →](../02_02_create_an_iam_role_for_the_build_server/README.md)
<!-- FooterEnd -->
