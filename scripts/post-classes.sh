curl -XPOST \
    -H 'Content-Type: application/json' \
    -d '{
        "data": {
            "image_uri": "https://pc-ap.renttherunway.com/productimages/front/1080x/5c/SA97.jpg"
        }
    }' \
    "http://ec2-54-174-19-194.compute-1.amazonaws.com:8888/classes"
