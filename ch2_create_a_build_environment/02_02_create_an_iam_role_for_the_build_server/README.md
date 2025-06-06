# 02_02 Create an IAM role for the build server

Follow these steps to create the IAM role that your EC2-based build server will use to access AWS Lambda services:

1. In the **AWS Console**, navigate to the **IAM dashboard**.
2. Select **Roles** from the sidebar, then choose **Create role**.
3. Under **Trusted entity type**, select **AWS service**.
4. For the use case, choose **EC2**, then click **Next**.
5. In the permissions policies search box, type `lambda`.
6. From the filtered list, select the checkbox for **AWSLambda_FullAccess**.
7. Click **Next** until you reach the role name field.
8. Set the **Role name** to `ec2-lambda`.
9. Add a tag:

   - **Key**: `Name`
   - **Value**: `jenkins`

10. Click **Create role**.

Once the role is created, proceed to the next step to configure the **key pair** and **security group** for the build server.

<!-- FooterStart -->
---
[← 02_01 Plan the build environment](../02_01_plan_the_build_environment/README.md) | [02_03 Create a security group and key pair for the build server →](../02_03_create_a_security_group_key_pair_for_the_build_server/README.md)
<!-- FooterEnd -->
