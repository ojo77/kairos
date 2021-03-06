class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODEXEW$$3",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, avg(value) as value from (select timestamp, 'Wait time'::text as label, wait * 60.0 as value from EBS12CM where node_name = '%(EBSNODEXEW)s'::text) as foo group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)