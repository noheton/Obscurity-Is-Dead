Thanks for the invitation.
My goal is as well controlling my SpiderFarmer Setup from Home Assistant.
Currently looking into the mqtt connection:
- DNS rewrite to connect my MQTT broker
- Added the certificates from apk: ca-sf.pem, emqx-sf.pem, emqx-sf.key
- Controller seems to accept connection (TLS pinning)
- Tries to auth with user: `[REDACTED:username:S-SF-5-username]`
- But I am still looking for the password, so my server denies connection. The password might be `[REDACTED:credential:S-SF-5-password]`, but that does not seem to work.

on the home assitant side i am building a proper extension (taking the BLE address), relying on the ESPHome BTProxy, but I cant decrypt the packages.

My Hardware:
- Lamp SF-G4500, v1.7
- Controller: SF-GGS-CB, v3.14

Happy for any hints and pointers.
Ill letz you know if my mqtt adventures lead somewhere.

UPDATE:
I managed to trick the controller to connect to my MQTT Broker.
Comment: really stupid to use self-signed certificates, enabling this kind of attack...

The password is actually `[REDACTED:credential:S-SF-5-password]` (notice the dash at the end)

The same credentials are also accepted by the the official server.

<img width="1907" height="1526" alt="Image" src="https://github.com/user-attachments/assets/7a231831-d08a-440a-a91c-be465c95ba6a" />

```json
{
  "method": "getDevSta",
  "pid": "<redacted>",
  "pcode": 1004,
  "uid": "<redacted>",
  "UTC": 1776595864,
  "code": 200,
  "msg": "ok",
  "data": {
    "alarmLast": {
      "id": 3,
      "epoch": 1776416472,
      "devType": 16,
      "alarmType": 3
    },
    "oplogLast": {
      "id": 246,
      "epoch": 1776595620,
      "devType": 21,
      "modeType": 2
    },
    "plan": {
      "isPlanRun": 1,
      "stageId": 1776498625,
      "planedTotalDays": 5,
      "planedDays": 1,
      "planRemainDays": 4,
      "planProgress": 20
    },
    "sensor": {
      "temp": 24.1,
      "humi": 62.2,
      "vpd": 1.13,
      "isDayEnvTarget": 1,
      "isDaySensor": 0
    },
    "light": {
      "on": 1,
      "level": 20
    },
    "light2": {
      "level": 0
    },
    "blower": {
      "modeType": 2,
      "level": 0
    },
    "fan": {
      "on": 1,
      "level": 1
    }
  }
}
```
Sending commands seems also to work: (on the same topic)
```json
{
  "method": "setDevSta",
  "pid": "<redacted>",
  "pcode": 1004,
  "uid": "<redacted>",
  "UTC": 1776598686,
  "data": {
   "light": {
        "on": 1,
        "level": 30
    }
  }
}
```
pid == mac address of the controller
UTC == needs to be dynamic
uid == probably my user id

Things are going right in home assistant: (NOTE this is MQTT based - i would prefer BLE probably, but atleast my data is not sent to spiderfarmer, at least not via mqtt)
<img width="1306" height="853" alt="Image" src="https://github.com/user-attachments/assets/dd8401b6-29bf-4c61-9b83-a8b6b2188038" />
