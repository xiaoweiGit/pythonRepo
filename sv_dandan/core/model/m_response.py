from core.lib.jsonModel import jsonModel


@jsonModel()
class responseData(object):

    def __init__(self, code=-1, msg=u'接口调用失败！', data=[]):
        """

        :type code: object
        """
        self.code = code
        self.msg = msg
        self.data = data


@jsonModel()
class response(object):

    def __init__(self, code=-1, msg=u'接口调用失败！'):
        """

        :type code: object
        """
        self.code = code
        self.msg = msg
