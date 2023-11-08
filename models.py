from django.db import models
import asyncio
from fast_bitrix24 import Bitrix




class Core_Supervizer(models.Model):

    REGION_CHOICES = (
        ('Чуйская', 'Чуйская'),
        ('Иссык-кульская', 'Иссык-кульская'),
        ('Нарынская', 'Нарынская'),
        ('Джалал-Абадская', 'Джалал-Абадская'),
        ('Баткенская', 'Баткенская'),
        ('Ошская', 'Ошская'),
        ('Таласская', 'Таласская')
    )

    region = models.CharField(max_length=50, choices=REGION_CHOICES, verbose_name = 'Область')
    supervizer_id = models.BigIntegerField(verbose_name = 'Супервайзер_ID')
    supervizer_surname = models.CharField(max_length=100, primary_key=True, verbose_name = 'ФИО супервайзера')


    def __str__(self) -> str:
        return self.supervizer_surname


    class Meta:
         verbose_name = 'Супервайзеры'
         verbose_name_plural = 'Супервайзеры'

class user_id(models.Model):


    bx_id = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True,verbose_name = 'Область')

    teleid = models.BigIntegerField( verbose_name = 'Телеграм_ID',primary_key= True)
    supervizer = models.CharField(max_length=10, blank=True)
    surname = models.CharField(max_length=50, verbose_name = 'ФИО агента')
    supervizer_surname = models.ForeignKey(
        to=Core_Supervizer,
        on_delete=models.CASCADE,
        related_name='super_id',
	verbose_name = 'ФИО супервайзера'
    )  
    hydra_id_sales = models.CharField(max_length=50, blank=True, verbose_name=('Гидра_ID'))

    def __str__(self) -> str:
        return self.surname

    def save(self, *args, **kwargs):
        region_agent = self.supervizer_surname.region
        self.region = region_agent
        superv_id = self.supervizer_surname.supervizer_id
        self.supervizer = superv_id
        name = self.surname

        async def main():
            if not self.bx_id:
                 webhook = "" # токен с битрикс24
                 b = Bitrix(webhook)
                 method = 'crm.deal.userfield.update'
                 params = {
                     "id": 1283,
                     'fields': {
                         "LIST": [{"VALUE": f'{name}'}]

                     }}

                 test = await b.call(method, params)
            else:
                webhook = "" # токен с битрикс24
                b = Bitrix(webhook)
                method = 'crm.deal.userfield.update'
                params = {
                    "id": 1283,
                    'fields': {
                        "LIST": [{"ID": f'{self.bx_id}'},
                            {"VALUE": f'{name}'}]

                    }}

                test = await b.call(method, params)
                return test
        asyncio.run(main())

        async def main2():
            webhook = "" # токен с битрикс24
            b = Bitrix(webhook)
            method = 'crm.deal.userfield.get'
            params = {
                "id": 1283}

            test = await b.call(method, params)

            test2 = test['LIST']
            for i in test2:

                if i['VALUE']==name:

                    self.bx_id = i['ID']
        asyncio.run(main2())
        return super().save(*args, **kwargs)

    class Meta:
         verbose_name = 'Агенты'
         verbose_name_plural = 'Агенты'


class user_state(models.Model):
	tg_id = models.BigIntegerField(max_length=20, primary_key= True)
	state = models.CharField(max_length=3)


class ticket(models.Model):
       tg_id = models.BigIntegerField(max_length=200,primary_key=True, blank=True)
       ticket_title = models.TextField(max_length=200, null=True)
       paystatus  = models.TextField(max_length=200, null=True)
       cf_954_tv = models.TextField(max_length=200, null=True)
       cf_968_naim = models.TextField(max_length=200, null=True)
       cf_924_adres = models.TextField(max_length=200, null=True)
       cf_926_router= models.TextField(max_length=200, null=True)
       cf_928_tariff = models.TextField(blank=True, max_length=200, null=True)
       description = models.TextField(max_length=200, null=True)
       name = models.TextField(max_length=200, null=True)
       surname = models.TextField(max_length=200, null=True)
       number = models.TextField(max_length=200, null=True)
       number2 = models.TextField(max_length=200, null=True)   
       location = models.TextField(max_length=200, null=True)
       passport = models.TextField(max_length=200, null=True)
       passport2 = models.TextField(max_length=200, null=True) 
       provider = models.TextField(max_length=200, null=True)



       def str(self): 
           return self.tg_id

