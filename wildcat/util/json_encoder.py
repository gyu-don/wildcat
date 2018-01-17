import json
import math

class CompactEncoder(json.JSONEncoder):
    "JSON encoder that renders floats to two decimal places"

    FLOAT_FRMT = '{0:.2f}'

    def floatstr(self, obj):
        return self.FLOAT_FRMT.format(obj)

    def default(self, obj):
        if isinstance(obj, float):
            self.floatstr(obj)
        return json.JSONEncoder.default(self, obj)

    def _iterencode(self, obj, markers=None):
        # stl JSON lame override #1
        new_obj = obj
        if isinstance(obj, float):
            if not math.isnan(obj) and not math.isinf(obj):
                new_obj = self.floatstr(obj)
        return super(CompactEncoder, self)._iterencode(new_obj, markers=markers)

    def _iterencode_dict(self, dct, markers=None):
        # stl JSON lame override #2
        new_dct = {}
        print(dct)
        for key, value in dct.iteritems():
            if isinstance(key, float):
                if not math.isnan(key) and not math.isinf(key):
                    key = self.floatstr(key)
            new_dct[key] = value
        return super(CompactEncoder, self)._iterencode_dict(new_dct, markers=markers)