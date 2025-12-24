#!/bin/bash

COMMIT_MESSAGE='Sample commit message with special characters: "Quotes", new lines
and $dollar signs.'

PAYLOAD=$(jq -n --arg text "✅ ML API built & deployed successfully!\n\n📝 Commit: $COMMIT_MESSAGE" '{text: $text}')
echo "$PAYLOAD" | jq .

