```
bodywork setup-namespace turbo-waffle

bodywork deployment create \
    --namespace=turbo-waffle \
    --name=training \
    --git-repo-url=https://github.com/mtszkw/turbo_waffle \
    --git-repo-branch=main \
    --local-workflow-controller
```