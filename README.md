# polkadot-release


You will need to create a Values.yaml and configure as needed. The Slack intergration will require an API key and invite the app to the channel. Slack Doc's https://api.slack.com/authentication/basics. This will also send a page with pager duty, you will need an API Key. The GitHub API Token will need access to view public repos. schedule and CHECK_TIMER should both be the same and are the time in minutes between checks.

Example Values.yaml
```
schedule: "*/10 * * * *"
CHECK_TIMER: "10"


PAGER_DUTY_API_KEY: "SERIVCE_KEY"
SLACK_API: "API_KEY_FROM_SLACK_FOR_APPLICATION"
PAGER_DUTY_SERVICE_NAME: "NAME OF THE SERVICE TO PAGE"
SLACK_CHANNEL_NAME: "POLKADOT-RELEASE"
GITHUB_API_TOKEN: "ACCESS_TO_PUBLIC_REPOS"
GITHUB_REPO: "paritytech/polkadot"
```

Chart installation:
```
helm repo add polkadot-release https://stkd-io.github.io/polkadot-release/
helm repo update
helm install polkadot-release polkadot-release/polkadot-release -n polkadot-release --create-namespace -f Values.yaml
```


Tips: 
-  KSM: Fq4YmiAq76DntjMKKjMiL98MYszoApUa9idSErvyzfdGoqG 
-  DOT: 12pdN2XsNmG2yPAv5QCkq7YYUg1MM3prvGMgusH7S6FnDHAx
