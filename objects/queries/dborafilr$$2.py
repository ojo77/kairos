class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILR$$2",
            "collections": [
                "DBORASTA"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, statistic label, value value from DBORASTA where statistic='physical reads') group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)