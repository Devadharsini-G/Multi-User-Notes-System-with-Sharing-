from config import db
from bson.objectid import ObjectId
from models.note_model import update_note
from flask import Blueprint, request, jsonify
note_bp = Blueprint("note_bp", __name__)
@note_bp.route("/update-note/<note_id>", methods=["PUT"])
def update_note_api(note_id):
    data = request.json
    user_id = data["user_id"]

    note = db.notes.find_one({"_id": ObjectId(note_id)})

    if not note:
        return jsonify({"message": "Note not found"}), 404

    # Owner check
    if note["user_id"] == user_id:
        update_note(note_id, data)
        return jsonify({"message": "Note updated (owner)"})

    # Shared permission check
    share = db.note_shares.find_one({
        "note_id": note_id,
        "shared_with": user_id,
        "permission": "write"
    })

    if share:
        update_note(note_id, data)
        return jsonify({"message": "Note updated (shared user)"})

    return jsonify({"message": "Permission denied"}), 403