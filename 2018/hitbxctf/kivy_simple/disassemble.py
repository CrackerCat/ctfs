import binascii
import marshal
import zlib
import dis

class LoginScreen():

    def __init__(self, **kwargs):
        self.flag = 'HITB{THIS_IS_TEST_FLAG}'

    def check(self):
        if self.flag == 'HITB{this_is_not_flag}':
            return True
        return False

    def auth(self, instance):
        if self.check():
            s = 'Congratulations you got the flag'
        else:
            s = 'Wrong answer'
        print s

screen = LoginScreen()
b64 = 'eJzF1MtOE2EUB/DzTculUKAUKJSr3OqIV0TBGEOMRqIuatJhowsndTrVA+MlnYEYhZXEhQuXLlz4CC58BBc+ggsfwYWPYDznhHN8BJr5Tv7fby6Z8/VrIzj+eDRu0kirVFoARwCPAGI6HOx4EBI6CHy+LHLH1/O4zfd8onQAsEOHg0MHmQcHDt45vmc3B50FyHIQELU8qLZyYutmebIusftm3WQ9Yo/NeskKYh2zPrJ+sfdmRbIBsc9mg2RDYl/NSmTDYt/NymQjYj/NRsnGxH6bVcjGxf6aTZBVxcpObdL6rZlNkU2LXTebsT7qZrP2fk/M5shOie2bzdvzPpgtkC2KfTFbIlsW+2ZWIzst9sPMJzsj9stsheys2B+zc2TnxTxP7YL1UTG7aLZidolsVWzT7LL11jBbI7si1ja7SrYu9sZsw+yjWJaHgHZx4F+j/VnHOao4TCXjvbuBQxqXsV9jgDmNt7CiMURP4zZOaXyA3RrncVTjEpY0djCv8S2Oa3yF/OtC0PldLPN8hkuf4ioO8nxA5zWc1LiITuM97NG4hbMaD3FE4z4W+TEFLhOKD7GL59M6r+OYxjXsperz+YzfvZ00n0rI4tdZxkuTxC8yPr3VTNJYTm139mL5S5BZGidteVTqc4dSMil8V/Qsjnb52vSIzRVdGfKu5E5seHWfu2rw3sj460yjTkwt8oqFYZQ00zQM/3cipSErzQt14/nL1l4Sb0pHXAp3/gENPMQt'
eval(marshal.loads(zlib.decompress(binascii.a2b_base64(b64))))
# print dis.disassemble(marshal.loads(zlib.decompress(binascii.a2b_base64(b64))))
dis.disassemble(screen.__class__.check.im_func.func_code)
