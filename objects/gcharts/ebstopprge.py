class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EBSTOPPRGE",
            "title": "E-Business Suite - Programs exited with status 'E'::text",
            "subtitle": "",
            "reftime": "EBSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average number of concurrent sessions per unit of time",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {
                        "text": {
                            "fill": "red"
                        },
                        "line": {
                            "stroke": "red"
                        }
                    },
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
                                        "EBS12CM"
                                    ],
                                    "userfunctions": [
                                        "ebscoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "EBS12CM",
                                            "projection": "prg_name",
                                            "restriction": "status_code = 'E'::text",
                                            "value": "executecount * 1.0 / ebscoeff()"
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
                                    "projection": "label",
                                    "collections": [
                                        "EBS12CM"
                                    ],
                                    "userfunctions": [
                                        "ebscoeff"
                                    ],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "EBS12CM",
                                            "projection": "'All programs with status E'::text",
                                            "restriction": "status_code = 'E'::text",
                                            "value": "executecount * 1.0 / ebscoeff()"
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