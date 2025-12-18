lambdaconfig = {
    "awslambda-DA9A": {
        "function_name": "lambdademo",
        "runtime": "python3.14",
        "handler": "lambda_function.lambda_handler",
        "role": "arn:aws:iam::123456789012:role/lambda_basic_execution",

        "file_upload": [
            {
                "url": "https://madatcloud-issues.s3.amazonaws.com/fe384f2f-8e2a-45b7-9d69-7a864775e762/deployment-files/f18659fb6325f840_lambda_function.zip",
                "name": "lambda_function.zip",
                "size": 22470256,
                "type": "application/zip"
            }
        ],

        "memory_size": 2048,
        "size": 512,
        "timeout": 30,
        "architectures": "x86_64",
        "layers": [],
        "environment": [],

        "capacity_provider_name": "my-lambda-provider",

        "lambda_managed_instances": {
            "create_capacity_provider": True
        },

        "vpc_config": {
            "vpc_name": "my_vpc",
            "vpc_cidr": "10.0.0.0/16",
            "igw_required": True,
            "nat_required": False,
            "subnets": [
                {
                    "name": "public_subnet",
                    "cidr": "10.0.1.0/24",
                    "az": "us-east-1a",
                    "public": True,
                    
                },
                {
                    "name": "private_subnet",
                    "cidr": "10.0.2.0/24",
                    "az": "us-east-1b",
                    "private": False,
                }
            ]
        },

        "security_groups": [
            {
                "name": "app_sg",
                "description": "Allow app traffic",
                "ingress": [
                    {
                        "from_port": 80,
                        "to_port": 80,
                        "protocol": "tcp",
                        "cidr": "0.0.0.0/0"
                    }
                ],
                "egress": [
                    {
                        "from_port": 0,
                        "to_port": 0,
                        "protocol": "-1",
                        "cidr": "0.0.0.0/0"
                    }
                ]
            }
        ],

        "tags": [
            {
                "key": "testing",
                "value": "live"
            }
        ],

        "s3_bucket": "madatcloudinfra",
        "s3_key": "my_deployment_package.zip",
        "s3_file_path": "https://madatcloud-issues.s3.amazonaws.com/fe384f2f-8e2a-45b7-9d69-7a864775e762/deployment-files/f18659fb6325f840_lambda_function.zip"
    }
}
