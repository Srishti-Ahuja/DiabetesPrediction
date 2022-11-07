from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'storageblob1234' # Must be replaced by your <storage_account_name>
    account_key = 'gzeepIyLyKmNj6gi3hboGO3/Lu1/7hSk2Q3ujgwPSuEyiHlhfI+V1LnKZEWVjw6GpDekBcW0JshS+AStAtc+Bg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'storageblob1234' # Must be replaced by your storage_account_name
    account_key = 'gzeepIyLyKmNj6gi3hboGO3/Lu1/7hSk2Q3ujgwPSuEyiHlhfI+V1LnKZEWVjw6GpDekBcW0JshS+AStAtc+Bg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
