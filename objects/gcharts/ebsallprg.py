class UserObject(dict):
    def __init__(s):
        object = {
            "id": "EBSALLPRG",
            "title": "E-Business Suite - Running & Waiting programs",
            "subtitle": "",
            "reftime": "EBSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Average number of programs per unit of time",
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
                                    "projection": "'Running programs'",
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
                                            "projection": "'xxx'",
                                            "restriction": "prg_name not like 'FNDRS%'",
                                            "value": "executecount * 1.0 / ebscoeff()"
                                        }
                                    ]
                                },
                                {
                                    "groupby": "sum",
                                    "projection": "'Waiting programs'",
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
                                            "projection": "'xxx'",
                                            "restriction": "prg_name not like 'FNDRS%'",
                                            "value": "waitcount * 1.0 / ebscoeff()"
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