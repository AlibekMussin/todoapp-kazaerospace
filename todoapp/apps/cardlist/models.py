from django.db import models

# Create your models here.
# class CardList(CommonFields):
#     class Meta:
#         verbose_name = 'Данные внешнего адресата'
#         verbose_name_plural = 'Данные внешних адресатов'
#
#     applicant_status = models.ForeignKey(
#         ApplicantStatus,
#         on_delete=models.DO_NOTHING,
#         verbose_name='Статус обратившегося лица',
#         null=True, blank=True,
#     )
#     delivery_methods = models.ManyToManyField(
#         DeliveryMethod,
#         verbose_name='Способы доставки',
#         blank=True,
#     )
#     is_resident = models.BooleanField(
#         default=True,
#         verbose_name='Является резидентом',
#     )
#     author_type = models.CharField(
#         choices=AuthorTypeChoices.choices,
#         verbose_name='Тип автора письма',
#         null=True, blank=True,
#         max_length=50
#     )