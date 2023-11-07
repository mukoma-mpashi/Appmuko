import logging
from applicationinsights.logging import LoggingHandler
from applicationinsights import TelemetryClient
import time
import os


app_insights_instrumentation_key = 'fsj6vocdxqs4mnqawfng6tjoaec8tuwaobbc8s5h'
client = TelemetryClient(app_insights_instrumentation_key)

log_filename = os.path.join(os.path.dirname(__file__), 'application.log')
logging.basicConfig(filename=log_filename, level=logging.INFO)

app_insights_handler = LoggingHandler(app_insights_instrumentation_key)
app_insights_handler.setLevel(logging.INFO)


root_logger = logging.getLogger()
root_logger.addHandler(app_insights_handler)

def log_custom_event(event_name, properties=None):
    
    client.track_event(event_name, properties=properties)
    client.flush()

def log_custom_metric(metric_name, value):
    
    client.track_metric(metric_name, value)
    client.flush()

def log_operation_duration(operation_name, start_time):
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    client.track_metric(operation_name, elapsed_time)
    client.flush()

def log_exception():
    
    try:

        result = 1 / 0
    except Exception as e:
        client.track_exception()
        client.flush()

if __name__ == '__main__':
    

    try:
        start_time = time.time()

        
        result = 10 / 2

        
        log_operation_duration('OperationDuration', start_time)

        if result != 5:
            raise Exception("Unexpected result")

    except Exception as e:
    
        log_exception()
        log_custom_event('CustomEventName', properties={'customProperty': 'customValue'})
    else:
        
        log_custom_metric('CustomMetricName', result)
