"""
Signals.py:
"""
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED


def item_purchased(sender, **kwargs):
    """
    item_purchased(sender, **kwargs):
    """
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != "admin@gamershub.uk":
            # Not a valid payment
            return
    else:
        return


valid_ipn_received.connect(item_purchased)
