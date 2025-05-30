# 01_08 Challenge Set up a Jenkins server

## **Introduction**

In this challenge, you’ll create and configure the AWS resources needed to host a Jenkins server.

The challenge walks through the full setup process: from provisioning infrastructure in AWS to installing and configuring Jenkins with NGINX as a reverse proxy.

## **Overview**

You will complete  the following steps in this challenge:

1. **Create an IAM role** that allows EC2 instances to be accessed via Systems Manager (SSM).
1. **Create a security group** that enables HTTP and HTTPS access to your server.
1. **Create the Jenkins EC2 instance** using an Ubuntu AMI, associate the IAM role and security group, and assign an Elastic IP.
1. **Install Java, Jenkins, and NGINX** using the AWS Systems Manager session.
1. **Configure NGINX** to serve as a reverse proxy for Jenkins.
1. **Configure Jenkins** by unlocking it, installing default plugins, and setting up an admin account.

## **Instructions**

### **Create an IAM Role**

1. In the AWS Console, navigate to the **IAM dashboard**.
1. Select **Roles** from the sidebar, then choose **Create role**.
1. Select **AWS service** as the trusted entity, and choose **EC2** as the use case.
1. Select **Next** until you reach the name field.
1. Name the role `ec2-ssm`.
1. Add a tag: Key = `Name`, Value = `jenkins`.
1. Select **Create role**.

### **Create a Security Group**

1. Navigate to the **EC2 Dashboard** and select **Security Groups** under Network & Security.
1. Select **Create Security Group**.
1. Name the group `jenkins-server` and add a description like `Allow web traffic`.
1. Keep the default VPC setting.
1. Add the following **inbound rules**:

    - HTTP (port 80) from **Anywhere (IPv4)**
    - HTTPS (port 443) from **Anywhere (IPv4)**

1. Leave the **outbound rules** as-is (allowing all traffic).
1. Add a tag: Key = `Name`, Value = `jenkins-server`.
1. Select **Create security group**.

### **Create the Jenkins EC2 Instance**

1. On the EC2 Dashboard, select **Launch Instance**.
1. Set the instance name to `jenkins-server`.
1. Choose the AMI: **Ubuntu Server 24.04 LTS**.
1. Choose instance type: **t2.micro** (eligible for free tier).
1. Under **Key pair**, choose **Proceed without a key pair**.
1. Under **Network settings**:

    - Enable **Auto-assign Public IP**.
    - Select the existing security group: `jenkins-server`.

1. Under **Storage**, set the root volume size to **20 GB**.
1. Under **Advanced Details**, select the IAM role: `ec2-ssm`.
1. Select **Launch Instance**.
1. After launching, allocate a new **Elastic IP**.
1. Associate the Elastic IP with the EC2 instance.

#### **Install Java, Jenkins, and NGINX**

1. From the EC2 instance page, select **Connect**, then use **Session Manager** to open a terminal session.
1. Run `sudo --login` to switch to the root user.
1. Clear the screen with `Ctrl+L`.
1. Copy and run the following commands (in order):

    - Add Jenkins repo key and list:

        ```bash
        wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
        sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
        ```

    - Update packages and install software:

        ```bash
        apt update
        apt install -y openjdk-8-jdk nginx jenkins
        ```

    - Verify installations:

        ```bash
        systemctl status nginx
        systemctl status jenkins
        ```

#### **Configure NGINX**

1. In the EC2 Dashboard, copy the **Public IPv4 DNS** of your instance.
1. Open a browser and go to `http://<public_dns>` — you should see the NGINX welcome page. _*NOTE: Be sure to use `http` vs `https` when viewing the public DNS in a browser.*_
1. In your terminal session:

    - Remove the default NGINX configuration.

        ```bash
        unlink /etc/nginx/sites-enabled/default
        ```

    - Add the Jenkins proxy configuration in `/etc/nginx/conf.d/jenkins.conf`:

        ```bash
        upstream jenkins {
            server 127.0.0.1:8080;
        }

        server {
            listen 80 default_server;
            listen [::]:80  default_server;
            location / {
                proxy_pass http://jenkins;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
            }
        }
        ```

    - Test the updated configuration by running `nginx -t`.
    - Reload NGINX by running `systemctl reload nginx`.

1. Refresh the browser. You should now see the Jenkins "Unlock" screen.

#### **Configure Jenkins**

1. On the Unlock Jenkins page, copy the path to the initial admin password.
1. In the terminal, display the password:

    ```bash
    cat /var/lib/jenkins/secrets/initialAdminPassword
    ```

1. Copy the password and paste it into the Unlock Jenkins screen. Select **Continue**.
1. Choose **Install suggested plugins**.
1. After plugins install, fill in the form to create an admin user.
1. Accept the default Jenkins URL and select **Save and Finish**.
1. Select **Start using Jenkins** to complete the setup.

<!-- FooterStart -->
---
[← 01_07 Configure Jenkins](../01_07_configure_jenkins/README.md) | [01_09 Solution Set up a Jenkins server →](../01_09_solution_set_up_a_jenkins_server/README.md)
<!-- FooterEnd -->
