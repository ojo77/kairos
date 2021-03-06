class UserObject(dict):
    def __init__(s):
        object = {
            "id": "NMONPAGE",
            "title": "Paging activity",
            "subtitle": "",
            "reftime": "NMONREFTIME",
            "type": "chart",
            "yaxis": [
                {
                    "title": "# of pages per second",
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
                                    "query": "NMONPAGE$$1",
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