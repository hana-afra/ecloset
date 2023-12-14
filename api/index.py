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
def api_endponit_item_upload():
    if request.method == 'POST':
        try:
            # Retrieve data from the JSON request body
            data = request.json

            name = data.get('name')
            price = data.get('price')
            size = data.get('size')
            image_path = data.get('image_path')
            description = data.get('description')
            id_wilaya = data.get('id_wilaya')
            id_category = data.get('id_category')
            id_commune = data.get('id_commune')
            id_type = data.get('id_type')
            id_user = data.get('id_user')

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

                if len(response.data) == 0:
                    error = 'Error creating the item'

            if error:
                return json.dumps({'status': 500, 'message': error})

            return json.dumps({'status': 200, 'message': '', 'data': response.data})

        except Exception as e:
            return json.dumps({'status': 500, 'message': f'Error: {str(e)}'})

    return json.dumps({'status': 400, 'message': 'Bad Request'})