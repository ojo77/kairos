class UserObject(dict):
    def __init__(s):
        object = {
            "id": "PGSYSMEM",
            "title": "Memory usage",
            "subtitle": "",
            "reftime": "PGSYSREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "Size",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "vpsutil_virtual_memory"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": false,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Total size'",
                                            "restriction": "",
                                            "value": "total"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Available size'",
                                            "restriction": "",
                                            "value": "available"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Used size'",
                                            "restriction": "",
                                            "value": "used"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Free size'",
                                            "restriction": "",
                                            "value": "free"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Active size'",
                                            "restriction": "",
                                            "value": "active"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Inactive size'",
                                            "restriction": "",
                                            "value": "inactive"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Buffers size'",
                                            "restriction": "",
                                            "value": "buffers"
                                        },
                                        {
                                            "table": "vpsutil_virtual_memory",
                                            "projection": "'Cached size'",
                                            "restriction": "",
                                            "value": "cached"
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