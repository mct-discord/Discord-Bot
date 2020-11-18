import json
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

class GSpreadsheets:

    def __init__(self, keypath, spreadsheetId):
        self.keypath = keypath
        self.spreadsheetId = spreadsheetId

    def authorize(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.keypath, scope)


        self.service = build('sheets', 'v4', credentials=credentials)

    def add_warning(self, to_warn, reason, given_by):
        self.authorize()
        
        list = [[str(datetime.datetime.now()), str(to_warn.id), to_warn.name,reason,given_by.name,str(given_by.id)]]
        resource = {
            "majorDimension": "ROWS",
            "values": list
        }
        range = "Warnings!A:F"
        self.service.spreadsheets().values().append(
        spreadsheetId=self.spreadsheetId,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
        ).execute()

    def add_kick(self, to_kick, reason, given_by):
        self.authorize()
        
        list = [[str(datetime.datetime.now()), str(to_kick.id), to_kick.name,reason,given_by.name,str(given_by.id)]]
        resource = {
            "majorDimension": "ROWS",
            "values": list
        }
        range = "Kicks!A:F"
        self.service.spreadsheets().values().append(
        spreadsheetId=self.spreadsheetId,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
        ).execute()

    def add_ban(self, to_ban, reason, given_by):
        self.authorize()
        
        list = [[str(datetime.datetime.now()), str(to_ban.id), to_ban.name,reason,given_by.name,str(given_by.id)]]
        resource = {
            "majorDimension": "ROWS",
            "values": list
        }
        range = "Bans!A:F"
        self.service.spreadsheets().values().append(
        spreadsheetId=self.spreadsheetId,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
        ).execute()

    def add_mute(self, to_mute, reason, given_by, length=None):
        self.authorize()
        
        if length is None:
            length = 'Infinite'
        
        list = [[str(datetime.datetime.now()), str(to_mute.id), to_mute.name,reason,length,given_by.name,str(given_by.id)]]
        resource = {
            "majorDimension": "ROWS",
            "values": list
        }
        range = "Mutes!A:G"
        self.service.spreadsheets().values().append(
        spreadsheetId=self.spreadsheetId,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
        ).execute()

    def add_message(self, to_message, reason, given_by):
        self.authorize()
        
        list = [[str(datetime.datetime.now()), str(to_message.id), to_message.name,reason,given_by.name,str(given_by.id)]]
        resource = {
            "majorDimension": "ROWS",
            "values": list
        }
        range = "MessageLog!A:F"
        self.service.spreadsheets().values().append(
        spreadsheetId=self.spreadsheetId,
        range=range,
        body=resource,
        valueInputOption="USER_ENTERED"
        ).execute()