# 03_04 Create and test a webhook with GitLab (TEXT)

- [Integrating GitLab with Jenkins](https://docs.gitlab.com/integration/jenkins/)

1. Jenkins -install plugin (see older image)
1. Gitlab - create repo, create access token with `read_repository` permission.
1. Gitlab - Get the repo HTTPS URL
1. Jenkins - Create a freestyle project named `gitlab-webhook-test`.
1. Jenkins - add the repo URL to Git SCM; create a credential
1. Jenkins - select the credential to use with the repo; clear the branch specifier to allow builds for all branches.
1. Jenkins - Triggers, select "Build when a change is pushed to Gitlab..." with at least "Push Events" selected.
1. Jenkins - make a note of the webhook URL
1. Jenkins - Under Gitlab build trigger, select advanced, generate secret token, save the token
1. Jenkins - Add a build step and save the job
1. Jenkins - save the URL for the job (copy link)
1. Gitlab repo - settings -> webhooks; add new webhook
1. Gitlab - name the repo, description, add the URL, add the secret token, select push events
1. Gitlab - disable SSL verification, select add webhook
1. Gitlab - test the webhook using a push event
1. Gitlab - confirm the push was successful
1. Jenkins - confirm push activated the project. If test push results in failure, check branch specifier in Jenkins and secret token configurations in Jenkins and GitLab.
1. Gitlab - edit the README.md file and commit the changes
1. Jenkins - confirm the push and the output

<!-- FooterStart -->
---
[← 03_03 Create and test a webhook with GitHub](../03_03_create_a_webhook_with_github/README.md) | [03_05 Create and test a webhook with Bitbucket (TEXT) →](../03_05_create_a_webhook_with_bitbucket/README.md)
<!-- FooterEnd -->
