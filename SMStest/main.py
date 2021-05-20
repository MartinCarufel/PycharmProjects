import clx.xms
import requests

client = clx.xms.Client(service_plan_id='c058e3f76d2840d4b011c2a0280f38f0', token='5b262ef13ba5473f9b3b904d01373be4')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = '19809997005'
create.recipients = {'15149622278'}
create.body = 'This is a test message from your Sinch account'

try:
  batch = client.create_batch(create)
except (requests.exceptions.RequestException,
  clx.xms.exceptions.ApiException) as ex:
  print('Failed to communicate with XMS: %s' % str(ex))
