class UserObject(dict):
    def __init__(s):
        object = {
            "id": "TTSQLTOPX",
            "title": "Top SQL by executions",
            "subtitle": "",
            "reftime": "TTREFTIME",
            "type": "gchart",
            "yaxis": [
                {
                    "title": "# of executions per second",
                    "scaling": "LINEAR",
                    "position": "LEFT",
                    "properties": {},
                    "minvalue": 0,
                    "maxvalue": null,
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "groupby": "sum",
                                    "projection": "label",
                                    "collections": [
                                        "TTSQLTOPX"
                                    ],
                                    "userfunctions": [],
                                    "info": null,
                                    "onclick": null,
                                    "filterable": true,
                                    "nocache": false,
                                    "pieces": [
                                        {
                                            "table": "TTSQLTOPX",
                                            "projection": "hashid",
                                            "restriction": "",
                                            "value": "execs"
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