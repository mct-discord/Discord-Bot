import json
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


class GSpreadsheets:

    def __init__(self, keypath):
        self.keypath = keypath

    def authorize(self):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.keypath, scope)

        self.client = gspread.authorize(
            credentials)  # authenticate with Google

    def add_warning(self, to_warn, reason, given_by):
        self.authorize()

        def next_available_row(worksheet):
            str_list = list(filter(None, worksheet.col_values(1)))
            return str(len(str_list)+1)
        # gspread.Client.open_by_url
        # json credentials you downloaded earlier

        worksheet = self.client.open_by_url(
            url="https://docs.google.com/spreadsheets/d/1pB7nv1Oaf8En7YOLiqiKny9tOTli42Psvpn8-RibBXU/edit?usp=sharing").get_worksheet(0)
        next_row = next_available_row(worksheet)

        # insert on the next available row
        worksheet.update_acell("A{}".format(next_row),
                               str(datetime.datetime.now()))
        worksheet.update_acell("B{}".format(next_row), to_warn.id)
        worksheet.update_acell("C{}".format(next_row), to_warn.name)
        worksheet.update_acell("D{}".format(next_row), reason)
        worksheet.update_acell("E{}".format(next_row), given_by.name)
        worksheet.update_acell("F{}".format(next_row), given_by.id)

    def add_kick(self, to_kick, reason, given_by):
        self.authorize()

        def next_available_row(worksheet):
            str_list = list(filter(None, worksheet.col_values(1)))
            return str(len(str_list)+1)
        # gspread.Client.open_by_url
        # json credentials you downloaded earlier

        worksheet = self.client.open_by_url(
            url="https://docs.google.com/spreadsheets/d/1pB7nv1Oaf8En7YOLiqiKny9tOTli42Psvpn8-RibBXU/edit?usp=sharing").get_worksheet(2)
        next_row = next_available_row(worksheet)

        # insert on the next available row
        worksheet.update_acell("A{}".format(next_row),
                               str(datetime.datetime.now()))
        worksheet.update_acell("B{}".format(next_row), to_kick.id)
        worksheet.update_acell("C{}".format(next_row), to_kick.name)
        worksheet.update_acell("D{}".format(next_row), reason)
        worksheet.update_acell("E{}".format(next_row), given_by.name)
        worksheet.update_acell("F{}".format(next_row), given_by.id)

    def add_ban(self, to_ban, reason, given_by):
        self.authorize()

        def next_available_row(worksheet):
            str_list = list(filter(None, worksheet.col_values(1)))
            return str(len(str_list)+1)
        # gspread.Client.open_by_url
        # json credentials you downloaded earlier

        worksheet = self.client.open_by_url(
            url="https://docs.google.com/spreadsheets/d/1pB7nv1Oaf8En7YOLiqiKny9tOTli42Psvpn8-RibBXU/edit?usp=sharing").get_worksheet(3)
        next_row = next_available_row(worksheet)

        # insert on the next available row
        worksheet.update_acell("A{}".format(next_row),
                               str(datetime.datetime.now()))
        worksheet.update_acell("B{}".format(next_row), to_ban.id)
        worksheet.update_acell("C{}".format(next_row), to_ban.name)
        worksheet.update_acell("D{}".format(next_row), reason)
        worksheet.update_acell("E{}".format(next_row), given_by.name)
        worksheet.update_acell("F{}".format(next_row), given_by.id)

    def add_mute(self, to_mute, reason, given_by, length=None):
        self.authorize()

        def next_available_row(worksheet):
            str_list = list(filter(None, worksheet.col_values(1)))
            return str(len(str_list)+1)
        # gspread.Client.open_by_url
        # json credentials you downloaded earlier

        worksheet = self.client.open_by_url(
            url="https://docs.google.com/spreadsheets/d/1pB7nv1Oaf8En7YOLiqiKny9tOTli42Psvpn8-RibBXU/edit?usp=sharing").get_worksheet(1)
        next_row = next_available_row(worksheet)

        # insert on the next available row
        worksheet.update_acell("A{}".format(next_row),
                               str(datetime.datetime.now()))
        worksheet.update_acell("B{}".format(next_row), to_mute.id)
        worksheet.update_acell("C{}".format(next_row), to_mute.name)
        worksheet.update_acell("D{}".format(next_row), reason)
        if length is not None:
            worksheet.update_acell("E{}".format(next_row), length)
        else:
            worksheet.update_acell("E{}".format(next_row), "Infinite")

        worksheet.update_acell("F{}".format(next_row), given_by.name)
        worksheet.update_acell("G{}".format(next_row), given_by.id)
