
class PoliticianSchema:

    post_response = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "message": {"type": "string"},
            "ok": {"type": "boolean"},
        },
    }

    get_response = {
        "type": "array",
        "properties": {
            "country": {"type": "string"},
            "createdAt": {"type": "string"},
            "id": {"type": "string"},
            "name": {"type": "string"},
            "position": {"type": "string"},
            "risk": {"type": "number"},
            "yob": {"type": "number"},
        },
    }

    getbyid_response = {
        "type": "object",
        "properties": {
            "country": {"type": "string"},
            "createdAt": {"type": "string"},
            "id": {"type": "string"},
            "name": {"type": "string"},
            "position": {"type": "string"},
            "risk": {"type": "number"},
            "yob": {"type": "number"},
        },
    }

    def __init__(self):
        pass
