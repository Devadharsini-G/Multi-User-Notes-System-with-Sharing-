from flask import Blueprint, request, jsonify
from models.share_model import share_note, get_shared_notes

share_bp = Blueprint("share", __name__)

# SHARE NOTE
@share_bp.route("/share-note", methods=["POST"])
def share_note_api():
    data = request.json

    share_data = {
        "note_id": data["note_id"],
        "owner_id": data["owner_id"],
        "shared_with": data["shared_with"],
        "permission": data["permission"]
    }

    share_note(share_data)

    return jsonify({"message": "Note shared successfully"})


# GET SHARED NOTES
@share_bp.route("/shared-notes/<user_id>", methods=["GET"])
def get_shared_notes_api(user_id):
    notes = get_shared_notes(user_id)

    for note in notes:
        note["_id"] = str(note["_id"])

    return jsonify(notes)