date
curl -XPOST \
    -H 'Content-Type: application/json' \
    -d '{
        "data": {
            "image_uri": "https://pc-ap.renttherunway.com/productimages/front/1080x/5c/SA97.jpg"
        }
    }' \
    "http://py-api-fe-MyLoadBa-1E7CQ1BROBY0G-1403710224.us-east-1.elb.amazonaws.com/classes"
