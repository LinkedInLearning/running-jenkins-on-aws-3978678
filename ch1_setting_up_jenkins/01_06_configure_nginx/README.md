# 01_06 Configure NGINX

In this lesson you will configure NGINX to act as a reverse proxy for the Jenkins web application.

> [!IMPORTANT]
> Jenkins and NGINX need to already be installed on your EC2 instance.

## 1. Disable the default configuration

1. Connect to the instance and become the `root` user.

    ```bash
    sudo --login
    ```

1. Disable the default NGINX configuration.

    ```bash
    unlink /etc/nginx/sites-enabled/default
    ```

## 2. Add the Jenkins proxy configuration

1. Create the proxy configuration file.

    ```bash
    vim /etc/nginx/conf.d/jenkins.conf
    ```

1. Inside the configuration file, add the following contents:

    Enter `insert` mode in `vim` by typing `i`. Then copy and paste the configuration below.

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

    Press the `esc` key to stop editing.

    Then type `:wq` to save the file and exit.

1. Check the NGINX configuration:

    ```bash
    nginx -t
    ```

    If there are any errors, edit the configuration file to fix them and then test
the configuration again.

1. Once the configuration is testing without errors, reload the configuration:

    ```bash
    systemctl reload nginx
    ```

1. Open a browser to the instance's address and look for the "Unlock Jenkins" page.

<!-- FooterStart -->
---
[← 01_05 Install Java, Jenkins, NGINX](../01_05_install_java_jenkins_nginx/README.md) | [01_07 Configure Jenkins →](../01_07_configure_jenkins/README.md)
<!-- FooterEnd -->
