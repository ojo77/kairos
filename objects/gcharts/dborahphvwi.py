class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORAHPHVWI",
            "title": "Top PHV - Waits due to I/O",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of seconds per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": {
                                        "query": "DBORAHHELPP",
                                        "variable": "DBORAHELPP"
                                    },
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, plan_hash_value, iowait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp)",
                                            "projection": "plan_hash_value",
                                            "restriction": "",
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'Captured PHVs'",
                                    "collections": [
                                        "ORAHQS",
                                        "DBORAMISC"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "(select h.timestamp timestamp, plan_hash_value, iowait_delta / 1000000.0 / m.elapsed value from ORAHQS h, DBORAMISC m where h.timestamp = m.timestamp)",
                                            "projection": "'xxx'",
                                            "restriction": "",
                                            "value": "value"
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
