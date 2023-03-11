from boltiot import Bolt
api_key = "451760fb-c462-4b96-b0c2-34e08392543d"
device_id  = "BOLT15316359"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response)
