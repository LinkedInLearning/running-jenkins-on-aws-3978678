# 02_07 Solution Set up a build server

In this challenge, you'll create and configure the AWS resources needed to run a build server.

Once the server is online, you’ll connect it to the Jenkins server.

## Overview

1. Create the following AWS resources:

   1. an IAM role that allows full access to AWS Lambda
   1. a security group that allows SSH traffic from the jenkins-server security group
   1. an SSH key for connecting to the build server
   1. an EC2 instance using an Amazon Linux 2023 AMI for the build server. Apply the provided user data to configure the build server

2. Add the SSH key to Jenkins as a credential
3. Add the build server as a new node on the Jenkins server

This challenge should take 15 to 20 minutes to complete.

## Solution

### 1. Create an IAM Role

1. Go to the **IAM Console**, select **Roles**, and select **Create role**
2. For **Trusted entity type**, keep **AWS service** selected
3. For **Use case**, choose **EC2**, then select **Next**
4. Search for **AWSLambdaFullAccess**, check the box next to it, and select **Next**
5. Name the role `ec2-lambda`
6. Add a tag with key: `Name`, value: `jenkins`
7. Select **Create role**

### 2. Create a Security Group

1. Go to the **EC2 Console**, select **Security Groups**, then select **Create security group**
2. Name it `build-server` and enter a description like `SSH from jenkins-server`
3. Under **Inbound rules**, add a rule

   - Type: `SSH`
   - Source: select **Custom**, then search and select the **Jenkins server's security group**
   - Description: `SSH from jenkins-server`

4. Add a tag with key: `Name`, value: `build-server`

5. Select **Create security group**

### 3. Create a Key Pair

1. In the **EC2 Console**, navigate to **Key Pairs**
2. Select **Create key pair**
3. Name it `build-server`, choose **ED25519** and **PEM** format
4. Add a tag with key: `Name`, value: `build-server`
5. Download and save the key file safely—you'll need it for the next step

### 4. Add the SSH Key to Jenkins

1. From the **Jenkins Dashboard**, go to: **Manage Jenkins → Credentials → (Global) → Add Credentials**
2. For **Kind**, choose **SSH Username with Private Key**
3. Use the following

   - **ID**: `build-server`
   - **Username**: `ec2-user`
   - **Private Key**: Select **Enter directly** and paste the contents of your PEM file

4. Select **OK** to save

### 5. Launch the Build Server (EC2 Instance)

1. From the **EC2 Dashboard**, select **Launch instance**
2. Enter `build-server` as the instance name
3. Choose **Amazon Linux 2023** as the AMI and **t2.micro** as the instance type
4. Under **Key pair**, select `build-server`
5. Under **Network settings**, choose **Select existing security group** and attach the `build-server` security group
6. Under **Storage**, increase the volume size to **20 GB**
7. Expand **Advanced details**, and

   - Set the **IAM instance profile** to `ec2-lambda`
   - Paste in the following **user data** script:

    ```bash
    #!/bin/bash
    set -eux

    # Log the installation output
    exec > >(tee /var/log/user-data.log) 2>&1

    # Unmount /tmp if already mounted
    umount /tmp || true

    # Create the /tmp directory if it doesn't exist
    mkdir -p /tmp

    # Backup /etc/fstab
    cp /etc/fstab /etc/fstab-$(date +%s).bak

    # Remove any existing /tmp entry (just in case)
    sed -i '/\/tmp/d' /etc/fstab

    # Add a new tmpfs entry for /tmp with 4G size
    echo "tmpfs /tmp tmpfs defaults,size=4G 0 0" >> /etc/fstab

    # Mount all filesystems in fstab (including /tmp)
    mount -a

    # Set correct permissions for /tmp
    chmod 1777 /tmp

    # install the ssm-agent
    dnf install --assumeyes \
        https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm

    # install java and python
    dnf install --assumeyes \
        java-21-amazon-corretto-headless \
        python3.12.x86_64

    # install development tools
    dnf groupinstall -y "Development Tools"

    reboot now
    ```

8. Select **Launch instance**

### 6. Connect the Build Server to Jenkins

1. In the **EC2 Console**, go to your instance and copy its **Private DNS name** (e.g., `ip-10-0-0-123.ec2.internal`)
2. In Jenkins

   - Go to **Manage Jenkins → Nodes**
   - Set the **# of executors** on the built-in node to `0` and select **Save**
   - Select **New Node**

3. Enter `build-server` as the node name, choose **Permanent Agent**, and select **Create**
4. Fill out the configuration

   - **Description**: `Amazon Linux 2023`
   - **# of Executors**: `4`
   - **Remote root directory**: `/home/ec2-user`
   - **Labels**: `lambda`
   - **Usage**: Leave default
   - **Launch method**: **Launch agents via SSH**

     - **Host**: Paste the private DNS name
     - **Credentials**: Select the `ec2-user` SSH key you added earlier
     - **Host Key Verification Strategy**: Choose **Non verifying verification strategy**

5. Select **Save**
6. Wait for the node to connect. Then view the logs to verify the connection was successful.

<!-- FooterStart -->
---
[← 02_06 Challenge Set up a build server](../02_06_challenge_set_up_a_build_server/README.md) | [03_01 Plan the CI/CD pipeline →](../../ch3_connect_jenkins_with_webhooks/03_01_plan_the_cicd_pipeline/README.md)
<!-- FooterEnd -->
