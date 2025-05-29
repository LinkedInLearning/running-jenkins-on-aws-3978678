# 03_08 Create and test a webhook with Bitbucket

Follow the steps in this document to create a webhook that connects a Jenkins job to a Bitbucket repository.

The goal is to have push commits to the Bitbucket repository trigger the Jenkins job to check out the code and run build steps.

## Overview

1. Create a Bitbucket repo and an access token that allows read access to a repository
1. Install the Bitbucket Push and Pull Request plugin to provide webhook functionality
1. Configure a Jenkins freestyle project that:
   1. Uses the Bitbucket repository for SCM
   1. Listens for push notifications from GitLab
1. Create a wehbook in Bitbucket that will notify Jenkins when a push event occurs on the repository

This challenge should take 15 to 20 minutes to complete.

## Instructions

### 1. Create Bitbucket Repository and Access Token

1. Log in to your Bitbucket account.
1. Create a new repository:

   - Assign it to a project.
   - Give it a unique name.
   - Set the access level to **Private**.
   - Enable the option to include a **README** file.
   - Set the default branch name to `main`.
   - Select **Create Repository**.

   ![Create a private repository in Bitbucket](images/03_08-00-b-create-private-repository.png)

1. Once created:

   - Select **Clone**, select **HTTPS**, and copy the URL.
   - Paste the URL into a document for later use.
   - **Edit the URL**: remove the username and `@` symbol from the URL.

   ![Get repository URL step 1](images/03_08-01-b-get-repo-url-step-1.png)
   ![Get repository URL step 2](images/03_08-02-b-get-repo-url-step-2.png)

1. Create an access token:

   - Go to **Repository Settings** > **Access Tokens** (under the Security section).
   - Select **Create access token**.
   - Provide a name for the token.
   - Under **Scopes**, check **Read access** for repositories.
   - Select **Create** and **copy** the generated token.
   - Save the token and the modified repository URL somewhere safe for later use.

   ![Create access token in Bitbucket](images/03_08-03-b-create-access-token.png)
   ![Copy the generated access token](images/03_08-04-b-copy-access-token.png)

### 2. Install Plugin and Create a Jenkins Freestyle Project

1. In Jenkins, go to **Manage Jenkins** > **Plugins** > **Available Plugins**.
1. Search for **Bitbucket Push and Pull Request**.
1. Check the box next to the plugin and select **Install**.

   ![Install Bitbucket Push and Pull Request plugin](images/03_08-05-j-install-push-and-pull-request-plugin.png)

1. Once installed, return to the Jenkins dashboard and select **New Item**.
1. Enter a name for your job, select **Freestyle Project**, and select **OK**.

**Configure Source Code Management:**

1. Under **Source Code Management**, select **Git**.
1. Paste the modified repository URL (without username and `@`) into the **Repository URL** field.

   ![Configure SCM with Bitbucket repository URL](images/03_08-06-j-configure-scm-with-bitbucket-repo-url.png)

1. Add credentials to solve the authentication error:

   - Select **Add** next to **Credentials** and choose **Jenkins**.
   - For **Kind**, select **Username and Password**.
   - Username: enter `x-token-auth`.
   - Password: paste the access token.
   - Description: use your Bitbucket username.
   - Select **Add**.

    ![Create credential with Bitbucket access token](images/03_08-07-j-create-credential-with-bitbucket-access-token.png)

1. Back in the job configuration, select the credential you just added from the **Credentials** dropdown.  Confirm the authentication error is resolved.
1. Change the **Branch Specifier** from `master` to `main`.

    ![Apply credential and set branch specifier to main](images/03_08-08-j-apply-credential-set-branch-specifier-to-main.png)

**Configure Triggers and Build Steps:**

1. Scroll down to **Build Triggers**.

    - Check the box for **Build with BitBucket Push and Pull Request Plugin**.
    - Select **Push** under trigger types.

    ![Configure build trigger with Bitbucket plugin](images/03_08-09-j-trigger-build-with-bitbucket-plugin.png)

1. Scroll to **Build** and select **Add build step** > **Execute shell**.

    - Enter the following command:

        ```bash
        cat README.md
        ```

    - Select **Save** to finalize the job configuration.

    ![Add build step to execute shell command](images/03_08-10-j-add-build-step.png)

1. Copy the Jenkins server URL by selecting the icon in the top right, right-click and select **Copy link address**.

   ![Copy Jenkins URL for webhook configuration](images/03_08-11-j-copy-jenkins-url.png)

### 3. Create a Webhook in Bitbucket

1. Return to the Bitbucket repository.
1. Go to **Repository Settings** > **Webhooks** > **Add Webhook**.

   ![Navigate to repository settings and add webhook](images/03_08-12-b-repo-settings-webhooks-add-webhook.png)

1. Fill out the webhook form:

   - Title: enter a descriptive name like "Trigger Jenkins Build".
   - URL: paste your Jenkins URL, followed by `/bitbucket-hook/`. _*NOTE: this part is critical for the webhook to work properly.  If the path is incorrect or the trailing slash is missing, the webhook may fail.*_

        ```bash
        Example: `http://jenkins.example.com/bitbucket-hook/`
        ```

   ![Configure webhook URL with Jenkins endpoint](images/03_08-13-b-configure-webhook-url.png)

   - Under **SSL/TLS**, check **Skip certificate verification** (if Jenkins is using HTTP).
   - Under **Triggers**, check **Push**.
   - Select **Save**.

   ![Configure and save webhook settings](images/03_08-14-b-configure-save-webhook.png)

### 4. Test the Webhook

1. Go back to the repository code view and open the **README.md** file.
1. Select **Edit**, make a small change, and **commit** the update to the `main` branch.

   ![Commit a change to test the webhook](images/03_08-15-b-commit-change.png)

1. In Jenkins, check your freestyle job:

   - Confirm that a new build starts automatically.
   - Wait for the build to complete.

1. Select the build number, then **Console Output**:

   - Verify that the build was triggered by the Bitbucket webhook.
   - Confirm that the correct repository URL was used.
   - Check that your changes appear in the output of the `cat README.md` step.

   ![View console output to verify build](images/03_08-16-j-view-console-output.png)
   ![Confirm repository was cloned successfully](images/03_08-17-j-confirm-repo-clone.png)

## References

- [Bitbucket Documentation: Manage webhooks](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/)

- [Bitbucket Push and Pull Request Plugin](https://plugins.jenkins.io/bitbucket-push-and-pull-request/)

<!-- FooterStart -->
---
[← 03_07 Create and test a webhook with GitLab](../03_07_create_a_webhook_with_gitlab/README.md) | [04_01 Plan the Deployment Target in AWS Lambda →](../../ch4_deploy_code_to_aws_lambda/04_01_plan_the_deployment_target_in_aws_lambda/README.md)
<!-- FooterEnd -->
