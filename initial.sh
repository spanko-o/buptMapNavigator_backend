#!/bin/bash

# 设定环境变量
export FLASK_APP=app.py
export FLASK_ENV=development

echo "Initializing the database..."
flask db init

echo "Creating migration..."
flask db migrate -m "Initial migration."

echo "Applying migration..."
flask db upgrade

echo "Database migration completed."

echo "Insert into map information..."
python insert_script2.py

echo "Starting Flask server..."
flask run --host=0.0.0.0 --port=5000
