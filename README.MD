
=================================
This application is simple Notes Creation application.

Configuration details for this application
------------------------------------------

To configure this appliction into your local machine you must have installed python and pip package of python.

Once you have installed above requirements then follow these instruction to configure this application.

clone/download this application repository into your local machine.
then navigate to notes_app directory and execute the following commands


```
In notes_app/notes_app directory , execute the command
$ pip install -r requirements.txt
```

this will install all require application dependencies.
As we used the Sqlite database and this database copy already exist in this application so you dont need to do any action with database. 

To start this application just run the following command

    python manage.py runserver

this will start the Django server, you can access the applicaiton on your browser using this url.

	http://localhost:8000/


Following actions should be done:

	
1. Home Page: Goto home page to see the notes page by executing url:
	
	http://localhost:8000/home

2. Create Notes: To create notes click the black button on the top of the page
                  type the notes and click the save button , this will create a note
                  and it is displayed in the left side. 
	
3. View Note: To view the content of a note click on it , it will show the full note.	


		
