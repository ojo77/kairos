class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACDBWAITEI$$1",
            "collections": [
                "DBORARACTTFE"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, event|| ' / '||inum label, timewaited value from DBORARACTTFE where inum != 0 and event != 'DB CPU') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)