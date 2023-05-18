from django.dispatch import receiver
from django.template.loader import get_template
from juntagrico.mailer import EmailSender, organisation_subject, base_dict
from juntagrico.signals import depot_changed

from gartenkoop.settings import ADMINS


@receiver(depot_changed)
def on_depot_change(sender, **kwargs):
    EmailSender.get_sender(
        organisation_subject('Ein Mitglied hat das Depot geändert'),
        get_template('juntagrico/mails/admin/depot_changed.txt').render(base_dict(kwargs)),
        bcc=[ADMINS[0][1]]
    ).send()
