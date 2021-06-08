from django.shortcuts import render, redirect
from django.views import View

from cart.cartmanager import *

# Create your views here.


class AddCartView(View):
    def post(self,request):
        #在多级字典数据的时候，需要手动设置modified=True，实时地将数据存入到session对象中
        request.session.modified = True


        # 1.获取当前操作类型
        flag = request.POST.get('flag', '')

        # 2.判断当前操作类型
        if flag == 'add':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 加入购物车操作
            carManagerObj.add(**request.POST.dict())
        elif flag == 'plus':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            #修改商品的数量（添加）
            carManagerObj.update(step=1,**request.POST.dict())

        elif flag == 'minus':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 修改商品的数量（添加）
            carManagerObj.update(step=-1, **request.POST.dict())

        elif flag == 'delete':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            #逻辑删除购物车选项
            carManagerObj.delete(**request.POST.dict())

        return redirect('cart:queryAll')


class CartListView(View):
    def get(self,request):
        # 创建cartManager对象
        carManagerObj = getCartManger(request)

        #查询所有购物项信息
        cartList = carManagerObj.queryAll()


        return render(request,'cart.html',{'cartList':cartList})