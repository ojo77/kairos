class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONDISK",
            "title": "Activity for disk: %(NMONDISK)s",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Read / Write (MB/s)",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": null,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "'Read MB/s'",
                                    "collections": [
                                        "NMONDISKREAD"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "NMONDISKREAD",
                                            "projection": "'xxx'",
                                            "restriction": "id = '%(NMONDISK)s'",
                                            "value": "value / 1024.0"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Write MB/s'",
                                    "collections": [
                                        "NMONDISKWRITE"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "NMONDISKWRITE",
                                            "projection": "'xxx'",
                                            "restriction": "id = '%(NMONDISK)s'",
                                            "value": "value / 1024.0"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Busy rate (%)",
                    "position": "RIGHT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": 110,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "avg",
                                    "projection": "'Busy rate'",
                                    "collections": [
                                        "NMONDISKBUSY"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": true,
                                    "pieces": [
                                        {
                                            "table": "NMONDISKBUSY",
                                            "projection": "'xxx'",
                                            "restriction": "id = '%(NMONDISK)s'",
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