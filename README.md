##Mini-Wiki
A dynamic wiki-like app for displaying markdown files. 

####Requirements & Guides
--Requires [Flask](http://flask.pocoo.org/)     
--[Here](http://daringfireball.net/projects/markdown/syntax#link) is a great guide to editing markdown files

####Logging In
The ```settings.py``` file contains a list of people who are allowed to access Bootcamp:    
``` 
	USERS = [
				'example@provplan.org',
			]   
```
2. The names in the list will be the username to login with.
3. There is one password for everyone. This will also be saved in ```settings.py```.
4. Set a secret key.

####Functionality
1. A user can choose to be any one of four roles: Analyst, Programmer, Intern or Communications.
2. Each role has its own directory containing files and subdirectories associated to that role.
3. The application will then dsiplay a list of menu items based on the files and subdirectories in that roles directory.
4. When a menu item is clicked the application will convert markdown to HTML and display the content to the user through an ajax request.

####Folder structure
```			
			/templates/
			/static/
			/content/
					/analyst/
					/programmer/
					/communications/
					/intern/
					/for_all/
					/pdfs/
					/images/
					/role_greetings/

```
1. Each role has their own folder located in the ```/content/``` folder that stores all files related to that role.
2. Any markdown file that is placed in a role specific folder will be displayed as a menu item on their page.
3. Any markdown file placed in the ```/for_all/``` folder will be displayed on all menus. This is content each role will need access to. 
	*	Example: ```Helpful_Links.md``` contains links to Toggl, Postini, HipChat etc... These are things we all use every day. 
4. The ```/role_greetings/``` folder contains a greeting message to be displayed when a user selects their role.

####Naming markdown files    
1. Don't use hyphens.  
2. The file names ARE case sesitive.  
3. Use an underscore to add spaces between words.    
	*	Example: the file ```Data_Cleaning.md``` will be displayed as ```Data Cleaning``` on the menu tab.

####Adding Images and PDFs
1. Place the pdf or image in their folders: 
	*	The path the images folder is: ```/content/images/```
	*	The path the pdf folder is: ```/content/pdfs/```   
2. To include an image or a pdf you must include the syntax in the markdown file.   
3. Example pdf syntax: ```[SPSS Syntax Guide](/content/pdfs/SPSSSyntaxReferenceGuide.pdf)```
	*	this will create a link to the pdf. 
	*	it depends on the browser whether it is downloaded or displayed in another tab.   
4. Example image syntax: ```![Text displayed on hover](/content/images/img.jpg)```




  





