# 03_03 Create and test a webhook with GitHub

Follow these steps to set up a webhook in GitHub that triggers a Jenkins job when code is pushed to a repository.

## Get the Repository URL

1. In **GitHub**, open the target repository and copy the repository URL:

   - Select **Code**
   - Select the **HTTPS** tab
   - Select the **clipboard icon** to copy the URL

## Create a Freestyle Job in Jenkins

1. In **Jenkins**, select **New Item**.
2. Enter the name: `webhook-test`, then select **Freestyle project** and select **OK**.
3. Enter a description: `Testing the Jenkins webhook`.
4. Under **Source Code Management**, select **Git** and paste the repository URL.
5. Update the **Branch Specifier** from `master` to `main`.
6. Under **Build Triggers**, select **GitHub hook trigger for GITScm polling**.
7. Scroll to **Build** and:

   - Select **Add build step**
   - Select **Execute shell**
   - Enter the command: `cat README.md`

8. Select **Save**.

## Configure the GitHub Webhook

1. In **Jenkins**, copy the server URL by:

   - Right-selecting the **Jenkins icon** in the top-left corner
   - Selecting **Copy link address**

2. In **GitHub**, return to the repository and:

   - Select **Settings**
   - Select **Webhooks**
   - Select **Add webhook**

3. In the webhook form:

   - **Payload URL**: Paste the Jenkins URL, and **append** `github-webhook/` to the end (including the trailing slash).
   - **Content type**: Select `application/json`
   - Leave other settings as-is, then select **Add webhook**

4. Refresh the page to confirm the webhook was added successfully.

#### c. Test the Webhook

1. In **GitHub**, return to the **Code** tab and select the **pencil icon** next to the `README.md` file.
2. Add a message like:

   ```bash
   If you see this, the webhook test worked. It really did! :D
   ```

3. Select **Commit changes**, then confirm again with **Commit changes**.
4. In **Jenkins**, go to the **Dashboard** and open the `webhook-test` job.
5. Once the build runs, open the **build dropdown** and select **Console Output**.
6. Review the output:

   - Confirm the job was triggered by a GitHub push
   - Verify the build ran on the correct node (`build-server`)
   - Look for Git commands showing repo checkout
   - Confirm the updated README content appears in the log

<!-- FooterStart -->
---
[← 03_02 What's a webhook?](../03_02_whats_a_webhook/README.md) | [03_06 Challenge Connect Jenkins to GitHub →](../03_04_challenge_connect_jenkins_to_github/README.md)
<!-- FooterEnd -->
