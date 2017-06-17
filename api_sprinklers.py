# sprinkler_api.py
class DefaultHandler:
    def __init__(self, sprink):
        self.sprink = sprink
        pass
    
    def get(self, api_request):
        return {'running': self.sprink.isRunning(), 
            'bank': self.sprink.getRunningBank(), 
            'startTime': self.sprink.getStartTime()}

    def post(self, api_request):
        print(api_request['body'])
   
        bank = api_request['body']['bank']
        if api_request['body']['run'] is True:
            self.sprink.start_bank(bank)
            return {'message': 'Starting', 'bank' : bank}
        else:
            self.sprink.stop_bank()
            return {'message': 'Stopping', 'bank' : bank }