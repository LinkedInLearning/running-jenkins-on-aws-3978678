# 03_07 Solution Connect Jenkins to GitHub

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
4. Make a change to the GitHub repository to trigger the Jenkins job and review the console output

This challenge should take 15 to 20 minutes to complete.

## **Instructions**

### 1. Create a Public GitHub Repository and Copy the URL

1. Open [GitHub](https://github.com) and create a new **public repository**.
2. Name the repository and **initialize it with a README file**.
3. From the repository page, select the **Code** button.
4. Select the **HTTPS** tab.
5. Select the **clipboard** icon to copy the URL.

### 2. Create and Configure a Jenkins Freestyle Project

1. Open the **Jenkins dashboard**.
1. Select **New Item**.
1. Enter the name: `webhook-test`.
1. Select **Freestyle project**, then select **OK**.
1. In the job configuration screen, under **Description**, enter: `Testing the Jenkins webhook`.

1. **Source Code Management**

    - Select **Source Code Management** > **Git**.
    - Paste the GitHub repository URL into the **Repository URL** field.
    - Change the **Branch Specifier** to `*/main`

1. **Add a Build Trigger**

    - Select **Build Triggers**.
    - Check the box next to **GitHub hook trigger for GITScm polling**.

1. **Add a Build Step and save the job**

    - Scroll to the **Build** section.
    - Select**Add build step** > **Execute shell**.
    - Enter the following command:

        ```bash
        cat README.md
        ```

    - Select**Save**.

### 3. Configure the GitHub Webhook

1. In Jenkins, copy the base URL of your Jenkins server.
   (Copy it from the browser bar or right-select the Jenkins logo and select **Copy link address**.)
2. In GitHub, go to your repository and select **Settings**.
3. Select **Webhooks** in the left menu.
4. Select **Add webhook**.

    - Paste the Jenkins server URL into the **Payload URL** field.
    - At the end of the URL, append `/github-webhook/`
    - Make sure there is a **trailing slash**!
    - Set **Content type** `application/json`
    - Leave the remaining settings unchanged and select **Add webhook**.

### 4. Trigger the Jenkins Job and Review Output

1. In GitHub, return to the **Code** tab of the repository.
1. Select the **pencil icon** to edit the `README.md` file.
1. Make small change to the file.
1. Select **Commit changes**.
1. In Jenkins, go to the **webhook-test** job.
1. Wait for the build to be triggered automatically.
1. Once the build finishes, select the **dropdown next to the build number** and select **Console Output**.
1. Review the output:

   - Confirm that the build was triggered by a GitHub push.
   - Check the Git clone steps and build environment.
   - Verify that the modified contents of `README.md` are displayed.

<!-- FooterStart -->
---
[← 03_06 Challenge Connect Jenkins to GitHub](../03_04_challenge_connect_jenkins_to_github/README.md) | [README →](../03_06_webhooks_with_other_services/README.md)
<!-- FooterEnd -->
