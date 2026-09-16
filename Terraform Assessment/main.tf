data "databricks_current_user" "me" {
}

locals {
  default_local_folder = "${path.module}/${var.local_folder}"
  default_db_folder    = "${data.databricks_current_user.me.home}/${var.databricks_folder}"
  users                = {
    user_1 = "notebook_1"
    user_2 = "notebook_2"
  }
}

# Add notebooks to the workspace 
resource "databricks_notebook" "this" {
  for_each = local.users

  language = "PYTHON"
  source   = "${local.default_local_folder}/${each.value}.py"
  path     = "${local.default_db_folder}/${each.value}"
}
