python_sources(
    sources=["*.py"],
    name="lib",
    dependencies=[
        "3rdparty/python:reqs#pbipy",
    ],
)

pex_binary(
    name="bin",
    # script="hello",
    dependencies=[":lib"],
    shebang="/usr/local/bin/python",
    include_tools=True,
    complete_platforms=["3rdparty/platforms:docker_python_311_amd64"],
)

docker_image(
    name="hello-app",
    image_tags=["latest"],
    dependencies=["project/src/python/hello:bin"],
    tags=["docker"],
)
