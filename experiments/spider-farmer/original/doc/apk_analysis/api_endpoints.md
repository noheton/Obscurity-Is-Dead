# REST API Endpoints

Base URL: `https://api.spider-farmer.com/`

All paths extracted verbatim from `libapp.so`. The app uses the `/api/ios/` prefix
for all device/account endpoints (identical for Android — the naming is legacy).

---

## Authentication

| Method | Path | Notes |
|--------|------|-------|
| POST | `api/ios/ulogin/mailLogin/v1` | Email + password login |
| POST | `api/ios/ulogin/mailRegister/v1` | New account registration |
| POST | `api/ios/ulogin/forgotPassword/v1` | Password reset flow |
| POST | `api/ios/ulogin/updatePassword/v1` | Change password |
| POST | `api/ios/ulogin/getEmailCode/v1` | Send email verification code |
| GET  | `api/ios/ulogin/getBelongingUrlInfo/v1` | Resolve account's regional server |
| POST | `api/ios/tlogin/unionLogin/v1` | Third-party / OAuth login |
| POST | `api/android/cq/commitClientQuestion/v1` | Submit user feedback |

---

## Account / Profile

| Method | Path |
|--------|------|
| POST | `api/ios/mine/editNickName/v1` |
| POST | `api/ios/mine/editHeadImage/v1` |
| POST | `api/ios/mine/editTHUnits/v1` — switch °C / °F |
| POST | `api/ios/mine/deleteAccount/v1` |

---

## Device Management

| Method | Path | Notes |
|--------|------|-------|
| GET  | `api/ios/udm/getDeviceList/v1` | List all paired devices |
| POST | `api/ios/udm/addDevice/v1` | Pair a new device |
| POST | `api/ios/udm/editDevice/v1` | Rename device |
| POST | `api/ios/udm/deleteDevice/v1` | Unpair device |
| GET  | `api/ios/udm/getUserRooms/v1` | List rooms |
| POST | `api/ios/udm/addUserRooms/v1` | Create room |
| POST | `api/ios/udm/deleteOrEditUserRooms/v1` | Rename / delete room |
| GET  | `api/ios/udm/getMzSmartCustomList/v1` | Custom outlet names |
| POST | `api/ios/udm/addMzSmartCustomInfo/v1` | Add custom outlet name |
| POST | `api/ios/udm/delMzSmartCustomDetails/v1` | Delete custom outlet name |
| POST | `api/ios/udm/delAllMzSmartCustom/v1` | Delete all custom outlet names |
| GET  | `api/ios/udm/getSocketCustomizeName/v1` | Get socket custom name |
| POST | `api/ios/udm/setSocketCustomizeName/v1` | Set socket custom name |

---

## Device Upgrade / Firmware

| Method | Path |
|--------|------|
| GET | `api/ios/dua/getDeviceUpInfo/v1` — check for firmware update |
| GET | `api/ios/dua/getUpRjDevice/v1` — get sub-device update info |
| GET | `api/app/version` — check app version |

---

## Sensor / Environmental Data

| Method | Path | Notes |
|--------|------|-------|
| GET | `api/ios/dr/getDeviceTHPData/v1` | Temp/Humidity/PPFD history |
| GET | `api/ios/dr/getDeviceTHPData_Industry/v1` | Industry version |
| GET | `api/ios/dr/getDeviceTHPAvgData_Industry/v1` | Averaged industry data |
| GET | `api/ios/dr/getDevicePowerData/v1` | Power consumption history |
| GET | `api/ios/dSensor/getSensorInfo_Industry/v1` | Industry sensor info |
| POST | `api/ios/dSensor/opSensorInfo_Industry/v1` | Configure industry sensor |

---

## Alarm Logs

| Method | Path |
|--------|------|
| GET | `api/ios/alarmLog/getAlarmLogList/v1` |
| GET | `api/ios/alarmLog/getAlarmLogList_Industry/v1` |
| GET | `api/ios/alarmLog/getUserDevicesForAlaram/v1` |
| GET | `api/ios/alarmLog/getAlarmCode/v1` |

---

## Operation / Run Logs

| Method | Path |
|--------|------|
| GET | `api/ios/runLog/queryDeviceRunLogList/v1` |
| GET | `api/ios/dOperate/getDeviceOperateRecordList_Industry/v1` |

---

## Grow Plans / Plant Templates

| Method | Path | Notes |
|--------|------|-------|
| GET  | `api/ios/userPlanting/getTemplateList/v1` | User's saved templates |
| GET  | `api/ios/userPlanting/getTemplateInfo/v1` | Single template detail |
| POST | `api/ios/userPlanting/addOrEditTemplate/v1` | Create or update template |
| POST | `api/ios/userPlanting/delTemplate/v1` | Delete template |
| POST | `api/ios/userPlanting/copyTemplate/v1` | Copy own template |
| POST | `api/ios/userPlanting/copySysTemplate/v1` | Copy system template |
| GET  | `api/ios/psd/getPlantSysTemList/v1` | System (built-in) templates |

---

## Products / Light Models

| Method | Path |
|--------|------|
| GET | `api/ios/product/getProductModel/v1` |
| GET | `api/ios/product/getProductImg/v1` |
| GET | `api/ios/lightModel/getLightModelList/v1` |
| GET | `api/ios/air/queryAirProductList/v1` |
| GET | `api/ios/air/queryAirProductNameList/v1` |

---

## Utilities

| Method | Path |
|--------|------|
| GET  | `api/ios/dict/getTimeZone/v1` — timezone list (also bundled locally as `sf_timezone.json`) |
| POST | `api/common/upload/image/v1` — upload profile image |

---

## Data Export

| Method | Path |
|--------|------|
| POST | `api/ios/export/getHistroyDataToEmail/v1` |
| POST | `api/ios/export/getHistroyDataToEmailCosumerSoil/v1` |
| POST | `api/ios/export/getHistroyDataToEmail_Industry/v1` |
| POST | `api/ios/export/getHistroyDataToEmail_AvgIndustry/v1` |
