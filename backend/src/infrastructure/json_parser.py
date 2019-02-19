class JsonParser(object):

    @classmethod
    def try_get_parameter(cls, json, name):
        try:
            return json[name]
        except:
            return None
