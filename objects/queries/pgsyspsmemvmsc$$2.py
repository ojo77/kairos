class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSPSMEMVMSC$$2",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'All commands'::text as label, vms::real as value from vpsutil_processes) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)