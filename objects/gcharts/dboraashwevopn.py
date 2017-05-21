class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAASHWEVOPN",
            "title": "Top SQL operations for event: %(DBORAASHWEVOPN)s",
            "subtitle": "",
            "reftime": "DBORAASHREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Number of active sessions",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SA",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "ORAHAS"
                                    ],
                                    "userfunctions": [
                                        "ashcoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "ORAHAS",
                                            "projection": "sql_opname",
                                            "restriction": "session_type = 'FOREGROUND' and session_state = 'WAITING' and event = '%(DBORAASHWEVOPN)s'",
                                            "value": "kairos_count * 1.0 /ashcoeff()"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)