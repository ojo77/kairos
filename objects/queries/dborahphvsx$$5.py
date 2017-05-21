class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHPHVSX$$5",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Fetches' label, sum(value) value from (select timestamp, 'xxx' label, fetches_delta * 1.0 / (case when executions_delta = 0 then 1 else executions_delta end) value from ORAHQS where plan_hash_value='%(DBORAHPHVSX)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)