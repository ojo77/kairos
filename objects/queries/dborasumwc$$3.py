class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASUMWC$$3",
            "collections": [
                "DBORATMS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, statistic as label, time as value from DBORATMS where statistic='DB time') as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)