## Content Download Script

### Overview

This script downloads, aggregates, and JSON-ifies content stored in a Google spreadsheet.

### Running the Script

#### Dependencies:

- Python 2.7
- gspread library (`pip install gspread`)
- oauth2client (`pip install oauth2client`)


#### Setup Google API Credentials 

1. Eanble Goolge SpreadSheet API and Google Drive API
2. Make sure the credentials are for a service account. 
3. Your credentials should be saved as `keyfil.json`. The file should look like this

```
{
   "type":"",
   "project_id":"",
   "private_key_id":"",
   "private_key":"",
   "client_email":"",
   "client_id":"",
   "auth_uri":"",
   "token_uri":"",
   "client_x509_cert_url":""
}
```

4. Share the "client_email" with your spreadsheet to access the data via the python script


#### Usage example:

The example uses the credentials in `keyfile.json` and writes JSON from the spreadsheet to `temp_content.json`. The example also uses [this](https://docs.google.com/spreadsheets/d/1h1nuh9a3iZ8JetcZ_lyVCUsvsx23ZCK-x2xb7oSSk2I/edit?usp=sharing) spreadsheet as an example. 

To run the script: 

1. Open terminal
2. CD into the folder 
2. Run `python main.py keyfile.json temp_content.json`


### Helpful Links

* [Google Sheets API Documentation](https://developers.google.com/sheets/api)

### License

* [google spreadsheet cms](https://github.com/nicoleyimessier/google_spreadsheet_cms) is distributed under the [MIT license](License.md).