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

@app.route('/item.upload', methods=['GET','POST'])
def api_endpoint_item_upload():
    
            # Retrieve data from the JSON request body
            name = request.form.get('name')
            price = request.form.get('price')
            size = request.form.get('size')
            image_path = request.form.get('image_path')
            description = request.form.get('description')
            id_wilaya = request.form.get('id_wilaya')
            id_category = request.form.get('id_category')
            id_commune = request.form.get('id_commune')
            id_type = request.form.get('id_type')
            id_user = request.form.get('id_user')

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

                

            if error:
                return json.dumps({'status': 500, 'message': error})

            return json.dumps({'status':200,'message':'','data':response.data[0]})

        
