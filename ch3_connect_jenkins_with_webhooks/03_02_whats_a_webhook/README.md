# 03_02 What's a webhook?

A **webhook** is a way for web applications to notify each other when an event occurs, typically using an HTTP POST request.

Think of a webhook like a **delivery notification**—an event occurs (e.g., code is pushed), and a message is sent to inform another service that it's time to act.

In our CI/CD pipeline:

- **GitHub** acts as the sender, notifying **Jenkins** whenever code is pushed to the repository.
- Jenkins receives this webhook notification at a designated **endpoint** and uses the included data (e.g., committer name, changed files, branch info) to trigger the next automation steps.

This allows Jenkins to immediately begin building and deploying code whenever changes are committed—no manual action required.

<!-- FooterStart -->
---
[← 03_01 Plan the CI/CD pipeline](../03_01_plan_the_cicd_pipeline/README.md) | [03_03 Create and test a webhook with GitHub →](../03_03_create_a_webhook_with_github/README.md)
<!-- FooterEnd -->
