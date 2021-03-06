class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "PGDBOVREADT$$2",
            "collections": [
                "vkpg_stat_database"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, 'all databases'::text as label, blk_read_time as value from vkpg_stat_database) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)