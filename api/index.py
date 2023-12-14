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
   response = supabase.table('item').select("*").execute()
   return json.dumps(response.data)
