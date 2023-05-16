# ChatGPT-Python

![logo](https://github.com/MorganRO8/ChatGPT-Python/assets/47795945/549ecdb5-00d1-4702-a01d-9d2696445246)

(logo made by using stable diffusion to combine the chatgpt and python logos, yes, it's silly.)

The ChatGPT Local Execution Plugin is a simple tool that allows users with ChatGPT plugin access to execute Python code locally in a virtual environment. This plugin enhances the capabilities of ChatGPT by enabling the execution of code directly within the chat interface.

## Prerequisites

To use the plugin, you will need the following:

   ChatGPT plugin access
   A Linux computer (haven't tried running on any other operating systems yet)
   flask and flask-cors packages installed using pip
   python3.10-venv

## Installation and Setup

   Clone the repository or download the source code.
   Install the required packages by running the following commands in your terminal:


    pip install flask flask-cors
    sudo apt install python3.10-venv
    

   Start the server by running the following command in your terminal:

    python app.py

## Usage

   Open your web browser and navigate to the ChatGPT interface.
   Click on the "Plugins" section.
   Scroll down to the "Plugin Store" and click on "Develop your own plugin."
   In the provided field, type localhost:3333 and submit.
   The plugin will now be installed and connected to your local environment, allowing you to execute Python commands directly in ChatGPT.

## Why Use the Plugin?

The ChatGPT Local Execution Plugin offers several advantages and possibilities, such as:

   Generating code snippets: You can instruct ChatGPT to write code that performs specific tasks and execute it locally, ensuring it runs without errors.
   Customization: If you have ideas for specific functions to add to the plugin, please let us know. We are open to feedback and feature requests.

We hope you enjoy using the ChatGPT Local Execution Plugin and have productive conversations with ChatGPT. Happy coding! :-)
