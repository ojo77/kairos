class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASVADM$$1",
            "collections": [
                "DBORASVW"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, service label, admwaitt value from DBORASVW) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)