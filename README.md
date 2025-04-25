# Data-Analytics-And-Visualization

## How to run the project
	- Pull the code from the github repository from the "development" branch.
	- check for the available environment in your machine by running the below code
		- "jupyter kernelspec list"
	- If an environment with the name "conda-base-py" is not found, you need to create and add conda env as a Jupyter kernel
	- The development was done on the environment called "conda-base-py". If you don't have an environment with this name, please create one and activate it. 
		- create environment -> "conda create --name conda-base-py python=3.9"
		- activate environment -> "conda activate conda-base-py"
		- add the conda env to jupyter - > "python -m ipykernel install --user --name conda-base-py --display-name "conda-base-py"

	- run the following command in anaconda terminal to install the required packages
		"pip install jupyter python-dotenv py2neo pandas numpy seaborn matplotlib plotly dash papermill mysql psycopg2 pathlib dotenv neo4j pymongo kaleido dagster dagster-webserver openpyxl"
		
	- Make sure all the database configurations are updated according to your database connection by updating the configuration values in the ".env" file found in the root directory.
	
	- Next run the dagster pipeline with the following command in the Anaconda terminal from the root directory of the project.
		- dagster dev -f pipeline.py
	- After dagster successfully launches, you need to materialize all the assets and wait for them to complete their run successfully.
	- When all the assets in the pipeline are successfully executed then we can start the Dashboard
		- navigate to Dashboard/Dashboard.ipynb and run the jupyter notebook file completely
		- the dashboard will be opened in a web browser tab.
		
### Members contribution
"Dataset 01 related implementation" - Pathmanathan Gawtham
"Dataset 02 related implementation" - Aniket Vivekanand Rane
"Dataset 03 related implementation" - Rohit Pramod Pawar
