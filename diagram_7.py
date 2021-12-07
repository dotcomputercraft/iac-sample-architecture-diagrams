from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.compute import AppEngine, Functions
from diagrams.gcp.database import BigTable
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS

from diagrams.gcp.security import Iam
from diagrams.gcp.compute import Run
from diagrams.gcp.devtools import ContainerRegistry
from diagrams.gcp.devtools import Build
from diagrams.onprem.iac import Terraform
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import React


with Diagram("Trace.io Architecture") as med_diag:

    with Cluster("Development Environment"):
        cb = Build("Cloud Build")
        tf = Terraform()

    with Cluster("Manual deployment"):
        crs=ContainerRegistry("Container Registry")

    with Cluster("Automated deployment"):
        cr=Run("Cloud Run")
        iam=Iam("IAM")

        with Cluster("Container"):
            d=Docker()
            with Cluster("Editor"):
                web=Nginx("Web Server")
                app=React("Editor App")
    
    cb >> crs >> cr >> d
    d >> web >> app
    tf >> cr

med_diag