# 02_04 Create the build server

> [!IMPORTANT]
> An IAM role and EC2 Key Pair should already be in place before creating the build server.

1. On the EC2 Dashboard, select **Launch instance**.
1. Enter the name `build-server`.
1. Under **Application and OS Images (Amazon Machine Image)**, select **Amazon Linux**.
1. Under **Instance type**, select **t2.micro**.
1. Under **Key pair (login)**, select **build-server**.
1. Under **Network settings**, choose **Select existing security group**.
1. Under **Common security groups**, select **build-sever**.
1. Under **Configure storage**, increase the storage to `20` GB.
1. Open the **Advanced details** section.
1. Under **IAM instance profile**, select **ec2-lambda**.
1. Under **User data**, enter the following:

    ```bash
    # !/bin/bash

    # install dependencies

    yum -y group install "Development Tools"
    yum -y install \
            bzip2-devel.x86_64 \
            java-21-amazon-corretto-headless \
            libffi-devel \
            ncurses-devel \
            openssl-devel \
            python3 \
            readline-devel.x86_64 \
            sqlite-devel.x86_64 \
            zlib-devel
    ```

1. Select **Launch instance**.

<!-- FooterStart -->
---
[← 02_03 Create a security group and key pair for the build server](../02_03_create_a_security_group_key_pair_for_the_build_server/README.md) | [02_05 Connect Jenkins to the build server →](../02_05_connect_jenkins_to_the_build_server/README.md)
<!-- FooterEnd -->
