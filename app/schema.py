import strawberry
import strawberry_django
from django.db import models
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry_django.relay import ListConnectionWithTotalCount


#
class User(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    user = models.ForeignKey(
        "User",
        blank=True,
        null=True,
        related_name="products",
        on_delete=models.CASCADE,
    )


@strawberry_django.type(Product)
class ProductType(strawberry.relay.Node):
    name: strawberry.auto
    size: strawberry.auto


@strawberry.django.type(User)
class UserType(strawberry.relay.Node):
    name: strawberry.auto
    products: ListConnectionWithTotalCount[ProductType] = strawberry.django.connection(prefetch_related="products")


@strawberry.type
class Query:
    user: UserType = strawberry_django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
