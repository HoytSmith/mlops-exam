variable "adb_service_url" {
  type        = string
  description = "URL of the Azure Databricks Workspace, should be like https://adb-XXXXXXXXXXXXX.azuredatabricks.net"
}

variable "subscription_id" {
  type        = string
  description = "ID of the Azure subscription."
}

variable "databricks_folder" {
  type        = string
  description = "Default Databricks Folder to save the notebooks"
  default     = "Terraform"
}

variable "local_folder" {
  type        = string
  description = "Local Folder containing notebooks"
  default     = "notebooks"
}
