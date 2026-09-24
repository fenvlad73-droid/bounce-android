[app]
title = Bounce Mobile
package.name = bouncegame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3,pygame
orientation = landscape
fullscreen = 1

android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.3
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_licenses = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
