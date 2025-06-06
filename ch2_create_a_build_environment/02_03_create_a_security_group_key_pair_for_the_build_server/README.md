# 02_03 Create a security group and key pair for the build server

## Create the Security Group

1. Navigate to the **EC2 Dashboard**, and under **Network & Security**, select **Security Groups**.
2. Select **Create Security Group**.
3. Set the **Security group name** to `build-server`.
4. Enter a **description** such as `SSH from jenkins-server`.
5. Leave the **VPC** setting as default.
6. Add an **inbound rule**:

   - Type: `SSH`
   - Port Range: `22`
   - Source: **Custom** → Select the security group for `jenkins-server`
   - Description: `SSH from jenkins-server`

7. Leave the **outbound rules** as-is (allowing all traffic).
8. Add a tag:

   - **Key**: `Name`
   - **Value**: `build-server`

9. Select **Create security group**.

## Create the Key Pair

1. From the **EC2 Dashboard**, select **Key Pairs** from the sidebar.
2. Click **Create Key Pair**.
3. Name the key pair `build-server`.
4. Set the **Key type** to `ED25519`.
5. Set the **Private key format** to `PEM`.
6. Add a tag:

   - **Key**: `Name`
   - **Value**: `build-server`

7. Click **Create Key Pair**.
8. The key file will automatically download—save it securely.

## Add the Private Key to Jenkins

1. Open the key file in a text editor (e.g., VS Code) and copy the entire contents of the private key.
2. In the Jenkins dashboard:

   - Select **Manage Jenkins**
   - Choose **Credentials**
   - Under **Stores scoped to Jenkins**, select **(global)**, then click **Add Credentials**

3. Set the **Kind** to `SSH Username with private key`.
4. Set the **ID** to `build-server`.
5. Set the **Username** to `ec2-user`.
6. Under **Private Key**, choose **Enter directly**, then click **Add**.
7. Paste in the private key you copied earlier.
8. Leave the **Passphrase** field blank.
9. Click **Create** to save the credential.

Move on to the next step to create the build server.

<!-- FooterStart -->
---
[← 02_02 Create an IAM role for the build server](../02_02_create_an_iam_role_for_the_build_server/README.md) | [02_04 Create the build server →](../02_04_create_the_build_server/README.md)
<!-- FooterEnd -->
