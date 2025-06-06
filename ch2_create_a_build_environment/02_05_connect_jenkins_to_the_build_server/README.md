# 02_05 Connect Jenkins to the build server

Follow these steps to connect your Jenkins server to the EC2-based build server using SSH.

## Copy the Private DNS Name of the Build Server

Using the private IP address for the build server connection has benefits:

- Reduces network costs by minimizing ingress and egress from the AWS network.
- Keeps the connection between the Jenkins server and the build server fast, again, because the public internet is not traversed.
- The private IP address of an Amazon EC2 instance will remain the same after a shutdown and restart.  This saves us from having to reconfigure the connection between the build server and Jenkins if the build server is taken offline.

1. In the **EC2 Console**, open the **Instance Details** for the build server.
2. Locate the **Private DNS (IPv4)** field.
3. Select the **copy icon** next to the DNS name to copy it to your clipboard.

   - Use the private DNS to keep traffic internal to AWS and reduce latency and costs.

## Remove Executors from the Jenkins Server

1. In Jenkins, go to **Manage Jenkins** > **Nodes**.
2. Next to the `Built-In Node` node, select the **configure (gear) icon**.
3. Set **# of Executors** to `0`.
4. Select **Save**.

## Add the Build Server as a New Node

1. In **Manage Jenkins** > **Nodes**, select **New Node**.
2. Enter the node name: `build-server`.
3. Choose **Permanent Agent**, then select **Create**.

## Configure the Build Server Node

1. **Description**: Enter `Amazon Linux 2023`.
2. **# of Executors**: Enter `4`.
3. **Remote Root Directory**: Enter `/home/ec2-user`.
4. **Labels**: Enter `lambda`.
5. **Usage**: Leave as default ("Use this node as much as possible").
6. **Launch method**: Select **Launch agents via SSH**.
7. **Host**: Paste the **private DNS name** copied earlier.
8. **Credentials**: Select the SSH credentials you created (ID: `build-server`, username: `ec2-user`).
9. **Host Key Verification Strategy**: Choose **Non verifying Verification Strategy**.
10. **Availability**: Keep **"Keep this agent online as much as possible"** selected.
11. Leave **Environment Variables** and **Tool Locations** blank.
12. Select **Save**.

## Verify the Connection

1. Wait for the node to finish launching. Jenkins will attempt to connect automatically.
2. Once connected, select the node name: `build-server`.
3. Select **Log** to view connection output and verify that the build server is online.

Your Jenkins server is now connected to the build server and ready to delegate jobs.

<!-- FooterStart -->
---
[← 02_04 Create the build server](../02_04_create_the_build_server/README.md) | [02_06 Challenge Set up a build server →](../02_06_challenge_set_up_a_build_server/README.md)
<!-- FooterEnd -->
