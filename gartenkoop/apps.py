from django.apps import AppConfig


class GartenkoopConfig(AppConfig):
    name = 'gartenkoop'
    verbose_name = "gartenkooperative"

    def ready(self):
        # add export resources
        from juntagrico.admins.subscription_admin import SubscriptionAdmin
        from gartenkoop.resources.subscription import SubscriptionWithAddressResource
        SubscriptionAdmin.resource_classes.append(SubscriptionWithAddressResource)

        # disallow sending from private email address
        from juntagrico.entity.member import Member
        original_all_emails = Member.all_emails
        def all_emails(self):
            return [(identifier, email) for identifier, email in original_all_emails(self) if identifier != 'private']
        Member.all_emails = all_emails
