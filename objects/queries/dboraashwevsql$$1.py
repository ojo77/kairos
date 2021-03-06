class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHWEVSQL$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sql_id as label, kairos_count * 1.0 /ashcoeff() as value from ORAHAS where session_type = 'FOREGROUND' and session_state = 'WAITING' and event = '%(DBORAASHWEVSQL)s') as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)