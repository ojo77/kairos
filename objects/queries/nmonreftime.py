class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONREFTIME",
            "collections": ["NMONCPU"],
            "request": "select distinct timestamp from NMONCPU"
        }
        super(UserObject, s).__init__(**object)