# backup_route53_settings
backing up aws route53 settings( all HostedZones and  RecordSets )

# 概要

route53の全てのHostedZoneとレコードセットの設定をJson形式で取得するPythonスクリプトです。

**Hosted zones**
![](https://i.gyazo.com/ffcb87fda027a861ee258cd0ad252465.png)
**Record Set**
![](https://i.gyazo.com/6de6b19f9f3fb4e601101a52e51f1843.png)

# 確認した環境

| 項目 | バージョン |
|:--|:--|
| OS   | CentOS 7.5.1804  |
| python  | 2.7.5  |
| boto3  | 1.9.33  |

# 使い方

スクリプトを実行すると後述したようにコンソール出力されるのでリダイレクトしてファイルに格納する想定です。

```bash
$ python backup_route53_settings.py > route53_settings.txt
```

## コンソール出力例

```bash
"hostedZones": [
{
    "Id": "/hostedzone/xxxxxxxx"
    "Name": "xxxxx.com.",
    "Config": {
        "Comment": "\u4f1a\u793e\u30db\u30fc\u30e0\u30da\u30fc\u30b8",
        "PrivateZone": false
    },
    "CallerReference": "D00D4DCE-876F-CEBF-87C3-B698F213C668",
    "ResourceRecordSetCount": 15,
    "recordSets": [
        {
            "ResourceRecords": [
                {
                    "Value": "158.199.141.166"
                }
            ],
            "Type": "A",
            "Name": "nyango.com.",
            "TTL": 300
        },
        { ... }
     ]
},{
    ... 省略 ...
}

```

# スクリプト

```python:backup_route53_settings.py
import json
import boto3
from boto3.session import Session

profile = '<your profile name>'
session = Session(profile_name=profile)
route53Client = session.client('route53')

def convertToJson(dictSource):
    return json.dumps(dictSource, indent=4, separators=(',', ': '))

def listHostedZones():
    result = []
    response = route53Client.list_hosted_zones()
    for hostedZone in response["HostedZones"]:
        result.append(hostedZone)
    return result

def printInfo(hostedZone,recordSets):
    hostedZone["recordSets"] = recordSets
    print('{},'.format(convertToJson(hostedZone)))

def main():
    hostedZones = listHostedZones()
    if( not hostedZones ):
        print("not found hosted zone.")
        exit()
    print('"hostedZones": [')
    for hostedZone in hostedZones:
        response = route53Client.list_resource_record_sets(
            HostedZoneId=hostedZone["Id"]
        )
        recordSets = response["ResourceRecordSets"]
        printInfo(hostedZone, recordSets)
    print(']')

if __name__ == '__main__':
    main()
```

# boto3 APIドキュメント

- [list_hosted_zones](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_hosted_zones)
- [list_resource_record_sets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_resource_record_sets)
