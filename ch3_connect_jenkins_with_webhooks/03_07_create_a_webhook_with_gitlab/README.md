# 03_07 Create and test a webhook with GitLab

Follow the steps in this document to create a webhook that connects a Jenkins job to a GitLab repository.

The goal is to have push commits to the GitLab repository trigger the Jenkins job to check out the code and run build steps.

## Overview

1. Create a GitLab repo and an API token in GitLab that allows read access to a repository
2. Install the GitLab plugin to provide webhook functionality
3. Configure a Jenkins freestyle project that:
   1. Uses the GitLab repository for the SCM configuration
   2. Listens for push notifications from GitLab
4. Create a wehbook in GitLab that will notify Jenkins when a push event occurs on the repository

This challenge should take 15 to 20 minutes to complete.

## Instructions

### 1. Set Up GitLab

1. **Create a GitLab Repository**

   - Sign in to GitLab and create a **private repository**.
   - Ensure the repository includes a `README.md` file.

1. **Copy the Repository URL**

   - In the repository, select **Code**, then under **Clone with HTTPS** select the **clipboard icon** to copy the URL.

   ![Copy the GitLab repository URL from the Clone with HTTPS section](images/03_04-02-g-copy-the-repo-url.png)

1. **Create an Access Token**

   - Go to **User Settings > Access Tokens**.
   - Create a new token with the following settings:

     - **Name**: Any descriptive name (e.g., `Jenkins Access`)
     - **Scopes**: Select **read_repository**
   - Copy and save the token somewhere safe—you will need it later.

   ![Create a new access token in GitLab with read_repository scope](images/03_07-00-g-create-an-access-token.png)

### 2. Configure Jenkins

1. **Install the GitLab Plugin**

   - Go to **Manage Jenkins > Plugins  > Available Plugins**.
   - Search for `gitlab-plugin`.
   - Select the checkbox next to the plugin and select **Install**.

   ![Install the GitLab plugin in Jenkins from the Available Plugins section](images/03_07-01-j-install-the-plugin.png)

1. **Create a New Jenkins Job**

   - On the Jenkins dashboard, select **New Item**.
   - Enter a name for your project.
   - Choose **Freestyle project** and select **OK**.

1. **Set Up Source Code Management**

   - Under **Source Code Management**, select **Git**.
   - Paste the GitLab repository URL you copied earlier.
   - You will likely see an authentication error at this point.

   ![Add GitLab repository URL to Jenkins SCM configuration and create credentials](images/03_07-03-j-add-the-repo-url-to-scm-and-create-credentials.png)

1. **Add GitLab Credentials**

   - select **Add > Jenkins** under the **Credentials** dropdown.
   - For **Kind**, select **Username with password**.
   - Enter your **GitLab username** and paste the **access token** into the password field.
   - select **Add**.

   ![Create username with password credential in Jenkins for GitLab access](images/03_07-04-j-create-username-with-password-credential.png)

1. **Select Your Credentials**

   - Back under **Source Code Management**, select the new credentials you just added from the **Credentials** dropdown.

   ![Select the newly created GitLab credentials in Jenkins SCM configuration](images/03_07-05-j-select-the-credential.png)

1. **Configure Branches**

   - Under **Branch Specifier**, change the value from `*/master` to `*/main`, or clear it entirely to allow builds on any branch.

1. **Enable GitLab Webhook Trigger**

    - Scroll to the **Build Triggers** section.
    - Check the box for **Build when a change is pushed to GitLab**.
    - Copy the **Webhook URL** shown on screen.

    ![Enable GitLab webhook trigger and copy the webhook URL in Jenkins](images/03_07-06-j-add-trigger-for-copy-webhook-url.png)

    - Select **Advanced**, scroll to the bottom, and select **Generate** to create a secret token.
    - Copy the **Secret Token** and save it along with the Webhook URL.

    ![Generate and copy the secret token in Jenkins webhook configuration](images/03_07-07-j-advanced-create-secret-token.png)

1. **Add a Build Step**

    - Scroll to **Build** and select **Add build > Execute shell**.
    - In the command field, enter:

      ```bash
      cat README.md
      ```

    - Select **Save** to finish creating the job.

    ![Add build step to execute shell command and save the Jenkins job](images/03_07-08-j-add-build-step-save-job.png)

### 3. Create the Webhook in GitLab

1. **Add a Webhook**

    - In your GitLab repository, go to **Settings > Webhooks**.
    - Select **Add New Webhook**.

    ![Navigate to Webhooks section in GitLab repository settings](images/03_07-09-g-settings-webhook.png)

    ![Click Add New Webhook button in GitLab repository settings](images/03_07-10-g-add-webhook.png)

1. **Fill in Webhook Details**

    - **URL**: Paste the Jenkins Webhook URL.
    - **Secret Token**: Paste the token you copied from Jenkins.
    - **Trigger**: Select **Push events**.
    - (Optional) Disable SSL verification if your Jenkins server does not use HTTPS.
    - Select **Add Webhook**.

    ![Configure webhook details with Jenkins URL and secret token](images/03_07-11-g-configure-the-webhook.png)

    ![Disable SSL verification option in GitLab webhook configuration](images/03_07-12-g-disable-ssl-verification.png)

1. **Test the Webhook**

    - Select **Test > Push Events** to test the webhook connection.

    ![Test the webhook connection using Push Events option](images/03_07-13-g-test-the-webhook.png)

    ![Confirm successful webhook test in GitLab](images/03_07-14-g-confirm-webhook-success.png)

1. **Verify the Integration**

    - Make a small edit to the `README.md` file in GitLab.
    - Commit the change.

    ![Make a change to the README.md file in GitLab](images/03_07-15-g-make-a-change.png)

    - In Jenkins, open your project and view the **Console Output**.
    - Confirm that the build was triggered by the GitLab push event.

    ![View the successful Jenkins build triggered by GitLab push event](images/03_07-16-j-confirm-job-ran.png)

<!-- FooterStart -->
---
[← 03_03 Create and test a webhook with GitHub](../03_03_create_a_webhook_with_github/README.md) | [03_05 Create and test a webhook with Bitbucket →](../03_05_create_a_webhook_with_bitbucket/README.md)
<!-- FooterEnd -->
