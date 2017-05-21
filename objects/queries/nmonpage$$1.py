class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONPAGE$$1",
            "collections": [
                "NMONPAGE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONPAGE where id in ('pgin', 'pgout', 'pgsin', 'pgsout')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)