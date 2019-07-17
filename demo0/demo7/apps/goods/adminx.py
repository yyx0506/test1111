
from .models import *
import xadmin

class GoodsAdmin:
    style_fields={"goodscontent": "ueditor"}
# Register your models here.
xadmin.site.register(Goodsinfo,GoodsAdmin)
xadmin.site.register(TypeInfo)
xadmin.site.register(Ads)



