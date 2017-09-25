from ansible import errors

def to_list(value):
    try:
        res_list = value.split(",")
        return res_list
    except Exception, e:
        raise errors.AnsibleFilterError("to list error: %s" % str(e))

class FilterModule(object):
    def filters(self):
        return {
          'to_list': to_list
        }
