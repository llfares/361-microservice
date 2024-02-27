The UI microservice allows users to input a list of ingredients via the CLI and retrieves recipes based on those ingredients.    

A. Requesting Data from the UI Microservice
To request data from the UI microservice, follow the steps below:

Step 1: Run the recipe app and UI.py programs in separate processes.
Step 2: The recipe app will read the ingredients.txt file where the UI microservice will write the ingredients entered by the user.
Step 3: Upon processing the data read from the ingredients.txt file, the recipe app writes recipes meeting the user's criteria to the recipes.txt file.
Step 4: The UI microservice will read the data from the recipes.txt file and print a list of recipes.

Example Call:
An example call: the user enters "flour," "butter," and "sugar" when prompted by the UI microservice, which in turn writes these ingredients to the ingredients.txt file. The recipe app reads the ingredients.txt file, then writes the list of recipes to the recipes.txt file. The UI microservice reads the recipe list from the recipes.txt file and prints it in the CLI.

B.Receiving Data from the UI Microservice
To receive data from the UI microservice, follow the steps below:

Step 1: Prepare the user input data that you want to send to the recipe app. In this case, the input data should be a list of ingredients.
Step 2: Run the UI.py program in a separate process. It will prompt the user to enter the list of ingredients separated by commas. 
Step 3: Wait for the UI microservice to process the input data and write it to the ingredients.txt file.
Step 4: The recipe app reads the data from the ingredients.txt file.

C. UML Sequence Diagram:
![image](https://github.com/llfares/361-microservice/assets/155480234/42504211-c23e-414d-92d7-52caf1ea3fb1)

