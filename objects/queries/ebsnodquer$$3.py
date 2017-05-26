class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODQUER$$3",
            "collections": [
                "EBS12CM"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Response time' label, avg(value) value from (select timestamp, 'xxx' label, time * 60.0 value from EBS12CM where node_name = '%(EBSNODQUER)s') group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)