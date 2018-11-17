import pyrebase

config = {
    "apiKey": "AIzaSyBmehyMgBL4UfCaB66I05cuknt5dQl_T4g",
    "authDomain": "rpiappcontrol-1f76e.firebaseapp.com",
    "databaseURL": "https://rpiappcontrol-1f76e.firebaseio.com/",
    "projectId": "rpiappcontrol-1f76e",
    "storageBucket": "rpiappcontrol-1f76e.appspot.com",
    "messagingSenderId": "537116058868"
  }

firebase = pyrebase.initialize_app(config)
#data = {
#    "name": "Mortimer 'Morty' Smith"
#}
db = firebase.database()
st = firebase.storage()
#db.child("users").child("Morty")
data = {"occupied": "0"}
db.child("aeon").update(data)
#st.child(download.jpg).get_url()
st.child("carpark")
st.child("carpark").put("road.jpg")
#st.child("david/road.jpg").get_url()
#st.child("images/road.jpg").put("road1.jpg")
#urllink = st.child("images/road1.jpg").get_url(1)
#data = {"park": urllink}
#db.child("url").update(data)
