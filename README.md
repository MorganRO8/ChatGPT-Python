# ChatGPT-Python

![logo](https://github.com/MorganRO8/ChatGPT-Python/assets/47795945/549ecdb5-00d1-4702-a01d-9d2696445246)
(logo made by using stable diffusion to combine the chatgpt and python logos, yes, it's silly.)

A simple tool for those with chatgpt plugin access to allow for the local execution of code in a virtual environment.

To use the plugin, you'll need chatgpt plugin access, a linux computer (I'm pretty sure at least), and the packages flask and flask-cors installed using pip.

Once you have those, open a terminal and run 'python app.py' to start the server. Then, in your browser, open up chatgpt, click plugins, scroll down to the plugin store, then click 'develop your own plugin'. In this field type localhost:3333 and submit, it should now install and connect to your local plugin, allowing python commands to be run directly by chatgpt.

Okay coo, but why?

This enables quite a few possibilities, but generally think along the lines of "Hey chatgpt, write code that does {this} and then execute that code locally, and make sure it doesn't run into errors" and boom, it'll do just that. 

If you have any idea for more specific functions to add to the plugin, please, let me know!

Happy chatting :-)
