from strawberry_django_plus import gql
from strawberry_django_plus.gql import relay
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from .models import Milestone, Project
from typing import List, Optional


@gql.django.type(Milestone)
class MilestoneType(relay.Node):
    name: gql.auto

@gql.django.type(Project)
class ProjectType(relay.Node):
    name: gql.auto

    @gql.django.connection()
    def milestones(self) -> List["MilestoneType"]:
        return self.milestones.all()


@gql.type
class Query:
    @gql.django.field
    def project(self, info, name: Optional[str] = None) -> Optional[ProjectType]:
        return Project.objects.get(name=name)
    
    milestone_conn: relay.Connection[MilestoneType] = gql.django.connection()



schema = gql.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
