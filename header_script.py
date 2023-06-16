# Script to copy content from header_extend.html to navbar-authenticated.html

header_file = '/edx/src/edx-plugin/edx_plugin/templates/edx_plugin/header_extend.html'
navbar_file = '/edx/app/edxapp/edx-platform/lms/templates/header/navbar-authenticated.html'

# Read the content from header_extend.html
with open(header_file, 'r') as header:
    header_content = header.read()

# Append the content to navbar-authenticated.html
with open(navbar_file, 'a') as navbar:
    navbar.write(header_content)

print('Content copied successfully!')
