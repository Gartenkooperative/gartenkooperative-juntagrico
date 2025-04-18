from django.apps import AppConfig


class GartenkoopConfig(AppConfig):
    name = 'gartenkoop'
    verbose_name = "gartenkooperative"

    def ready(self):
        # add export resources
        from juntagrico.admins.subscription_admin import SubscriptionAdmin
        from gartenkoop.resources.subscription import SubscriptionWithAddressResource
        SubscriptionAdmin.resource_classes.append(SubscriptionWithAddressResource)
