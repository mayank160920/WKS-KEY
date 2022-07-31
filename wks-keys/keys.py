# -*- coding: utf-8 -*-
# Module: KEYS-L3
# Created on: 29-03-2022
# Authors: -∞WKS∞-
# Version: 1.1.0

import base64, requests, sys, xmltodict
import headers
from getPSSH import get_pssh
import os
import json
import subprocess
import argparse
import sys
import pyfiglet
from rich import print
from typing import DefaultDict
from pathlib import Path
from pywidevine.L3.cdm import cdm, deviceconfig
from base64 import b64encode
from pywidevine.L3.getPSSH import get_pssh
from pywidevine.L3.decrypt.wvdecryptcustom import WvDecrypt

title = pyfiglet.figlet_format('WKS-KEYS v3', font='slant')
print(f'[magenta]{title}[/magenta]')
print("by -∞WKS∞-#3982")

lic_url = input("\nLicense URL: ")
MDP_URL = input("\nInput MPD URL: ")
responses = []
license_b64 = ''
pssh = get_pssh(MDP_URL)

print("\nGenerating PSSH:.....")
print(f'\nPSSH: {pssh}')


def WV_Function(pssh, lic_url, cert_b64=None):
    wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
    widevine_license = requests.post(url=lic_url, data=wvdecrypt.get_challenge(), headers=headers.headers)
    license_b64 = b64encode(widevine_license.content)
    wvdecrypt.update_license(license_b64)
    Correct, keyswvdecrypt = wvdecrypt.start_process()
    if Correct:
        return Correct, keyswvdecrypt   
correct, keys = WV_Function(pssh, lic_url)

print()
for key in keys:
    print('--key ' + key)
    print("\nAll Done .....")
