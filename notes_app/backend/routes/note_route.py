from config import db
from bson.objectid import ObjectId
from datetime import datetime

# CREATE NOTE
def create_note(note_data):
    note_data["created_at"] = datetime.utcnow()
    note_data["is_deleted"] = False
    return db.notes.insert_one(note_data)


# GET ALL NOTES OF A USER
def get_notes_by_user(user_id):
    return list(db.notes.find({
        "user_id": user_id,
        "is_deleted": False
    }))


# UPDATE NOTE
def update_note(note_id, updated_data):
    return db.notes.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": updated_data}
    )


# SOFT DELETE NOTE
def delete_note(note_id):
    return db.notes.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {"is_deleted": True}}
    )