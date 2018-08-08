from django.shortcuts import  render ,HttpResponse

from app01 import models


from rest_framework.views import  APIView
from rest_framework.viewsets import  ViewSetMixin   # 这个是用来让你的url中的as_view中直接设置你的请求的方式的对应的方法  我们在下面可以把我们的post  get的请求的方式对应的方法名给改变


from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet   # GenericViewSet就是之前我们学的  封装了两个方法


from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin

from rest_framework.response import  Response
from rest_framework.pagination import PageNumberPagination   # 分页


from api.utils import response  # 导入你定义的字典类
from api.serializers import course



class CourseAll(ViewSetMixin,APIView):
    def retrive(self,request,pk,*args,**kwargs):
        res = response.BaseResponse()   # 这个是实例化你定义的字典类
        try:
            obj = models.Course.objects.filter(pk = pk).first()
            ret = course.Course(instance=obj)  # 把你的的CourseDetail表的的字段进行校验 序列化
            res.data = ret.data
        except Exception as e:
            res.code = 500
            res.errors = "查询失败"
        return Response(res.dict)
    def create(self,request,*args,**kwargs):
        res = response.BaseResponse()
        '''
        这是你的 post请求的方法方法
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return Response(res.code)

    def list(self,request,*args,**kwargs):
        '''
        这个是查询你的所有的course表中的数据
        :param request:  get
        :param args:
        :param kwargs:
        :return:
        '''
        res = response.BaseResponse()
        try:
            obj = models.Course.objects.all()
            ret = course.Course(instance=obj,many = True)
            res.data = ret.data
        except Exception as e:
            res.code = 500
            res.errors ="查询失败"
        return Response(res.dict)

    def update(self,request,pk,*args,**kwargs):
        '''
        修改
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
        pass
    def destory(self,request,pk,*args,**kwargs):
        '''
        删除
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
        pass




class Course(ListModelMixin,GenericViewSet):
    queryset = models.Course.objects.all()  #queryset是封装的方法
    def list(self,request,*args,**kwargs):  # 这个时候的list就是自带的  也可以重写告诉url他的请求就是list
        course_list  = models.Course.objects.all() # 我们也可以进行重写 queryset








