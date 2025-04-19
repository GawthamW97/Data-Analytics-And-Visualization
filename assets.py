from dagster import asset, Definitions, AssetExecutionContext
import papermill as pm
from pathlib import Path

OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

ROOT = Path(__file__).parent.parent

@asset
def load_data_to_neo4j_asset(context: AssetExecutionContext):
    """Read the data from excel file and upload it to neo4j DB"""
    
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_01/loading_data_neo4js.ipynb"
    output_path = OUTPUT / "output_loading_data_neo4js.ipynb"

    context.log.info(f"Executing {input_path}")

    try:
        pm.execute_notebook(
            input_path = input_path,
            output_path = str (output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
        context.log.info("Data is uploaded to neo4j DB successfully!")
        return str(output_path)
    except Exception as e:
        context.log.error(f"Error - {str(e)}")
        with open('app.log', 'a') as f:
            f.write(f"{input_path}\n") 
        raise


@asset
def visualize_data_from_neo4j(context: AssetExecutionContext, load_data_to_neo4j_asset: str):
    """ Run the notebook to visualize the dataset from neo4j"""
    context.log.info(f"load_data_to_neo4j output path: {load_data_to_neo4j_asset}")
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_01/loading_data_neo4js.ipynb"
    output_path = OUTPUT / "output_visualize_data_neo4j.ipynb"

    pm.execute_notebook(
            input_path = str(input_path),
            output_path = str(output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
    return str(output_path)

@asset
def load_data_to_mongoDB01_asset(context: AssetExecutionContext):
    """Read the data from excel file and upload it to Mongo DB"""
    
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_02/MongoDB (No-SQL).ipynb"
    output_path = OUTPUT / "output_MongoDB (No-SQL).ipynb"

    context.log.info(f"Executing {input_path}")

    try:
        pm.execute_notebook(
            input_path = input_path,
            output_path = str (output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
        context.log.info("Data is uploaded to Mongo DB successfully!")
        return str(output_path)
    except Exception as e:
        context.log.error(f"Error - {str(e)}")
        with open('app.log', 'a') as f:
            f.write(f"{input_path}\n") 
        raise

@asset
def visualize_data_from_mongoDB(context: AssetExecutionContext, load_data_to_mongoDB01_asset: str):
    """ Run the notebook to visualize the dataset from MongoDB"""
    context.log.info(f"load_data_to_mongoDB_asset output path: {load_data_to_mongoDB01_asset}")
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_02/Visualize data.ipynb"
    output_path = OUTPUT / "output_Visualize data.ipynb"

    pm.execute_notebook(
            input_path = str(input_path),
            output_path = str(output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
    return str(output_path)

@asset
def load_data_to_postgreSQL_asset(context: AssetExecutionContext):
    """Read the data from excel file and upload it to postgreSQL DB"""
    
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_01/loading_data_postgreSQL.ipynb"
    output_path = OUTPUT / "output_loading_data_postgreSQL.ipynb"

    context.log.info(f"Executing {input_path}")

    try:
        pm.execute_notebook(
            input_path = input_path,
            output_path = str (output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
        context.log.info("Data is uploaded to postgreSQL DB successfully!")
        return str(output_path)
    except Exception as e:
        context.log.error(f"Error - {str(e)}")
        with open('app.log', 'a') as f:
            f.write(f"{input_path}\n") 
        raise

@asset
def load_data_to_mySQL_asset(context: AssetExecutionContext):
    """Read the data from excel file and upload it to MySQL DB"""
    
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_02/MySQL.ipynb"
    output_path = OUTPUT / "output_MySQL.ipynb"

    context.log.info(f"Executing {input_path}")

    try:
        pm.execute_notebook(
            input_path = input_path,
            output_path = str (output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
        context.log.info("Data is uploaded to MySQL DB successfully!")
        return str(output_path)
    except Exception as e:
        context.log.error(f"Error - {str(e)}")
        with open('app.log', 'a') as f:
            f.write(f"{input_path}\n") 
        raise

@asset
def load_data_to_mongoDB02_asset(context: AssetExecutionContext):
    """Read the data from excel file and upload it to Mongo DB"""
    
    input_path = ROOT/"Data-Analytics-And-Visualization/notebooks/dataset_03/load_data_to_mongoDB.ipynb"
    output_path = OUTPUT / "output_load_data_to_mongoDB.ipynb"

    context.log.info(f"Executing {input_path}")

    try:
        pm.execute_notebook(
            input_path = input_path,
            output_path = str (output_path),
            parameters = {},
            log_output=True,
            pregress_bar=True
        )
        context.log.info("Data is uploaded to Mongo DB successfully!")
        return str(output_path)
    except Exception as e:
        context.log.error(f"Error - {str(e)}")
        with open('app.log', 'a') as f:
            f.write(f"{input_path}\n") 
        raise

defs = Definitions(
        assets=[load_data_to_neo4j_asset,visualize_data_from_neo4j,
                load_data_to_mongoDB01_asset,visualize_data_from_mongoDB,
                load_data_to_postgreSQL_asset,load_data_to_mySQL_asset,load_data_to_mongoDB02_asset]
    )
























    
