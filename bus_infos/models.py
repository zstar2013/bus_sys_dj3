from django.db import models
# Create your models here.
class RouteInfo(models.Model):
    TEAMS = (
        ('1', '1队'),
        ('2', '2队'),
        ('3', '3队'),
        ('4', '4队'),
        ('5', '5队')
    )

    routename=models.CharField(max_length=10,default="new route")
    team=models.CharField(max_length=10,choices=TEAMS)
    def __str__(self):
        return self.routename


class CarType(models.Model):
    POWER_TYPES=(
        ('混','油电混合'),
        ('柴','柴油'),
        ('电','纯电驱动'),
        ('汽','汽油')
    )
    SCALE_TYPE=(
        ('大','大型客车'),
        ('中','中型客车'),
        ('小','小型客车'),
    )

    #制造公司简称
    subname=models.CharField(max_length=10)
    #制造公司
    company_name=models.CharField(max_length=20)
    #型号名称
    type_name=models.CharField(max_length=50)
    # 动力类型
    power_type = models.CharField(max_length=20,choices=POWER_TYPES)
    # 车长
    car_length = models.CharField(max_length=10)
    # 载客量
    bus_load = models.IntegerField(default=0)
    #是否属于新能源车辆
    is_new_en=models.BooleanField()
    #车辆类别
    car_scale=models.CharField(max_length=10,choices=SCALE_TYPE)
    #百公里非空调指标
    target_value1=models.IntegerField(default=0)
    #百公里空调指标
    target_value2=models.IntegerField(default=0)

    def __str__(self):
        return self.subname+self.type_name


class BusInfo(models.Model):
    """

    """
    TEAMS=(
        ('1','1队'),
        ('2','2队'),
        ('3','3队'),
        ('4','4队'),
        ('5','5队')
    )

    #车牌号
    car_id=models.CharField(max_length=20,primary_key=True)
    #线路
    route=models.ForeignKey(RouteInfo,on_delete=models.CASCADE)
    #登记时间
    published_date=models.DateTimeField('date published')
    #最后更新时间
    updated_date=models.DateTimeField('date updated',null=False)
    #车辆型号
    cartype=models.ForeignKey(CarType,on_delete=models.CASCADE)
    #所属公司
    company=models.CharField(max_length=20)
    #所属车队
    team=models.CharField(max_length=10,choices=TEAMS)
    #描述
    describe=models.CharField(max_length=50)
    #是否报废
    scrap=models.BooleanField(null=False,default=False)
    #车辆识别号
    car_num=models.CharField(max_length=25,default='')
    #发动机号
    en_num=models.CharField(max_length=20,default='')
    #车型文本
    cartype_value=models.CharField(max_length=30,default='')

    def getPowerType(self):
        return self.cartype.power_type

    def get_car_length(self):
        return self.cartype.car_length

    def __str__(self):
        return self.car_id

    def re_set_type_id(self):
        ct=CarType.objects.get(type_name=self.cartype_value)
        if ct is not None:
            self.cartype=ct

class MonthlyFeedback(models.Model):
    #车辆信息外主键
    carInfo=models.ForeignKey('BusInfo',on_delete=models.CASCADE)
    #所属时间
    date=models.DateField("date published")
    #所属线路,车辆会抽调线路
    route=models.CharField(max_length=20,default='')
    #行驶公里
    mileage=models.FloatField(max_length=15,default=0)
    #油耗
    oilwear=models.FloatField(max_length=15,default=0)
    #二次保养补贴油量
    maintain=models.FloatField(max_length=3,default=0)
    #跟车实习补贴油量
    follow=models.FloatField(max_length=3,default=0)





class CarChangeLog(models.Model):
    # 变更车辆
    carInfo = models.ForeignKey(BusInfo, on_delete=models.CASCADE)
    # 更新日期
    pub_date = models.DateTimeField('date published')
    # 更新内容
    change_value = models.CharField(max_length=50)
