# The platforms file is required to build PEX'es for the target platform (Linux). The platform
# JSON file is created by running the following command:
#
# Start the container which corresponds to the target platform (Linux):
#
# > DOCKER_DEFAULT_PLATFORM=linux/amd64 docker run -it python:3.11.8-bookworm /bin/bash
#
# Generate the platform JSON file, and prettify it:
#
# > apt update && apt install jq -y
# > pip install pex
# > pex3 interpreter inspect --markers --tags | jq
#
# Copy the output into the platform JSON file, in this repository.

files(
    name="docker_python_311_amd64",
    sources=["python_311_amd64.json"],
)
