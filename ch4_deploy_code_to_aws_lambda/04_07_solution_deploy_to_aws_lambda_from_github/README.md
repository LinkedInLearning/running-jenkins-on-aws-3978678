# 04_07 Solution Deploy to AWS Lambda from GitHub

In this challenge, you’ll verify the integration between your GitHub repository and Jenkins by making a visible code change, committing it to the repo, and confirming that Jenkins automatically deploys the update to your application.

This process demonstrates how Continuous Deployment works in a real-world CI/CD workflow.

## Overview

Make sure the following tabs are open in your browser:

- **TAB 1**: GitHub repository with the application code
- **TAB 2**: Jenkins job page for `python-api`
- **TAB 3**: Live application running the Python API

You’ll complete the following steps:

1. **Update and commit a code change**
2. **Review the Jenkins job triggered by the commit**
3. **Confirm the change in the live application**

Complete all previous challenges before attempting this challenge.

This challenge should take 10 to 15 minutes to complete.

## Instructions

### 1. Update and Commit a Code Change

1. In the GitHub repo, open the file `template.html`.
1. Select the **pencil icon** to edit the file in the browser.
1. Scroll to **line 29**.
1. Locate and change the following line:

    ```html
    <h1>The Python API</h1>
    ```

    to:

    ```html
    <h1>The Python API, Deployed with Jenkins</h1>
    ```

1. Commit the change and add a commit message: `My first deployment to AWS Lambda`.
1. Select **Commit changes**.  This action triggers the webhook and starts the Jenkins deployment job.

### 2. Review Jenkins Job Triggered by the Commit

1. In the Jenkins interface, look for the new build that appears in the queue or is running.
1. Once the build starts, click the **pull-down arrow** next to the build number.
1. Select **Console Output** to watch the deployment in real-time.
1. Confirm the job was triggered correctly:

   - Look for a line that reads:
     `Started by GitHub push by YOU_GITHUB_USER_NAME`
   - Look for the commit message:
     `Commit message: "My first deployment to AWS Lambda"`

1. These messages confirm that the Jenkins job was triggered by the GitHub webhook and deployed the correct version of your code.

### 3. Confirm the Change in the Application

1. Refresh the API web page in your browser.
1. Look for the updated header: **The Python API, Deployed with Jenkins**.
1. Seeing this change on the live application confirms that the deployment succeeded end-to-end.

<!-- FooterStart -->
---
[← 04_06 Challenge Deploy to AWS Lambda from GitHub](../04_06_challenge_deploy_to_aws_lambda_from_github/README.md) | [05_01 Stop or remove AWS resources →](../../ch5_shut_down_aws_resources/05_01_stop_or_remove_aws_resources/README.md)
<!-- FooterEnd -->
