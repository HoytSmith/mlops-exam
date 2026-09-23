# Terraform Assessment

This project demonstrates my ability to automate cloud infrastructure with Terraform for Azure Databricks. The goal was to create a reusable configuration for provisioning notebooks across multiple users while keeping environment-specific values separate from source code and making deployment repeatable.

## Overview

The assignment focused on building a Terraform-based solution for Azure Databricks. The project uses a map of users to notebook names and creates one notebook per user in a shared Databricks folder. The solution is designed to be easily extended for additional users without rewriting the infrastructure code.

## Objectives

The main goals of the project were to:

- create a Terraform root module for Databricks notebook deployment
- support multiple users through a configurable map
- store notebooks in a folder named by a Terraform variable
- assign a default value for the Databricks folder name
- include a notebook parameter named `PARAMETER` with an empty default if no value is provided
- create notebooks containing a user-specific comment such as `# created for user_X`
- expose notebook URLs as an output named `notebook_urls`
- configure Azure and Databricks providers using variables and environment-based values

## Project Structure

The project contains:

- Terraform configuration for Azure resources
- Databricks provider configuration
- variable definitions
- notebook generation logic
- output values for created notebook URLs

## Implementation Details

### User-to-Notebook Mapping

The solution accepts a map such as:

```hcl
users = {
  user_1 = "notebook_1"
  user_2 = "notebook_2"
}
```

This allows the Terraform configuration to create multiple notebooks in a structured and maintainable way. The setup is easily extensible to additional users by adding more entries to the map.

### Databricks Notebook Storage

Each notebook is stored in a folder under the user’s home directory, using the variable:

```
databricks_folder
```

with a default value of:

```
Terraform
```

This keeps the organization of notebooks consistent and easy to manage in the Databricks workspace.

### Provider Configuration

The project separates configuration values from code:

- subscription_id is passed as a Terraform variable
- adb_service_url is treated as a sensitive runtime value and supplied through an environment variable

This follows Terraform and cloud best practices by avoiding hardcoded secrets or environment-specific configuration inside the codebase.

## Terraform Workflow

The deployment flow for this project used the standard Terraform lifecycle:

```bash
export TF_VAR_adb_service_url="https://your-databricks-workspace-url"
terraform init
terraform plan
terraform apply -auto-approve
```

This workflow initializes the providers, validates the infrastructure plan, and applies the Databricks notebook deployment.

## Outputs

The Terraform configuration exposes the created notebook URLs using the key:

```
notebook_urls
```

This makes it easy to retrieve and validate the generated outputs after deployment.

## Technologies Used

- Terraform
- Azure Resource Manager
- Databricks
- Azure Databricks notebooks
- HCL

## Skills Demonstrated

This project showcases practical experience with:

- infrastructure as code
- Terraform module design
- provider configuration
- environment variable usage for sensitive data
- Databricks workspace automation
- resource provisioning through declarative configuration

## Outcome

The final result is a reusable Terraform configuration that provisions Databricks notebooks for multiple users, keeps configuration flexible, and demonstrates a clean infrastructure automation workflow suitable for real-world cloud environments. This project highlights my ability to automate infrastructure in a repeatable, scalable, and production-friendly way.
