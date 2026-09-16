output "notebook_urls" {
  description = "List of URLs of the Databricks notebooks"
  value = [
    for notebook in databricks_notebook.this : notebook.url
  ]
}