# 04_05 Deploy to AWS Lambda from GitHub

In this lab, you'll complete the CI/CD pipeline by making a change to your application code in GitHub and verifying that the change is deployed to your Lambda-hosted web application.

This will confirm:

1. Your Jenkins job is correctly configured to build and deploy code automatically using webhooks.
1. The `build-server` has the correct permissions to update AWS Lambda resources.

This lab should take 5 to 10 minutes to complete.

## Overview

1. Make a visible change to the web app
2. Commit the change to GitHub
3. Verify the deployment using the Jenkins job output
4. Confirm the change appears in the running application

## Instructions

### 1. Make a Visible Change to the Web App

1. Open the repository that contains your application code in **GitHub**.
2. In the file list, select `template.html`.
3. Select the **pencil icon** to edit the file.
4. Locate the `<h1>` tag near the top of the page. Change:

   ```html
   <h1>The Python API</h1>
   ```

   to:

   ```html
   <h1>The Python API, Deployed with Jenkins :D</h1>
   ```

5. In the **Commit changes** section:

   - Enter a commit message: `My first deployment to AWS Lambda`
   - Select **Commit changes**

This will trigger the Jenkins job using the webhook you previously configured.

### 2. Monitor the Jenkins Job

1. In a new tab, open the **Jenkins dashboard**.
2. Wait for the job named `python-api` to appear in the **Build Executor Status** or **Build History**.
3. Once the job starts running, select the **dropdown arrow** next to the build number and choose **Console Output**.
4. Verify the job was triggered correctly:

   - Look for the line: `Started by GitHub push by <your-username>`
   - Confirm the commit message: `"My first deployment to AWS Lambda"`

### 3. Confirm the Deployment

1. Open the **web page** for your deployed application (found in the Lambda function URL shown in your CloudFormation outputs).
2. Select **Reload** or refresh the page in your browser.
3. Confirm that the updated `<h1>` heading now reads:

    ```bash
    The Python API, Deployed with Jenkins :D
    ```

An update to the web application confirms that your Jenkins pipeline is successfully deploying updates to AWS Lambda whenever changes are pushed to GitHub.

<!-- FooterStart -->
---
[← 04_04 Create a freestyle job to deploy code from GitHub, part 2](../04_04_create_a_freestyle_job_to_deploy_code_from_github_part_2/README.md) | [04_06 Challenge Deploy to AWS Lambda from GitHub →](../04_06_challenge_deploy_to_aws_lambda_from_github/README.md)
<!-- FooterEnd -->
