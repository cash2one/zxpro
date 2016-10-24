#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xhzxpro.settings")

    from xhzx.models import MnTAd

    print MnTAd.objects.all()
