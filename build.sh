#!/bin/bash
APIKEY="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"
sed "s|YOUR_API_KEY_HERE|${APIKEY}|g" ai-hearing-navi.html > /tmp/out.html && mv /tmp/out.html ai-hearing-navi.html && echo "APIキー設定完了"
