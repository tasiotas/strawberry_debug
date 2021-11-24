from typing import Any

from strawberry.arguments import UNSET

from .fields import DjangoCreateMutation, DjangoDeleteMutation, DjangoUpdateMutation


def create(input_type=UNSET, permission_classes=[]) -> Any:
    return DjangoCreateMutation(input_type, permission_classes=permission_classes)


def update(input_type=UNSET, filters=UNSET, permission_classes=[]) -> Any:
    return DjangoUpdateMutation(
        input_type, filters=filters, permission_classes=permission_classes
    )


def delete(filters=UNSET, permission_classes=[]) -> Any:
    return DjangoDeleteMutation(
        input_type=None, filters=filters, permission_classes=permission_classes
    )
