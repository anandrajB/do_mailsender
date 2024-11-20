# Cloud Functions: Venzo Mail Sender


## Deploying the Function

```bash
# clone this repo
git clone https://github.com/venzo-tech/DO_MailSender.git
```

```

- doctl serverless deploy .
- doctl serverless deploy venzo-mail-sender --remote-build
Deploying 'venzo-mail-sender'
  to namespace 'fn-...'
  on host 'https://faas-...'
Submitted action 'emails' for remote building and deployment in runtime python:default (id: ...)

Deployed functions ('doctl sls fn get <funcName> --url' for URL):
  - venzo-mail-sender/emails
```

## Using the Function


### using doctl
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


### http call


- from_email = "myemail@domain.com"
- from_name = "email_from_name"
- to_email  = "toemail@gmail.com"
- subject = "my subject"
- content = "my email content"
```
https://faas-blr1-8177d592.doserverless.co/api/v1/web/fn-a0613c26-e2da-4f68-a59c-7ab42b9d079f/venzo-mail-sender/emails/?from_email=venzotech@venzo.com&from_name=Venzo%20Tech&to_email=touser@gmail.com&subject=OTP%20Test%20Email&content=%3Cp%3EThis%20is%20a%20test%20email.%3C/p%3E

```