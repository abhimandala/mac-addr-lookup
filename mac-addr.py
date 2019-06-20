#!/usr/bin/python
import requests
import sys


def getCompanyName():
        API_KEY = "at_iNYbZNQCyHPEF7ATj9IeJmKgDmpxQ"

        print("--- MAC address vendor lookup ---")
        #MAC_ADDRESS = input('Enter MAC ADDRESS ')  #"44:38:39:ff:ef:57"
        MAC_ADDRESS = sys.argv[1]
        URL = "https://api.macaddress.io/v1?apiKey={0}&output=json&search={1}".format(API_KEY,MAC_ADDRESS)
        r = requests.get(url = URL)
        data = r.json()

        print("CompanyName : " + data['vendorDetails']['companyName'])

if __name__ == '__main__':
        getCompanyName()
