from flask import Flask, request
import json
from supabase import create_client, Client

app = Flask(__name__)

#This is the very stupid way to store private/confidential data inside GIT
#Store inside a file to be ignored
url="https://jzredydxgjflzlgkamhn.supabase.co"
key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp6cmVkeWR4Z2pmbHpsZ2thbWhuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIzMDQ1OTYsImV4cCI6MjAxNzg4MDU5Nn0.7jYAyMpWdzAnyioSoVkJiRFWzWyZvs0kdDxlli02er4"
supabase: Client = create_client(url, key)

@app.route('/item.get')
def api_item_get(): 
   response = supabase.table('item').select("*,wilaya(name)").execute()
   return json.dumps(response.data)

@app.route('/item.upload', methods=['POST'])
def api_endpoint_item_upload():
    if request.method == 'POST':
        
            # Hardcoded values for testing
            name = "Test Item"
            price = 10.99
            size = "M"
            image_path = "test_image_path"
            description = "Test description"
            id_wilaya = "test_wilaya_id"
            id_category = 1  # Adjust based on your actual data type
            id_commune = 1   # Adjust based on your actual data type
            id_type = 1      # Adjust based on your actual data type
            id_user = "test_user_id"

            # Your existing error checking logic
            error = False
            if not error:
                response = supabase.table('item').insert({
                    "name": name,
                    "price": price,
                    "size": size,
                    "description": description,
                    "id_user": id_user,
                    "id_commune": id_commune,
                    "id_wilaya": id_wilaya,
                    "id_type": id_type,
                    "id_category": id_category,
                    "image_path": image_path
                }).execute()

                
    else:
            return json.dumps({'status': 200, 'message': '', 'data': response.data})