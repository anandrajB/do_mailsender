# Cloud Functions: Venzo Mail Sender


## Deploying the Function

```bash
# clone this repo
git clone https://github.com/venzo-tech/DO_MailSender.git
```

```
# deploy the project, using a remote build so that compiled executable matched runtime environment
> doctl serverless deploy venzo-mail-sender --remote-build
Deploying 'venzo-mail-sender'
  to namespace 'fn-...'
  on host 'https://faas-...'
Submitted action 'emails' for remote building and deployment in runtime python:default (id: ...)

Deployed functions ('doctl sls fn get <funcName> --url' for URL):
  - venzo-mail-sender/emails
```

## Using the Function

```bash
doctl serverless functions invoke venzo-mail-sender/emails -p from_email:user@do.com from_name: venzo-tech to_email:user@gmail.com subject:Greetings content:Good Morning , Greetings from Venzo Tech!.
```
```json
{
    "from_email": "venzotech@venzo.com",
    "from_name": "Venzo Tech",
    "to_email": "toemail@gmail.com",
    "subject": "OTP Test Email",
    "content": "<p>This is a test email.</p>",
}
```

### To send an email using curl:
```
curl -X PUT -H 'Content-Type: application/json' {your-DO-app-url} -d '{"from_email":"user@do.com", "from_name" : "venzotech" ,"to_email":"user@gmail.com", "subject": "Greetings", "content":"Good Morning , Greetings from Venzo Tech!"}' 
```
