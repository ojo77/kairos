class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGTS$$2",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [
                "meet"
            ],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, statistic as label, value as value from DBORASTA where meet(statistic, 'table scans')) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)