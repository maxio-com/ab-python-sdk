
# Environment-Based Client Initialization

The SDK client can also be initialized directly from environment variables using the `from_environment()` class method. This allows the SDK to automatically read configuration values from the runtime environment or a .env file.

## Example

```python
from advancedbilling.advanced_billing_client import AdvancedBillingClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = AdvancedBillingClient.from_environment(dotenv_path='/path/to/.env')
```

You can also specify a path to a `.env` file by passing it to the `from_environment()` method:

The same method can accept keyword arguments to override any values read from the environment, and the arguments to override values should follow the same approach as code-based client initialization.

```python
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

client = AdvancedBillingClient.from_environment(
    dotenv_path='/path/to/.env',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    )
)
```

Values provided through arguments take precedence over those defined in environment variables.

Authentication credentials are left out of the example `.env` file below. Keep credentials out of `.env` and configuration files that are committed to source control or shipped with your application, and load them at runtime from a secret manager or your hosting platform's environment instead. Pass them to `from_environment()` as keyword arguments, as shown above.

## Example `.env` File

```python
SITE=subdomain
ENVIRONMENT=us

TIMEOUT=60
MAX_RETRIES=3
BACKOFF_FACTOR=2
RETRY_STATUSES=408,413
RETRY_METHODS=GET,PUT,DELETE

# Proxy Configuration
PROXY_ADDRESS=http://localhost:3000
PROXY_PORT=8080
```

## Note

- If an environment variable is not defined, the default SDK configuration value will be used.

