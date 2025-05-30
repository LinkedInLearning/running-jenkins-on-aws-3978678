# 04_04 Create a freestyle job to deploy code from GitHub, part 2

In this lab, you’ll complete the configuration of a Jenkins job that automates a deployment to AWS Lambda.

You’ll add the necessary build steps, use values from your CloudFormation stack, and manually run the job to verify that the deployment works. This is your final step in building a complete CI/CD pipeline from code to cloud!

## Overview

For easy reference, make sure you have the following tabs open in your browser:

- **Tab 1**: GitHub repository with the application code
- **Tab 2**: Jenkins job configuration screen (editing the `python-api` job)
- **Tab 3**: Exercise files for this challenge
- **Tab 4**: AWS CloudFormation Outputs page for the `python-api` stack
- **Tab 5**: The deployed Python API (should show a welcome page)

Follow these steps to complete the lab:

1. **Finish the Jenkins Job Configuration**
2. **Update the build step with values from CloudFormation**
3. **Run the Jenkins job manually to confirm everything works**

## Instructions

### 1. Finish the Jenkins Job Configuration

1. In Jenkins, edit the `python-api` job.
1. Add three build steps by selecting **Add build step** > **Execute shell**.
1. Create three build steps in the deployment job and copy the commands below into each step accordingly.

#### First Build Step: Create Virtual Environment

```bash
#!/bin/bash

# Check if venv directory exists
if [ ! -d "venv" ]; then
    # Create venv directory and activate it
    virtualenv venv
fi
```

#### Second Build Step: Test, Build and, Deploy the Code

```bash
#!/bin/bash -xe

# Activate the venv directory
source venv/bin/activate

# Run commands to test, build, and deploy the code
make all \
 FUNCTION="REPLACE_WITH_YOUR_FUNCTION_NAME" \
 REGION="REPLACE_WITH_YOUR_REGION" \
 URL="REPLACE_WITH_YOUR_FUNCTION_URL" \
 VERSION="${GIT_COMMIT}" \
 BUILD_TAG="${BUILD_TAG}" \
 BUILD_NUMBER="${BUILD_ID}" \
 ENVIRONMENT="production"
```

#### Third Build Step: Test the Deployed Code

```bash
#!/bin/bash -xe

# Run commands to test the deployed code
make testdeployment \
 URL="REPLACE_WITH_YOUR_FUNCTION_URL" \
 VERSION="${GIT_COMMIT}"
```

### 2. Update the Build Step with Values from CloudFormation

1. In the Jenkins job configuration, locate placeholder values in the pasted code such as:

    - `REPLACE_WITH_YOUR_REGION`
    - `REPLACE_WITH_YOUR_FUNCTION_NAME`
    - `REPLACE_WITH_YOUR_FUNCTION_URL`

1. Go to CloudFormation stack for the Lambda function and select the **Outputs** tab.
1. Copy the values for the following outputs and paste them into the Jenkins job accordingly:

    | Output Key       | Value Replaces                    |
    |------------------|-----------------------------------|
    | **AwsRegion**    | `REPLACE_WITH_YOUR_REGION`        |
    | **FunctionName** | `REPLACE_WITH_YOUR_FUNCTION_NAME` |
    | **FunctionURL**  |`REPLACE_WITH_YOUR_FUNCTION_URL`   |

1. Select **Save** to finish configuring the job.

### 3. Run the Jenkins Job Manually to Confirm Everything Works

1. View the current version of the deployed API homepage. It should still show the placeholder page.
1. In Jenkins, select **Build Now** to run the job.
1. Wait for the build to complete.

   - Select the build number in the **Build History**
   - Select **Console Output** to review the logs and confirm all steps executed successfully

1. Return to the application tab and reload the page.
1. If successful, the placeholder page will be replaced with your deployed application.

> [!TIP]
> If the job fails or the app doesn’t deploy correctly, review the console output for errors and update your Jenkins job configuration as needed.

## Shenanigans and Extra Credit

Use the following observations to expand your skill with Jenkins.

1. **Add Parameters**: The deployment job could be updated to use parameters.  That would keep us from having to hard code values into the build steps for the function name, function URL, region, and environment in the build steps.

    - Update the job to use **String** parameters for:

        - FUNCTION_NAME
        - REGION
        - FUNCTION_URL

    - Use the CloudFormation output values as the defaults.
    - Update the build steps to use the parameter variables instead of hard-coded values.

1. **Archive Artifacts**: It might be beneficial to make the build artifact more accessible after the job completes.

    - Add a **Post-Build Action** to archive the file named `lambda.zip` created by the build step.

<!-- FooterStart -->
---
[← 04_03 Create a freestyle job to deploy code from GitHub, part 1](../04_03_create_a_freestyle_job_to_deploy_code_from_github_part_1/README.md) | [04_05 Deploy to AWS Lambda from GitHub →](../04_05_deploy_to_aws_lambda_from_github/README.md)
<!-- FooterEnd -->
