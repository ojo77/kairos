class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORACHOOSEWEV$$1",
            "collections": [
                "DBORAWEV"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'average time (ms)' label, avg(value) value from (select timestamp, event label, 1000.0 * time / count value from DBORAWEV where event='%(DBORAWEV)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)