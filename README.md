# PopSmoke-bot
## Installation 
To install PopSmoke-bot first install and configure docker.

For a guide on installing docker go [here](https://docs.docker.com/get-docker/) 

Then go to the discord [developer portal](https://discord.com/developers/) and configure the bot 

documentation for this process is [here](https://discord.com/developers/docs/intro)

Finally enter the secret key into the line of the pop_smoke.py file which says

```
test_bot.run("ENTER YOUR KEY HERE")
```

Afterwards go to the directory and run 

```
docker build --tag pop_smoke .
```

After the docker image builds run 

```
docker run -d pop_smoke
```

To add users to the list of people that this bot will play for

Copy the id by right clicking the profile in discord and click Copy ID

Then in discord type 

```
PopSmoke add <Put Discord ID Here>
```

Alternatively you can also go into the source code and put the client id in the line

```
self.special_users = {<Put Discord ID Here>}
```
