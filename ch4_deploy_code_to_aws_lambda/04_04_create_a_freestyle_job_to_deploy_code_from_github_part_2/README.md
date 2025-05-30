# 04_04 Create a freestyle job to deploy code from GitHub, part 2

## First Build Step: Create Virtual Environment

```bash
#!/bin/bash

# Check if venv directory exists
if [ ! -d "venv" ]; then
    # Create venv directory and activate it
    virtualenv venv
fi
```

## Second Build Step: Test, Build and, Deploy the Code

```bash
#!/bin/bash -xe

# Activate the venv directory
source venv/bin/activate

make all \
 FUNCTION="REPLACE_WITH_YOUR_FUNCTION_NAME" \
 REGION="REPLACE_WITH_YOUR_REGION" \
 URL="REPLACE_WITH_YOUR_FUNCTION_URL" \
 VERSION="${GIT_COMMIT}" \
 BUILD_TAG="${BUILD_TAG}" \
 BUILD_NUMBER="${BUILD_ID}" \
 ENVIRONMENT="production"
```

## Third Build Step: Test the Deployed Code

```bash
make testdeployment \
 URL="REPLACE_WITH_YOUR_FUNCTION_URL" \
 VERSION="${GIT_COMMIT}"
```

<!-- FooterStart -->
---
[← 04_03 Create a freestyle job to deploy code from GitHub, part 1](../04_03_create_a_freestyle_job_to_deploy_code_from_github_part_1/README.md) | [04_05 Deploy to AWS Lambda from GitHub →](../04_05_deploy_to_aws_lambda_from_github/README.md)
<!-- FooterEnd -->
