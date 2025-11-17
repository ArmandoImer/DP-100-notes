#To connect to the workspace
#Assuming you have given the needed values to subscription_id, resource_group, workspace
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)

# After defining the authentication, you need to call MLClient for the environment to connect to the workspace.
# You'll call MLClient anytime you want to create or update an asset or resource in the workspace.
# For example, you'll connect to the workspace when you create a new job to train a model:

from azure.ai.ml import command

# configure job
job = command(
    code="./src",
    command="python train.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="aml-cluster",
    experiment_name="train-model"
)

# connect to workspace and submit job
returned_job = ml_client.create_or_update(job)
