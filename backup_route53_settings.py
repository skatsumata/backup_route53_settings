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
