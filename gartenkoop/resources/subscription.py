from import_export.fields import Field
from juntagrico.config import Config

from juntagrico.resources.subscription import SubscriptionResource


class SubscriptionWithAddressResource(SubscriptionResource):
    primary_member_street = Field('primary_member__addr_street')
    primary_member_zipcode = Field('primary_member__addr_zipcode')
    primary_member_location = Field('primary_member__addr_location')

    class Meta:
        name = Config.vocabulary('subscription_pl') + ' mit Adresse'
