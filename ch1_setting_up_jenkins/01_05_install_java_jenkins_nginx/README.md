# 01_05 Install Java, Jenkins, NGINX

In this lesson you will:

1. Connect to the Jenkins server using Session Manager.
1. Update the operating system packages.
1. Install Java, Jenkins, and NGINX

## 1. Connect to the Jenkins Server

1. On the EC2 instance homepage select **Connect**.
1. On the "Connect to instance" page, select **Session Manager** then select **Connect**.

## 2. Update the operating system packages

1. Change to the root user:

    ```bash
    sudo --login
    ```

1. Download the aptitude key for the Jenkins application and add the Jenkins Debian repo to the aptitude sources list:

    ```bash
    sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
        https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

    echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
        https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
        /etc/apt/sources.list.d/jenkins.list > /dev/null
    ```

1. Update the source lists and upgrade any out of date packages:

    ```bash
    sudo apt-get update
    ```

## 3. Install Java, Jenkins, and NGINX

Install the software needed to run Jenkins:

- `openjdk-21-jdk`
- `nginx`
- `jenkins`

1. Install JDK and NGINX first:

    ```bash
    apt -y install openjdk-21-jdk nginx
    ```

1. Then install Jenkins:

    ```bash
    apt -y install jenkins
    ```

1. Confirm that Jenkins and NGINX are installed:

    ```bash
    systemctl status nginx | grep Active
    systemctl status jenkins | grep Active
    ```

<!-- FooterStart -->
---
[← 01_04 Create the Jenkins EC2 instance](../01_04_create_the_jenkins_ec2_instance/README.md) | [01_06 Configure NGINX →](../01_06_configure_nginx/README.md)
<!-- FooterEnd -->
