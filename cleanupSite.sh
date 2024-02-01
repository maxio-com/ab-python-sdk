auth=$(echo "$BASIC_AUTH_USERNAME":"$BASIC_AUTH_PASSWORD" | base64)
curl -i --verbose --request POST --url https://python-sdk.staging-chargify.com/sites/clear_data.json --header "Authorization: $auth"