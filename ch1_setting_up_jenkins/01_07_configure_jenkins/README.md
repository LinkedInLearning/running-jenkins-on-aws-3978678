# 01_07 Configure Jenkins

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
[← 01_06 Configure NGINX](../01_06_configure_nginx/README.md) | [01_08 Challenge Set up a Jenkins server →](../01_08_challenge_set_up_a_jenkins_server/README.md)
<!-- FooterEnd -->
