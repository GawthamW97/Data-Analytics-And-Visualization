# Data-Analytics-And-Visualization

## Command to install the packages
pip install jupyter python-dotenv py2neo pandas numpy seaborn matplotlib plotly dash papermill mysql psycopg2 pathlib dotenv neo4j pymongo kaleido dagster

## How to run the project
	- Pull the code from the github repository from the "development" branch.
	- The development was done on the environment called "conda-base-py". If you don't have an environment with this name, please create one and activate it. 
		- create environment -> "conda create --name conda-base-py python=3.9"
		- activate environment -> "conda activate conda-base-py"
	- Then install the packages using the command above in the Anaconda terminal.
	- Make sure all the database configurations are updated according to your system by updating the configuration values in the ".env" file found in the root directory.
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
