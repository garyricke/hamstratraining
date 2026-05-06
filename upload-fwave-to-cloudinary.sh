#!/usr/bin/env bash
# Upload the F-Wave training images to Cloudinary under hamstra-training/fwave-*
# Requires: CLOUDINARY_API_SECRET env var (cloud_name and api_key are baked in).
#
# Usage:
#   CLOUDINARY_API_SECRET="<your-secret>" ./upload-fwave-to-cloudinary.sh
#
# Output: prints each upload's secure_url. Use those URLs in HTML.
set -euo pipefail

CLOUD_NAME="dsbllwpbh"
API_KEY="533151878225121"
API_SECRET="${CLOUDINARY_API_SECRET:-}"

if [[ -z "$API_SECRET" ]]; then
  echo "ERROR: CLOUDINARY_API_SECRET env var is required." >&2
  echo "Run: CLOUDINARY_API_SECRET=\"...\" $0" >&2
  exit 1
fi

# public_id : local file
declare -a PAIRS=(
  "hamstra-training/fwave-hero|generated_imgs/generated-2026-05-06T18-56-39-975Z-ys1apz.png"
  "hamstra-training/fwave-six-nail-pattern|generated_imgs/fwave-six-nail-pattern.png"
  "hamstra-training/fwave-open-valley|generated_imgs/fwave-open-valley.png"
  "hamstra-training/fwave-hand-seal|generated_imgs/fwave-hand-seal.png"
  "hamstra-training/fwave-polymer-vs-asphalt|generated_imgs/fwave-polymer-vs-asphalt.png"
  "hamstra-training/fwave-drip-edge-comparison|generated_imgs/fwave-drip-edge-comparison.png"
)

cd "$(dirname "$0")"

for pair in "${PAIRS[@]}"; do
  PUBLIC_ID="${pair%|*}"
  FILE_PATH="${pair#*|}"

  if [[ ! -f "$FILE_PATH" ]]; then
    echo "  ! SKIP — missing: $FILE_PATH" >&2
    continue
  fi

  TIMESTAMP=$(date +%s)
  # Cloudinary signature: SHA1 of "param1=value1&param2=value2...api_secret"
  # Params must be alphabetically sorted, only signed params (no file, api_key, signature, resource_type, cloud_name).
  TO_SIGN="overwrite=true&public_id=${PUBLIC_ID}&timestamp=${TIMESTAMP}"
  SIGNATURE=$(printf '%s%s' "$TO_SIGN" "$API_SECRET" | openssl dgst -sha1 | awk '{print $NF}')

  echo "→ uploading $FILE_PATH  →  $PUBLIC_ID"
  RESPONSE=$(curl -s -X POST "https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload" \
    -F "file=@${FILE_PATH}" \
    -F "api_key=${API_KEY}" \
    -F "timestamp=${TIMESTAMP}" \
    -F "public_id=${PUBLIC_ID}" \
    -F "overwrite=true" \
    -F "signature=${SIGNATURE}")

  URL=$(echo "$RESPONSE" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('secure_url') or ('ERROR: ' + json.dumps(d.get('error') or d)))")
  echo "   $URL"
done

echo
echo "Done. Use the URL pattern in HTML:"
echo "  https://res.cloudinary.com/${CLOUD_NAME}/image/upload/f_auto,q_auto,w_1400/<public_id>"
