import sentry_sdk
import sys


sentry_sdk.init(
    dsn="https://ead63d02fd9544c091baf83427e649da@o339527.ingest.sentry.io/4504868950179840",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
    # release=str(engine.sgtk.configuration_descriptor).replace(" ","@")
)