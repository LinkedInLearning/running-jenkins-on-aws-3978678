# 03_06 Challenge Connect Jenkins to GitHub

In this challenge you'll use a webhook to connect Jenkins to a GitHub repository.

The goal is to use push commits in GitHub to trigger a Jenkins job.

Developing a proficiency with this technique is key to developing the CI/CD pipeline in upcoming sections of the course.

## **Overview**

1. Create a public GitHub repository and copy its HTTPS URL
2. Create and configure a Jenkins freestyle project that:

   - Uses the GitHub repository for source code
   - Triggers builds using a GitHub webhook
   - Prints the contents of the `README.md` file

3. Configure a webhook in GitHub that notifies Jenkins when a push event occurs
4. Make a small change to the GitHub repository to trigger the Jenkins job and review the console output

This challenge should take 15 to 20 minutes to complete.

<!-- FooterStart -->
---
[← 03_03 Create and test a webhook with GitHub](../03_03_create_a_webhook_with_github/README.md) | [03_07 Solution Connect Jenkins to GitHub →](../03_05_solution_connect_jenkins_to_github/README.md)
<!-- FooterEnd -->
