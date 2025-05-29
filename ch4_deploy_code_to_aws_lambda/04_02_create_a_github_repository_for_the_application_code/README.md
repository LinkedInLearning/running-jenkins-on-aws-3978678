# 04_02 Create a GitHub repository for the application code

In this lab, you'll set up a new GitHub repository and upload the application code that will later be deployed to AWS Lambda.

Using Git-based source control is an essential step in the deployment workflow because it ensures your code is versioned and accessible to Jenkins.

This lab should take 5 to 10 minutes to complete.

## Overview

1. Download the exercise files
1. Create a GitHub repository
1. Upload the code into the repo
1. Copy the repo URL

## Instructions

### 1. Download the Exercise Files

> [!NOTE]
> If you've already downloaded the exercise files, you can skip this step!

1. Navigate to the home page of the course repository.
2. Select **Code** and choose **Download ZIP**.
3. Extract the contents of the ZIP file to your local system.
4. Locate the folder for this lesson: `ch4_deploy_code_to_aws_lambda/04_02_create_a_github_repository_for_the_application_code`.

### 2. Create a GitHub Repository

1. Log into your GitHub account.
1. Go to [github.com/new](https://github.com/new) to create a new repository.
1. In the **Repository name** field, enter: `python-api`
1. In the **Description** field, enter: `Python API`
1. Leave the repository as **Public**.
1. Check the box to **Add a README file**.
1. Check the box to **Add .gitignore** and select **Python** from the dropdown.
1. Select **Create repository** to finalize the setup.

### 3. Upload the Code into the Repo

1. From the new repository page, select **Add file** and select **Upload files**.
1. Select **Choose your files**.
1. Browse to the extracted exercise files and open the folder: `04_02_create_a_github_repository_for_the_application_code`.
1. Select all files in this folder and select **Open**.
1. Select **Commit changes** to upload the files to your GitHub repository.

### 4. Copy the Repo URL

1. On the repo homepage, select **Code** and then select **HTTPS**.
1. Select the **stacked squares** icon to copy the URL to your system clipboard.

You're now ready to move on to creating the deployment job in Jenkins.

<!-- FooterStart -->
---
[← 04_01 Initialize the deployment target in AWS Lambda](../04_01_initialize_the_deployment_target_in_AWS_Lambda/README.md) | [04_03 Create a freestyle job to deploy code from GitHub, part 1 →](../04_03_create_a_freestyle_job_to_deploy_code_from_github_part_1/README.md)
<!-- FooterEnd -->
