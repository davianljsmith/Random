from __future__ import print_function
import boto3
from botocore.exceptions import ClientError
import os
import json
import csv
from time import sleep
import datetime
import dateutil.parser
import sys



# Request the credential report, download and parse the CSV.
def get_credential_report(iam_client):
    resp1 = iam_client.generate_credential_report()
    if resp1['State'] == 'COMPLETE' :
        try: 
            response = iam_client.get_credential_report()
            credential_report_csv = response['Content']
            # print(credential_report_csv)
            reader = csv.DictReader(credential_report_csv.splitlines())
            # print(reader.fieldnames)
            credential_report = []
            for row in reader:
                credential_report.append(row)
            return(credential_report)
        except ClientError as e:
            print("Unknown error getting Report: " + e.message)
    else:
        sleep(2)
        return get_credential_report(iam_client)


def email_user(email, message, account_name):
    global ACTION_SUMMARY # This is what we send to the admins
    if SEND_EMAIL != "true": return # Abort if we're not supposed to send email
    if message == "": return # Don't send an empty message
    client = boto3.client('ses')
    body = EXPLANATION_HEADER + "\n" + message + "\n\n" + EXPLANATION_FOOTER
    def lambda_handler(event, context):
        response = client.send_email(
            Source=FROM_ADDRESS,
            Destination={ 'ToAddresses': [ email ] },
            Message={
                'Subject': { 'Data': email_subject.format(account_name) },
                'Body': { 'Text': { 'Data': body } }
            }
        )
        ACTION_SUMMARY = ACTION_SUMMARY + "\nEmail Sent to {}".format(email)
        return
    
def days_till_expire(last_changed, max_age):
    # Ok - So last_changed can either be a string to parse or already a datetime object.
    # Handle these accordingly
    if type(last_changed) is str:
        last_changed_date=dateutil.parser.parse(last_changed).date()
    elif type(last_changed) is datetime.datetime:
        last_changed_date=last_changed.date()
    else:
        # print("last_changed", last_changed)
        # print(type(last_changed))
        return -99999
    expires = (last_changed_date + datetime.timedelta(max_age)) - datetime.date.today()
    return(expires.days)
