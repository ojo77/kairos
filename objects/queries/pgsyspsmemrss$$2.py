class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGSYSPSMEMRSS$$2",
            "collections": [
                "vpsutil_processes"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, 'All processes' label, rss value from vpsutil_processes) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)