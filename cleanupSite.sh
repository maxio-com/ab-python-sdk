auth=$(echo "$BASIC_AUTH_USERNAME":"$BASIC_AUTH_PASSWORD" | base64)

curl -i --request POST \
  --url https://"$SUBDOMAIN"."$DOMAIN"/sites/clear_data.json \
  --header "Authorization: Basic $auth" \
  --header 'Content-Type: application/json'