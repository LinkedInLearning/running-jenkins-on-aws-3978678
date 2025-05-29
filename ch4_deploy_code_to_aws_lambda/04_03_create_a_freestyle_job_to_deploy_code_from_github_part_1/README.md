# 04_03 Create a freestyle job to deploy code from GitHub, part 1

In this lab, you’ll begin creating a Jenkins job that is connected to your GitHub repository via a webhook.

By the end of this lab, you’ll be on the way to having a Jenkins job that pulls your latest code and begins the deployment process each time you update your GitHub repository.

## Overview

1. Get the repo URL
1. Create a freestyle job in Jenkins
1. Create a webhook in the repo settings

## Instructions

### 1. Get the Repo URL

1. Open your GitHub repository for the project.
2. Select the **Code** button and select the **HTTPS** tab.
3. Select the **Copy** icon to copy the repo URL to your clipboard.

### 2. Create a Freestyle Job in Jenkins

1. Open Jenkins and select **New Item**.
1. Enter the item name as `python-api`.
1. Select **Freestyle project** and select **OK**.
1. Enter the description: `Deploy the application code to AWS Lambda`.
1. Under **General**, check **Restrict where this project can be run**.
1. Enter `lambda` in the field provided.
1. In the left menu, select **Source Code Management**.
1. Select **Git**.
1. Paste the GitHub repo URL you copied earlier into the **Repository URL** field.
1. Under **Branches to build**, set the **Branch Specifier** to `*/main`.
1. Select **Build Triggers** in the left menu.
1. Check the option: **GitHub hook trigger for GITScm polling**.
1. Select **Apply** to save the job settings.

### 3. Create a Webhook in the Repo Settings

1. In Jenkins, right-click the **Jenkins** icon and select **Copy Link Address** to get your Jenkins server URL.
2. Go back to your GitHub repository.
3. Select **Settings** > **Webhooks** > **Add webhook**.
4. In the **Payload URL** field, paste the Jenkins server URL and append `github-webhook/` to the end (e.g., `http://jenkins.example.com/github-webhook/`).
5. Set the **Content type** to `application/json`.
6. Select **Add webhook**.
7. Refresh the Webhooks page to verify GitHub shows a success message for the newly added webhook.

Continue to the next lab to finalize your deployment job configuration.

<!-- FooterStart -->
---
[← 04_02 Create a GitHub repository for the application code](../04_02_create_a_github_repository_for_the_application_code/README.md) | [04_04 Create a freestyle job to deploy code from GitHub, part 2 →](../04_04_create_a_freestyle_job_to_deploy_code_from_github_part_2/README.md)
<!-- FooterEnd -->
