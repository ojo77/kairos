class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALIBI$$1",
            "collections": [
                "DBORALIB"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, item label, invalidations value from DBORALIB) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)