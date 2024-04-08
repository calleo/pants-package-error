# FIXME https://github.com/pex-tool/pex/issues/2395: we need to pre-seed the pex_root named cache
# with these dependencies before building for other platforms
pex_binary(
    name="__workaround_pex_issue_2395",
    dependencies=["3rdparty/python:reqs#pbipy"],
    # this PEX isn't for anything, so let's choose options that make it most efficient to build
    layout="packed"
)
