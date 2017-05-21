class UserObject(dict):
    def __init__(s):
        object = {
            "id": "DBORASGLR",
            "title": "Top segments by logical reads",
            "subtitle": "",
            "reftime": "DBORAREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of blocks / logical reads per second",
                    "position": "LEFT",
                    "scaling": "LINEAR",
                    "properties": {},
                    "renderers": [
                        {
                            "type": "SC",
                            "datasets": [
                                {
                                    "query": "DBORASGLR$$1",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        },
                        {
                            "type": "L",
                            "datasets": [
                                {
                                    "query": "DBORASGLR$$2",
                                    "timestamp": "timestamp",
                                    "label": "label",
                                    "value": "value"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        super(UserObject, s).__init__(**object)