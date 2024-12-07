# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]


# def main():
#   """Shows basic usage of the Drive v3 API.
#   Prints the names and ids of the first 10 files the user has access to.
#   """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())

#   try:
#     service = build("drive", "v3", credentials=creds)

#     # Call the Drive v3 API
#     results = (
#         service.files()
#         .list(pageSize=10, fields="nextPageToken, files(id, name)")
#         .execute()
#     )
#     items = results.get("files", [])

#     if not items:
#       print("No files found.")
#       return
#     print("Files:")
#     for item in items:
#       print(f"{item['name']} ({item['id']})")
#   except HttpError as error:
#     # TODO(developer) - Handle errors from drive API.
#     print(f"An error occurred: {error}")


# if __name__ == "__main__":
#   main()

# import os.path
# from datetime import datetime
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from googleapiclient import discovery

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


# # ID таблицы и имя листа
# SPREADSHEET_ID = "14SinnbsApKptQCVEgQHmwf4TBEUCn_N6WJL7cWepLkQ"  # Замените на ID вашей таблицы
# SHEET_NAME = "test"  # Замените на имя вашего листа


# def main():
#     creds = None
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 "credentials.json", SCOPES
#             )
#             creds = flow.run_local_server(port=0)
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())

#     try:
#         # Подключение к API Google Sheets
#         service = build("sheets", "v4", credentials=creds)
        
#         # Данные сотрудников (пример)
#         employees_data = [
#             {"name": "Сотрудник 1", "status": "пришел", "arrival": "09:00", "departure": "18:00"},
#             {"name": "Сотрудник 2", "status": "не пришел", "arrival": "", "departure": ""},
#             {"name": "Сотрудник 3", "status": "отпросился", "arrival": "10:00", "departure": "15:00"},
#         ]
        
#         # Текущая дата
#         today_date = datetime.today().strftime('%Y-%m-%d')

#         # Формирование данных для записи
#         values = [["Дата", "Сотрудник", "Пришел", "Ушел", "Статус"]]
#         for employee in employees_data:
#             arrival = employee["arrival"] if employee["arrival"] else "не пришел"
#             departure = employee["departure"] if employee["departure"] else ""
#             status = employee["status"]
#             values.append([today_date, employee["name"], arrival, departure, status])

#         # Запись данных в Google Sheets
#         range_ = f"{SHEET_NAME}!A1:E{len(values)}"
#         body = {
#             "values": values
#         }
#         service.spreadsheets().values().update(
#             spreadsheetId=SPREADSHEET_ID, range=range_, valueInputOption="RAW", body=body
#         ).execute()

#         # Применение цветового форматирования
#         requests = []
#         for i, employee in enumerate(employees_data, start=2):  # Начинаем со второй строки
#             color = {
#                 "пришел": {"red": 0.6, "green": 1.0, "blue": 0.6},
#                 "не пришел": {"red": 1.0, "green": 0.6, "blue": 0.6},
#                 "отпросился": {"red": 0.6, "green": 0.6, "blue": 1.0}
#             }.get(employee["status"], {"red": 1.0, "green": 1.0, "blue": 1.0})
            
#             requests.append({
#                 "repeatCell": {
#                     "range": {
#                         "sheetId": 0,  # Замените на ID вашего листа
#                         "startRowIndex": i - 1,
#                         "endRowIndex": i,
#                         "startColumnIndex": 4,
#                         "endColumnIndex": 5,
#                     },
#                     "cell": {
#                         "userEnteredFormat": {
#                             "backgroundColor": color
#                         }
#                     },
#                     "fields": "userEnteredFormat.backgroundColor"
#                 }
#             })
        
#         # Применение изменений через batchUpdate
#         service.spreadsheets().batchUpdate(
#             spreadsheetId=SPREADSHEET_ID,
#             body={"requests": requests}
#         ).execute()

#         print("Таблица успешно обновлена.")

#     except HttpError as error:
#         print(f"Произошла ошибка: {error}")


# if __name__ == "__main__":
#     main()


from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os

credentials_file = "credentials.json"
token_file = "token.json"

if os.path.exists(token_file):
    creds = Credentials.from_authorized_user_file(token_file)
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_file, scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    creds = flow.run_local_server(port=0)

    with open(token_file, "w") as token:
        token.write(creds.to_json())

spreadsheet_id = '14SinnbsApKptQCVEgQHmwf4TBEUCn_N6WJL7cWepLkQ'

service = build('sheets', 'v4', credentials=creds)

sheet_name = "test"

spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

sheet_exists = False
for sheet in spreadsheet['sheets']:
    if sheet['properties']['title'] == sheet_name:
        sheet_exists = True
        break

if not sheet_exists:
    requests = [{
        'addSheet': {
            'properties': {
                'title': sheet_name
            }
        }
    }]
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={'requests': requests}
    ).execute()

header_range = f"{sheet_name}!A1:E1"
employee_range = f"{sheet_name}!A2:A4"

headers = [["Сотрудник", "Дата", "Пришел", "Ушел", "Статус"]]
employees = [["Сотрудник 1"], ["Сотрудник 2"], ["Сотрудник 3"]]

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=header_range,
    valueInputOption="RAW",
    body={"values": headers}
).execute()

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=employee_range,
    valueInputOption="RAW",
    body={"values": employees}
).execute()

print("Данные успешно добавлены.")
