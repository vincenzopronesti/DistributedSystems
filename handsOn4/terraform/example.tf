terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-032e334ee4b9d084d"   # AMI with photogallery
  #ami           = "ami-04d29b6f966df1537"   # base AMI
  instance_type = "t2.micro"
  vpc_security_group_ids = ["sg-0c1bec6fa237ca68d"] # HTTP, SSH
  subnet_id              = "subnet-0eba0d496db693faf"
  tags = {
    Name = "terraform-example"
  }
}

