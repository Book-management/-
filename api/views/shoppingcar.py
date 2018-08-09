import redis

import json
from  app01 import models
from django.conf import settings
from api.utils import response  # 导入你自定义的字典类
from django.shortcuts import render,HttpResponse
# from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser  # JSONParser 是会自动对你的请求体中的数据进行json.loads  反序列化后我们就去request.data中取值


USER_ID = 2  # 我们先设置默认的一个用户id
# CONN = redis.Redis(host="192.168.11.148", port = 6379) # 全局变量大写
CONN = redis.Redis(host="192.168.11.175", port = 6379)



# 购物车 这个时候你要想下平时 的生活 是先加入购物车再去查看购物车内的信息

class ShoppingCarView(ViewSetMixin,APIView):
    # parser_classes = [JSONParser]  # 实例化JSONParser 这个就会自动取你的请求体中进行反序列化  然后下面就去request.data中取值
    def list(self,request,*args,**kwargs):
        # conn.hset("zy_name","name1","老王")
        # conn.hset("zy_name","name2","隔壁老王")
        #
        # name1 = conn.hget("zy_name","name1").decode("utf8")
        # name2 = conn.hget("zy_name","name2").decode("utf8")
        '''
        查看购物车的信息
        购物车的信息你要知道 用户id  课程id  价格策略
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        return Response("...")

    def create(self,request,*args,**kwargs):
        print(11111111)
        '''
        这个是给你的购物车添加信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        res = response.BaseResponse()

        CONN = redis.Redis()  # 生成一个redis字典的实例
        # 这个时候你要知道redis是一个大字典{ }  这个时候要设置一个key设置一个key值 这个key我们要设置不一样的  以防止你以后的存储的会覆盖它
        # 我们就以 类名_用户id_课程id拼接起来用作当key  里面放置这个用户对应的信息
        course_id = request.data.get('courseid') # 取到你的课程id
        policy_id = request.data.get('policyid')  # 取到你的课程id
        # 取到数据之后你要判断你的数据是否合法
        #     课程是否存在  价格策略是否合法
        #先判断课程是否存在
        course_obj = models.Course.objects.filter(pk = course_id).first()
        if not course_obj:  # 如果不存在  这个就是简单的逻辑放在上面 编程思想
            res.code = 500
            res.errors = "课程不存在"
            return Response(res.dict)
        # 下面就是课程存在的时候 就要验证价格是否合法
        policy_list = course_obj.price_policy .all()  # 这是得到所有课程的的价格策略的对象
        price_policy_dict = {}  # 定义一个字典 马上让你的价格策略的所有的信息都存进去
        for item in policy_list:
            items= {  # 得到价格策略的所有的信息
                "id":item.id,
                "price":item.price,
                "valid_period":item.valid_period, # 得到你的周期的所有的数字
                "valid_period_display":item.get_valid_period_display() # 得到你的周期的所有数字对应的中文
            }
            price_policy_dict[item.id] = items   # 把你的所有的策略信息存放到这个字典中
        # 上面已经把你的策略信息放进去了 这个时候你就要判断你传进来的策略信息是不是在所有的策略信息都额字典中
        if policy_id not in price_policy_dict:  # 如果不在里面
            res.code = 501
            res.errors = "傻X 价格策略别瞎改"
            return Response(res.dict)
        # 如果在里面 就是成功了 就要把购物车的信息放置进去
            # 3. 把商品和价格策略信息放入购物车 SHOPPING_CAR
        '''
                 购物车中要放：
                课程ID
                课程名称
                课程图片
                默认选中的价格策略
                所有价格策略
        '''
        # 我们可以用来判断购物车的数量 如果你的购物车的数量是超出你的定义的的话就把你存放的信息清空
        # pattern = settings.LUFFY_SHOPPING_CAR % (USER_ID,"*")  # 这个是导入你设置的settings中的用户id然后*是代表的所有  意思就是这个用户id的下的所有的key
        # keys = CONN.keys(pattern)  # keys是找到这个key下的所有的key
        # if keys and len(keys) > 100:  #如果这个用户的信息存在并且存放额数据是大于100个
        #     return Response({"code":5002, "errors":"购物车信息过多先去结算"})
        # 然后下面把你的信息写入进redis内
        print(333)
        # key = settings.LUFFY_SHOPPING_CAR % (USER_ID,course_id)
        key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)
        print(444)
        CONN.hset(key,"id",course_id) # hset就是对子弹的操作就是你第一个参数是key 后面是的两个参数就是一个字典
        print(5555555)
        CONN.hset(key,"name",course_obj.name)  # 把你的课程名字放进去
        print(77777777)
        CONN.hset(key,"img",course_obj.course_img)
        print(888888888888)
        CONN.hset(key,"default_price_id", policy_id )
        print(66666)
        # CONN.hset(key,"price_policy_dict",json.dumps(price_policy_dict))  # 把你的所有的额课程的信息都放进去  但是你的redis不支持第三层内部放置的是字典  如果第三层内部是字典必须序列化
        CONN.hset(key, 'price_policy_dict', json.dumps(price_policy_dict))
        print(555)


        CONN.expire(key,20*60)  # 设置的是20*60秒后伸出你的这个key

        return Response({"code":1000,"data":"购买成功赶紧去学习吧"})





    def create_al(self,request,*args,**kwargs):

        '''
        向你的购物车中添加信息

        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 因为你已经在你的settings中配置了一个JSONParser 所以直接就可以在request.data中取值
        course_id = request.data.get("courseid")  # 课程id
        policy_id = request.data.get("policyid")  # 价格策略id

        #然后下面就要校验你的课程id和价格策略id是否合法

        # 先验证你的课程id是否存在
        course = models.Course.objects.filter(pk = course_id).first()
        if not course: # 如果不存在
            return Response({'code':10001,'error':'课程不存在'})
        #如果存在


        #验证价格策略id  先找到课程所对应的所有的价格策略
        # 根据你的满足额课程来找价格策略
        price_policy_queryset = course.price_policy.all()  # 因为是contentType 所以可以通过GenericRelation的字段进行反向查找

        price_policy_dict = {}  # 定义一个字典用来存放所有的价格策略数据信息
        for item in price_policy_queryset :
            itmp = {
                "id":item.id,
                "price":item.price,
                "valid_period":item.valid_period,
                "valid_period_display":item.get_valid_period_display()
            }
            price_policy_dict [item.id] = itmp  # 把你的所有的课程对应的价格策略都加入到这个字典中

        if policy_id not in  price_policy_dict:  # 如果价格策略不在你的课程关联的价格所有的策略中
            return Response({'code':10002,'error':'傻×，价格策略别瞎改'})


        # 下面就是都满足了就把所有的信息放入redis中

        key = settings.LUFFY_SHOPPING_CAR %(USER_ID,course_id)
        CONN.hset(key,"id", course_id)
        CONN.hset(key, "name",course.name)  #课程名字
        CONN.hset(key,"img",course.course_img )
        CONN.hset(key,'default_price_id',policy_id)
        CONN.hset(key,'price_policy_dict',json.dumps(price_policy_dict))

        return Response({'code': 10000, 'data': '购买成功'})





