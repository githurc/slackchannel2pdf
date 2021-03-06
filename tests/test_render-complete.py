import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir + "/slackchannel2pdf")
from slackchannel2pdf import SlackChannelExporter

def main():    
    exporter = SlackChannelExporter(slack_token="TEST", add_debug_info=True)
    exporter._workspace_info = {
        "team": "test",
        "user_id": "U92345678"
    }
    exporter._user_names["U92345678"] = "Erik Kalkoken"
    exporter._user_names["U82345678"] = "Mei Tsukaya"
    exporter._user_names["U72345678"] = "Mr. Y"
    
    exporter._channel_names = {
        "G1234567X": "render-complete"
    }
    
    exporter.run(["render-complete"], currentdir)

if __name__ == '__main__':
    main()