class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "NMONCPUV$$1",
            "collections": [
                "NMONLPAR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, id label, value value from NMONLPAR where id in ('VP_User%', 'VP_Sys%', 'VP_Wait%', 'VP_Idle%')) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)