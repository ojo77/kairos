class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORARACGCALLFXTY$$1",
            "collections": [
                "DBORARACGCTS"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'From '||src||' to '||dest as label, cublocks + crblocks as value from DBORARACGCTS) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)