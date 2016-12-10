curl -XPOST \
    -H 'Content-Type: application/json' \
    -d '{
        "data": {
            "image_uri": "https://pc-ap.renttherunway.com/productimages/front/1080x/5c/SA97.jpg"
        }
    }' \
    "localhost:8888/classes"
