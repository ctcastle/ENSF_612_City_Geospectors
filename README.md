First it is highly recommended to setup a python virtual environment to isolate the requirements of this project from the rest of your system. 

Project Setup w/ virtual environment: 
1. Clone project to your folder structure 
2. Navigate to the Github project folder 
3. Use: python -m venv venv (It is recommended to use "venv" as your virtual environment name but you can make it whatever you'd like)
4. Next you must activate the environment:
5. If on Windows enter this into powershell terminal in project folder: .\venv\Scripts\activate
6. If on Mac/Unix enter this into terminal in project folder: source venv/bin/activate
7. Run: pip install -r requirements.txt
8. (If you want to add a dependency to the project, this can be done by running pip install "your dependency" followed by pip freeze > requirements.txt to install and then update the requirements for everyone else) 
9. Finally, if you chose a different name for your virtual environment other than "venv", add your virtual environment name into .gitignore file

Register venv as a Jupyter Kernel with VS code (if you are using something else this guide will be less helpful, you may need to look it up online): 
1. While your venv is activated run: python -m ipykernel install --user --name=venv --display-name="City Geospectors Environment" (Display name can be whatever)
2. You may need to restart vs code but afterwards you should be able to select the kernel you want to use by selecting the kernel in the top right corner of your ipynb file
3. Select City Geospectors Environment 

After this you should be ready to go. Official project work will be done in the City_Geospectors.ipynb file but feel free to make additional notebooks and py files as necessary if you want to experiment with anything. As a general request, lets keep the main notebook free of errors and warnings, this means if you have an unfinished section of code that you want to save either keep it in a separate notebook or on a separate branch. 
