from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    ""MTA2MjY2NDA4NjExNjEyNjgwMQ.Gl4zXw.GRnYC5LnIgtQ23Inagp8MbxiRknvH3Ad97qfUQ"":
    "1102092681422852186"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
