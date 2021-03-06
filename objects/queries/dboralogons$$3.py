class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORALOGONS$$3",
            "collections": [
                "DBORAMISC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'sessions'::text as label, sessions as value from DBORAMISC) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)