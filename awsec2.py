ec2config={
  "awsec2-DA9A": {
    "service_id": "awsec2-DA9A",
    "service_region": "us-east-1",
    "create_new_vpc": False,

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
    "instance_name": "demo-ec2",
    "instance_image": "ami-068c0051b15cdb816",
    "instance_type": "t3.micro", #x86_64 
    "auto_assign_public_ip": True,
    "user_data": "#!/bin/bash\nyum update -y\nyum install -y httpd\nsystemctl start httpd\nsystemctl enable httpd",
    "storage_volumes": [
      {
        "type": "gp3",
        "size": 20,
        "delete_on_termination": True
      }
    ],
    "tags": [
      {
        "key": "Environment",
        "value": "dev"
      },
      {
        "key": "Owner",
        "value": "MadatCloud"
      }
    ]
    
  }
}