terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    # Configure your state backend here
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      Project     = "agentic-trader"
      ManagedBy   = "terraform"
    }
  }
}

# VPC and networking
module "vpc" {
  source = "./modules/vpc"

  environment  = var.environment
  vpc_cidr     = var.vpc_cidr
  cluster_name = local.cluster_name
}

# EKS cluster
module "eks" {
  source = "./modules/eks"

  cluster_name    = local.cluster_name
  environment     = var.environment
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.private_subnet_ids
  instance_types = var.eks_instance_types
}

# RDS database
module "rds" {
  source = "./modules/rds"

  environment     = var.environment
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.database_subnet_ids
  instance_class = var.rds_instance_class
}

# ElastiCache for Redis
module "redis" {
  source = "./modules/redis"

  environment     = var.environment
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.database_subnet_ids
  instance_type  = var.redis_instance_type
}
