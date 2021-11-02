#
# SPDX-License-Identifier: GPL-2.0-only
#

# ## Build configuration, tied to config.json in yocto-autobuilder-helpers
# Repositories used by each builder
buildertorepos = {
    "a-quick": ["poky", "meta-intel", "oecore", "bitbake",
                "meta-mingw", "meta-gplv2"],
    "a-full": ["poky", "meta-intel", "oecore", "bitbake",
                "meta-mingw", "meta-gplv2", "meta-arm", "meta-aws", "meta-agl", "meta-openembedded"],
    "non-gpl3": ["poky", "meta-gplv2"],
    "meta-mingw": ["poky", "meta-mingw"],
    "qa-extras": ["poky", "meta-mingw"],
    "meta-oe": ["poky", "meta-openembedded"],
    "meta-virt": ["poky", "meta-openembedded", "meta-virtualization"],
    "meta-intel": ["poky", "meta-intel"],
    "meta-arm": ["poky", "meta-arm"],
    "meta-agl-core": ["poky", "meta-agl"],
    "meta-aws": ["poky", "meta-aws", "meta-openembedded"],
    "qemuarm-oecore": ["oecore", "bitbake"],
    "checkuri": ["poky"],
    "check-layer": ["poky", "meta-mingw", "meta-gplv2"],
    "check-layer-nightly": ["poky", "meta-agl", "meta-arm", "meta-aws", "meta-intel", "meta-openembedded", "meta-virtualization", "meta-ti", "meta-security"],
    "docs": ["yocto-docs", "bitbake"],
    "default": ["poky"]
}

# Repositories used that the scripts need to know about and should be buildbot
# user customisable
repos = {
    "yocto-autobuilder-helper": ["https://github.com/gholang/yocto-autobuilder-helper", "master"],
    "poky": ["https://github.com/gholang/poky", "master"],
    "meta-intel": ["git://git.yoctoproject.org/meta-intel", "master"],
    "meta-arm": ["git://git.yoctoproject.org/meta-arm", "master"],
    "meta-agl": ["https://git.automotivelinux.org/AGL/meta-agl", "next"],
    "meta-aws": ["https://github.com/aws/meta-aws.git", "master"],
    "meta-ti": ["git://git.yoctoproject.org/meta-ti", "master"],
    "meta-security": ["git://git.yoctoproject.org/meta-security", "master"],
    "oecore": ["git://git.openembedded.org/openembedded-core", "master"],
    "bitbake": ["git://git.openembedded.org/bitbake", "master"],
    "meta-qt4": ["git://git.yoctoproject.org/meta-qt4", "master"],
    "meta-qt3": ["git://git.yoctoproject.org/meta-qt3", "master"],
    "meta-mingw": ["git://git.yoctoproject.org/meta-mingw", "master"],
    "meta-gplv2": ["git://git.yoctoproject.org/meta-gplv2", "master"],
    "meta-openembedded": ["git://git.openembedded.org/meta-openembedded", "master"],
    "meta-virtualization": ["git://git.yoctoproject.org/meta-virtualization", "master"],
    "yocto-docs": ["git://git.yoctoproject.org/yocto-docs", "master"]
}

trigger_builders_wait_shared = [
    "qemuarm", "qemuarm-alt", "qemuarm64", "qemuarm-oecore",
    "qemumips", "qemumips64",
    "multilib",
    "qemuppc",
    "qemux86", "qemux86-alt",
    "qemux86-64", "qemux86-64-alt",
    "qemux86-64-x32", "qemux86-world",
    "edgerouter",
    "genericx86", "genericx86-alt",
    "genericx86-64", "genericx86-64-alt",
    "beaglebone", "beaglebone-alt",
    "pkgman-non-rpm",
    "pkgman-rpm-non-rpm", "pkgman-deb-non-deb",
    "build-appliance", "buildtools",
    "non-gpl3", "wic",
    "poky-tiny", "musl-qemux86", "musl-qemux86-64", "no-x11",
    "qa-extras", "qa-extras2",
    "check-layer", "meta-mingw",
    "qemuarm64-armhost"
]

trigger_builders_wait_quick = trigger_builders_wait_shared + [
    "oe-selftest", "reproducible", "qemux86-64-ptest-fast", "qemuarm64-ptest-fast"
]

trigger_builders_wait_full = trigger_builders_wait_shared + [
    "qemumips-alt", "edgerouter-alt", "qemuppc-alt", "qemux86-world-alt",
    "oe-selftest-ubuntu", 
    "reproducible-ubuntu", 
    "qemux86-64-ptest", "qemux86-64-ltp", "qemuarm64-ptest", "qemuarm64-ltp", 
    "meta-intel", "meta-arm", "meta-aws", "meta-agl-core"
]

trigger_builders_wait_quick_releases = {
    "zeus" : trigger_builders_wait_quick + ["mpc8315e-rdb"],
    "thud" : trigger_builders_wait_quick + ["mpc8315e-rdb"],
    "sumo" : trigger_builders_wait_quick + ["mpc8315e-rdb"]
}

trigger_builders_wait_full_releases = {
    "zeus" : trigger_builders_wait_full + ["mpc8315e-rdb-alt"],
    "thud" : trigger_builders_wait_full + ["mpc8315e-rdb-alt"],
    "sumo" : trigger_builders_wait_shared + ["qemumips-alt", "edgerouter-alt", "mpc8315e-rdb-alt", "qemuppc-alt", "qemux86-world-alt",
                                             "oe-selftest-ubuntu"]
}

trigger_builders_wait_perf = ["buildperf-ubuntu2004",]

# Builders which are individually triggered
builders_others = [
    "meta-oe", "meta-virt",
    "bringup",
    "qemuarm-armhost",
    "check-layer-nightly",
    "auh"
]

subbuilders = list(set(trigger_builders_wait_quick + trigger_builders_wait_full + trigger_builders_wait_perf + builders_others))
builders = ["a-quick", "a-full", "docs"] 

# ## Cluster configuration
# Publishing settings
sharedrepodir = "/srv/autobuilder/repos"
publish_dest = "/srv/autobuilder/autobuilder.yoctoproject.org/pub"

# Web UI settings
web_port = 8010

# List of workers in the cluster
workers_ubuntu = ["ubuntu2004-ty-1", "ubuntu2004-ty-2", "ubuntu1804-ty-1", "ubuntu1804-ty-2", "ubuntu1804-ty-3", "ubuntu1604-ty-1"]

workers = workers_ubuntu 

workers_bringup = []
# workers with wine on them for meta-mingw
workers_wine = ["ubuntu1804-ty-1", "ubuntu1804-ty-2", "ubuntu1804-ty-3"]
workers_buildperf = ["perf-ubuntu2004",]
workers_arm = ["ubuntu1804-arm-1"]

all_workers = workers + workers_buildperf

# Worker filtering for older releases
workers_prev_releases = {
    "hardknott" : ("ubuntu1604", "ubuntu1804", "ubuntu2004", "perf-"),
    "gatesgarth" : ("ubuntu1604", "ubuntu1804", "ubuntu1904", "ubuntu2004", "perf-"),
    "dunfell" : ("ubuntu1604", "ubuntu1804", "ubuntu1904", "ubuntu2004", "perf-"),
    "zeus" : ("ubuntu1604", "ubuntu1804", "ubuntu1904", "perf-"),
    "warrior" : ("ubuntu1604", "ubuntu1804", "ubuntu1904", "perf-"),
    "thud" : ("ubuntu1604", "ubuntu1804", "ubuntu1904", "perf-"),
    "sumo" : ("ubuntu1604", "ubuntu1804", "perf-")
}

# Worker configuration, all workers configured the same...
# TODO: support per-worker config
worker_password = "pass"
worker_max_builds = None
notify_on_missing = None

# Some builders should only run on specific workers (host OS dependent)
builder_to_workers = {
    "pkgman-rpm-non-rpm": workers_ubuntu,
    "oe-selftest-ubuntu": workers_ubuntu,
    "reproducible-ubuntu": workers_ubuntu,
    "meta-mingw": workers_wine,
    "buildperf-ubuntu2004": ["perf-ubuntu2004"],
    "default": workers
}
