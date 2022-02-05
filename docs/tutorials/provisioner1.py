import terrascript
import terrascript.provider.aws
import terrascript.resource.aws

config = terrascript.Terrascript()

# AWS provider
config += terrascript.provider.aws.aws(region="us-east-1")

# Provisioners
create = terrascript.Provisioner("local-exec", command="echo 'Create'")
destroy = terrascript.Provisioner(
    "local-exec",
    when="destroy",
    command="echo 'Destroy'",
)

# Resource with two provisioners
config += terrascript.resource.aws.aws_instance(
    "instance1",
    instance_type="t2.micro",
    ami="ami-4bf3d731",
    provisioner=[
        create,
        destroy,
    ],
)
