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

1. Select **Launch instance**.

<!-- FooterStart -->
---
[← 02_03 Create a security group and key pair for the build server](../02_03_create_a_security_group_key_pair_for_the_build_server/README.md) | [02_05 Connect Jenkins to the build server →](../02_05_connect_jenkins_to_the_build_server/README.md)
<!-- FooterEnd -->
