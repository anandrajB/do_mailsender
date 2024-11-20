# Cloud Functions: Venzo Mail Sender


## Deploying the Function

```bash
# clone this repo
git clone git@github.com:digitalocean/sample-functions-python-sendgrid-email.git
```

```
# deploy the project, using a remote build so that compiled executable matched runtime environment
> doctl serverless deploy sample-functions-python-sendgrid-email --remote-build
Deploying 'sample-functions-python-sendgrid-email'
  to namespace 'fn-...'
  on host 'https://faas-...'
Submitted action 'emails' for remote building and deployment in runtime python:default (id: ...)

Deployed functions ('doctl sls fn get <funcName> --url' for URL):
  - sample/emails
```

## Using the Function

```bash
doctl serverless functions invoke sample/emails -p from:user@do.com to:user@gmail.com subject:Sammy content:Good Morning from Sammy.
```
```json
{
  "body": "email sent"
}
```

### To send an email using curl:
```
curl -X PUT -H 'Content-Type: application/json' {your-DO-app-url} -d '{"from":"user@do.com", "to":"user@gmail.com", "subject": "Sammy", "content":"Good Morning from Sammy!"}' 
```
