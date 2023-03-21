After cloning the repository, follow these steps to run the project:

- Open the terminal in the root directory of the cloned repository and run the following command to install all the dependencies: "pip install -r requirements.txt"

- Download and install wkhtmltopdf from the official website: https://wkhtmltopdf.org/downloads.html

- Once you have installed wkhtmltopdf, you need to add its path to your system's environment variable PATH so that it can be found by your Django application.

- To do this on a Windows machine, search for "Environment Variables" in the Windows search bar and click on "Edit the system environment variables".

- In the System Properties window that opens, click on the "Environment Variables" button.

- In the "System Variables" section, scroll down to find the "Path" variable and click on "Edit".

- Click "New" and add the path to the directory where wkhtmltopdf is installed. For example, if wkhtmltopdf is installed in C:\Program Files\wkhtmltopdf\bin, then you would add that path.

- Save your changes and restart your command prompt or terminal to make sure the changes are recognized.

- Check the version by running the command "wkhtmltopdf --version".

- Create migrations by running the following command in the terminal (also in the root directory): "python manage.py makemigrations" and "python manage.py migrate".

- Finally, run the server by running the following command in the terminal (also in the root directory): "python manage.py runserver".