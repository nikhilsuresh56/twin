project_name             = "twin"
environment              = "prod"
bedrock_model_id         = "amazon.nova-lite-v1:0"  # Use better model for production
lambda_timeout           = 90
api_throttle_burst_limit = 20
api_throttle_rate_limit  = 10
use_custom_domain        = true
root_domain              = "nikhildigitaltwin.com"  # Replace with your actual domain