# Azure Cost Monitoring Demo Script
# This is a sample (mock API usage; update with credentials)
import requests
from datetime import datetime

URL = 'https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/query?api-version=2023-03-01'
HEADERS = {'Authorization': 'Bearer {access_token}'}
PARAMS = {
    'type': 'ActualCost',
    'timePeriod': {
        'from': str(datetime.now().date()),
        'to': str(datetime.now().date())
    }
}
response = requests.post(URL, headers=HEADERS, json=PARAMS)
print(response.json())  # Shows daily spend breakdown

# Note: Replace tokens, IDs for live API. Use free tier for cost demos.