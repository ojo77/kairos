class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSQLSES$$1",
            "collections": [
                "ORAHAS"
            ],
            "userfunctions": [
                "ashcoeff"
            ],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, session_id||' - '||program label, kairos_count * 1.0 /ashcoeff() value from ORAHAS where session_type = 'FOREGROUND' and sql_id = '%(DBORAASHSQLSES)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)