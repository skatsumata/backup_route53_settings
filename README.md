# Overview

route53の全てのHostedZoneとレコードセットの設定をJson形式で取得するPythonスクリプトです。

This is a Python script that gets all HostedZone and Recordset settings of route53 in Json format.

**Hosted zones**  
![](https://i.gyazo.com/ffcb87fda027a861ee258cd0ad252465.png)

**Record Set**  
![](https://i.gyazo.com/6de6b19f9f3fb4e601101a52e51f1843.png)

# environment

| # | version |
|:--|:--|
| OS   | CentOS 7.5.1804  |
| python  | 2.7.5  |
| boto3  | 1.9.33  |

# usage

スクリプトを実行すると後述したようにコンソール出力されるのでリダイレクトしてファイルに格納する想定です。

```bash
$ python backup_route53_settings.py > route53_settings.txt
```

## output sample

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

# boto3 documents

- [list_hosted_zones](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_hosted_zones)
- [list_resource_record_sets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_resource_record_sets)
