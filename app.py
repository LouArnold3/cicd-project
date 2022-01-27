#!/usr/bin/env python3
import aws_cdk as cdk
from cicd_project.cicd_project_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(account="465444432665", region="us-east-1")
)

app.synth()