class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHSQLTX$$5",
            "collections": [
                "ORAHQS"
            ],
            "userfunctions": [],
            "request": "select timestamp, 'Cpu' label, sum(value) value from (select timestamp, 'xxx' label,  value from (select timestamp, sum(cpu_time_delta) / 1000000.0 / (case when sum(executions_delta) = 0 then 1 else sum(executions_delta) end) value from ORAHQS where sql_id = '%(DBORAHSQLTX)s' group by timestamp)) group by timestamp, label order by timestamp",
            "nocache": true,
            "filterable": false
        }
        super(UserObject, s).__init__(**object)