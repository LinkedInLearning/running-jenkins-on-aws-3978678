# 03_01 Plan the CI/CD pipeline

**Continuous Integration (CI)** encourages developers to commit code frequently to a shared repository, allowing for early error detection and smoother integration of changes.

**Continuous Delivery (CD)** automates the build and deployment process, enabling rapid and repeatable releases to different environments.

In our pipeline:

- Developers write and commit code to **GitHub**.
- **Webhooks** trigger Jenkins to start a job on the **build server**.
- The build server pulls the updated code and deploys it to **AWS Lambda**.
- Jenkins can send **notifications** to developers about deployment results and application status.

This process supports fast iteration and reliable delivery of new features, updates, and fixes—even after the app is in production.

<!-- FooterStart -->
---
[← 02_07 Solution Set up a build server](../../ch2_create_a_build_environment/02_07_solution_set_up_a_build_server/README.md) | [03_02 What's a webhook? →](../03_02_whats_a_webhook/README.md)
<!-- FooterEnd -->
