from firebase import firebase

def firebase_database(report):
#     print(report)
    con = firebase.FirebaseApplication(FIREBASE_URI)        
    result = con.post(DATABASE_URI, report)
