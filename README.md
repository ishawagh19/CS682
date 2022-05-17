# CS682
Connecting to google spreadsheets using python
Reference link:-  https://erikrood.com/Posts/py_gsheets.html
(1)	Google Drive API, credentials
Head over to Google sheets and create a file called “gps”. Add some dummy columns which could be programmatically accessed later when required.

Further, we need to create a service account and OAuth2 credentials from the Google API console. Follow the steps below to authorize the API and take hold of the credentials.
1.	Head over to the Google API console.
2.	Create a new project by selecting MyProject ->+button.
3.	Search for a ‘Google API drive’ and enable it.
4.	Move on to ‘Credentials’(side bar) and click on ‘Create Credentials’ -> ‘Service Account Key’.

 
 ![image](https://user-images.githubusercontent.com/81271164/168862278-bd49931b-23b7-4d5a-90c7-5d8864b899ea.png)

 

5.	Select Compute Engine service, JSON, click create
6.	Open up the JSON file , share your spreadsheet with the XXX-compute@developer.gservice.com email listed.
7.	Save the JSON file wherever you are hosting the project because it will be needed to load in through python later.



(2)	Connecting Python to Google Sheets:
Install pygsheets (Refer link :- https://github.com/nithinmurali/pygsheets )  for more information about installing pygsheets . This library will allow to practically read/write to the sheet through Python. Once that is installed you are all set.

(3)	Done-Check the sheet to see if the data is uploaded.
 
![image](https://user-images.githubusercontent.com/81271164/168862560-448feab2-e954-4089-ba72-de35931e5b08.png)
