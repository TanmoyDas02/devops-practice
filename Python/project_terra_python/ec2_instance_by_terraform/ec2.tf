# key pair (login)

resource "aws_key_pair" "my_key" {
    key_name = "terra-key-ec2"
    public_key = file("terra-key-ec2.pub")
}

# VPC & Security Group

resource "aws_default_vpc" "default" {
  
}

resource "aws_security_group" "my_security_group" {
    name = "automate-sg"
    description = "this will add a TF generated security group"
    vpc_id = aws_default_vpc.default.id   # interpolation

    # inbound rules
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "allow SSH from anywhere"
    }
    
    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "allow HTTP from anywhere"
    }

    # outbound rules
    egress{
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
        description = "allow all outbound traffic"
    }

    tags = {
        Name = "automate-sg"
    }
}

# EC2 Instance

resource "aws_instance" "my_instance" {
    # count = 3  # meta argument
    for_each = tomap({
        TWS-automate-1 = "t2.micro",
        TWS-automate-2 = "t2.micro"
    })

    depends_on = [ aws_security_group.my_security_group, aws_key_pair.my_key ]

    key_name = aws_key_pair.my_key.key_name
    security_groups = [aws_security_group.my_security_group.name]
    instance_type = each.value
    ami = var.ec2_ami_id
    user_data = file("install_nginx.sh")

    root_block_device {
        volume_size = var.env == "prd" ? 20 : var.ec2_default_root_storage_size
        volume_type = "gp3"
    }

    tags = {
        Name = each.key
    }
}

# resource "aws_instance" "my_new_instance" {
#     ami = "unknown"
#     instance_type = "unknown"

# }