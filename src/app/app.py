##
## Main application starting point. Creates the pywebview window, associates with the start page 
## and starts the local webserver.
##
import webview

webview.create_window('pywebview-template', '../../assets/index.html',
                        width=1920, height=1080)
webview.start(http_server=True)
