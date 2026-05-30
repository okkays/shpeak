SHPEAK_HOST='http://localhost:5000'

function say() {
  curl \
    -s \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"to_say":"'"$1"'"}' \
    "$SHPEAK_HOST/say"
}
