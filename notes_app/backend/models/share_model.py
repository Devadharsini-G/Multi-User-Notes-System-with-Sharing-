from config import db

def share_note(data):
    return db.note_shares.insert_one(data)


def get_shared_notes(user_id):
    return list(db.note_shares.find({"shared_with": user_id}))