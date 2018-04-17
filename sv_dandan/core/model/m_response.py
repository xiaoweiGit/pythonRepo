
class response(object):

    def __init__(self,code=-1,msg=u'接口调用失败！'):
        """

        :type code: object
        """
        self.code=code
        self.msg=msg