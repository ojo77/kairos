class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBOVREADB$$1",
            "collections": [
                "vkpg_stat_database"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, datname label, blks_read value from vkpg_stat_database) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)